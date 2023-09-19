#!/usr/bin/python3
# Author: James Sperry
# Last Updated, 2023-09-19

import game_functions as game
import time


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
