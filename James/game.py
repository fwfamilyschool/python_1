#!/usr/bin/python3
# Author: James Sperry
# Last Updated, 2023-09-19

import subprocess
import sys
import game_functions as game
import time

# OS Specific imports
if sys.platform == "win32":
    windows = True
else:
    windows = False


def not_trust_witch():
    game_text = "You see the witch and run away.  You trip on a a snake and fall into a pit of dispare.  You are sad, and crying.  You die."

    print(game_text)
    if windows == False:
        subprocess.run(["say", game_text])

    quit()
    
    
def trust_witch():
    game_text = "You trust the witch, and she gives you candy and a ride home.  You are safe."

    print(game_text)
    if windows == False:
        subprocess.run(["say", game_text])

    quit()


def go_bubble(character):
    game_text = "You swim a bit lower, and you enter the area surrounded by the air bubble. It's much larger than it looked from the outside."

    print(game_text)
    if windows == False:
        subprocess.run(["say", game_text])

    quit()


def go_pond(character):
    game_text = "You jump into the pond fully clothed.  Perhaps you should have prepared a little more.  Anyway, you see a light shining down in the depths.  As you swim closer, you notice a large air bubble that doesn't seem to be rising.  The light is coming from the air bubble. As you reach it, you stretch your arm out, and it's able to pass through.  Do you enter the bubble, and explore, or do you swim back up?\n"

    print(game_text)
    if windows == False:
        subprocess.run(["say", game_text])

    choice = input("enter or swim\n> ")
    if choice == "enter":
        go_bubble(character)
    elif choice == "swim":
        start_spot(character)
    else:
        print("Please type 'enter' or 'swim'.\n")


    quit()


def go_left():
    game_text = "You head to the meadow, and there's a lion there.  It see's you and eats you.  You have died, and nobody knows where you are. You should have left a note.\n"

    print(game_text)
    if windows == False:
        subprocess.run(["say", game_text])

    quit()


def go_meadow(character):
    game_text = "You head to the meadow, and there's a lion there.  It notices you and raises it's head to stair you straight in the eye.  You feel a challenge.\nDo you fight, or flee?"

    print(game_text)

    if windows == False:
        subprocess.run(["say", game_text])
    
    choice = input("fight or flee\n> ")
    if choice == "flee":
        game_text = "You turn around and sprint as fast as you can.  \nFortunatley, it's much quicker than you, and pounces on you with no trouble.  Fortunate for him, not for you. It eats you.  You have died, and nobody knows where you are. You should have left a note.\n"

        print(game_text)
        if windows == False:
            subprocess.run(["say", game_text])

        quit()
    elif choice == "fight":

        pass
    else:
        print("What did you just type?!")
        go_meadow(character)
    
    
    
def go_right(character):
    print("You go deeper into the forest, against all common sense.  After a half hour of stumbling through the forest, \nyou come upon an old run down house. ")
    print(f"You shout, 'Hello, is anyone home?'\n An old witch comes out.  The witch says, 'Hello, {character['name']}, I've been expecting you.'\n")
    
    print("Do you trust the witch, or run away?")
    choice = input("trust or run\n> ")
    if choice == "trust":
        trust_witch()
    elif choice == "run":
        not_trust_witch()
    else:
        print("Please type left or right.\n")
        go_right(character)


def start_spot(character):
    game_text = f"{character['name']}, you find yourself by a pond in a dark forest.  \nIt is day time, but there is little light because of the trees.  You see a path to the left, leading to a meadow, and a path to the right, leading deeper into the woods. Or you can jump in the pond.\n"
    
    print(game_text)
    if windows == False:
        subprocess.run(["say", game_text])

    choice = input("left, right or jump?\n> ")
    if choice == "left":
        print("You go left.\n")
        go_meadow(character)
    elif choice == "right":
        print("You go right.\n")
        go_right(character)
    elif choice == "jump":
        print("You go right.\n")
        go_pond(character)
    else:
        print("Please type left, right or jump.\n")
        start_spot(character)


def main():
    character = {
        'name': "unknown",
        'hitpoints': 50,
        'inventory': []
    }
    # name variable is just a name.  Age is the age of the person
    game_text = "What is your name?"
    if windows == False:
        subprocess.run(["say", game_text])

    name = input("What is your name? \n> ")
    character['name'] = name

    print(f"Hi {character['name']}, how are you?")
    
    start_spot(character)


def game_loop(current_location, player_stats):
  print("#############################################################################")
  player_stats = game.get_player_stats(name)

  # Get Location information
  location_name, location_description, location_type = game.get_location_info(current_location)

  # # Get Location Description
  # location_description = game.get_location_description(current_location)

  # # Find out if you can rest
  # location_type = game.get_location_type(current_location)

  # Get all paths from this location
  location_paths = game.get_paths(current_location)

  # Basic Location Options
  if location_type == "RestSite":
    location_options = ["(e) Explore", "(v) See your inventory", "(i) See nearby items", "(r) Rest Here", "(q) Quit the game"]
    options = ["e", "i", "r"]
  else:
    location_options = ["(e) Explore", "(v) See your inventory", "(i) See nearby items", "(q) Quit the game"]
    options = ["e", "i", "q"]


  # Print stuff to the screen
  print(f"Your current location is: {location_name} - {current_location}")
  print(f"Your hitpoints: {player_stats['hitpoints']}/{player_stats['max_hp']}\n")
  game.slowPrint(f"Description: {location_description}\n")

  print("Location Options:")
  for option in location_options:
    print(f"\t{option}")

  print("\nNavigation:")

  for path in location_paths:
    # print(f"\t({path}) {location_paths[path]['name']} - Path ID: {location_paths[path]['path_id']} - Destination ID:{location_paths[path]['destination']}")
    print(f"\t({path}) {location_paths[path]['name']}")

  # Get user input to do something in game
  userInput = ""
  while userInput not in options:
    userInput = input("\nCommand: ")
    if userInput == "":
      game_loop(current_location, player_stats)
    elif userInput == "e":
      game.explore(current_location)
    elif userInput == "r":
      if location_type == "RestSite":
        game.rest(player_stats)
      else:
        print("This is not a location you may rest at.")
    elif userInput == "i":
      game.show_location_items()
    elif userInput == "v":
      game.show_inventory(player_stats)
    elif userInput < str(len(location_paths)):
      # Travel to location selected
      destination_id = game.travel(current_location, location_paths[int(userInput)]['path_id'], player_stats)
      time.sleep(4)
      game_loop(destination_id, player_stats)
    elif userInput == "q":
      # print(f"It's been fun, {name}.  I hope you come back soon.")
      print("It's been fun.  I hope you come back soon.")
      quit()
    else:
      game.slowPrint("Please enter a valid option.")


if __name__ == "__main__":
  print("Hello Adventurer.  Are you ready for a world of monsters and loot?")
  name = input("Let's start with your name: ")
  # name = "James"
  print("Good luck, " +name+ ".\n")
  player_stats = game.get_player_stats(name)

  while True:
    game_loop(player_stats['location'], player_stats)
