#!/usr/bin/python3
# Author: James Sperry
# Last Updated, 2023-09-19

import game_functions as game
import time


def main(current_location, player_stats):
  print("#############################################################################")
  player_stats = game.get_player_stats(name)
  player_status = player_stats['status']

  # Get Location information
  location_name, location_description, location_type = game.get_location_info(current_location, player_status)

  # Get all staticpaths from this location
  location_paths, path_count = game.get_paths(current_location, player_status)

  # Get all Dynamic paths from this location
  mob_paths, path_count = game.get_mob_paths(current_location, path_count, player_status)

  # Basic Location Options
  if location_type == "rest_site":
    location_options = ["(e) Explore", "(i) See your inventory", "(n) See nearby items", "(r) Rest Here", "(q) Quit the game"]
    options = ["e", "i", "n", "r"]
  elif location_type == "combat_site":
    location_options = ["(r) Run", "(p) your pants", "(q) Quit the game"]
    options = ["r", "f", "q"]
  else:
    location_options = ["(e) Explore", "(i) See your inventory", "(n) See nearby items", "(q) Quit the game"]
    options = ["e", "i", "n", "q"]


  # Print stuff to the screen
  print(f"Your current location is: {location_name}")
  print(f"Your hitpoints: {player_stats['hitpoints']}/{player_stats['max_hp']}")
  print(f"Player Status: {player_status}\n")
  game.slowPrint(f"Description: {location_description}\n")

  print("Location Options:")
  for option in location_options:
    print(f"\t{option}")

  if location_type != "combat_site":
    print("\nNavigation:")
    for path in location_paths:
      # print(f"\t({path}) {location_paths[path]['name']} - Path ID: {location_paths[path]['path_id']} - Destination ID:{location_paths[path]['destination']}")
      print(f"\t({path}) {location_paths[path]['name']}")

  if location_type != "rest_site" and location_type != "town":
    print("\nOld Combat Sites:")
    for path in mob_paths:
      print(f"\t({path}) {mob_paths[path]['name']}")

  if location_type == "combat_site":
    mob_info = game.get_mob_info(current_location)
    print(f"\nThere is a {mob_info['name']} here.")
    print(f"\tHP is {mob_info['hitpoints']}")
    print(f"\tEquipment: {mob_info['itemSpawners']}")


    print("\nCombat Options:")
    print(f"\n\t(1) Attack with right hand: {player_stats['right_hand']}")
    print(f"\t(2) Attack with left hand: {player_stats['left_hand']}")

  # Get user input to do something in game
  userInput = ""
  while userInput not in options:
    userInput = input("\nCommand: ")
    try:
      userInput = int(userInput)
      command_type = "int"
    except ValueError:
      command_type = "str"

    if userInput == "":
      main(current_location, player_stats)
    elif userInput == "e":
      destination_id = game.explore(current_location, player_stats)
      main(destination_id, player_stats)
    elif userInput == "r":
      if location_type == "rest_site":
        game.rest(player_stats)
      elif location_type == "combat_site":
        print("You try to run, but you can't.  Because it's not programmed yet.  RIP")
        game.slowPrint("....",.5)
        destination_id = game.escape_combat(current_location, player_stats)
        main(destination_id, player_stats)
      else:
        print("This is not a location you may rest at.")
    elif userInput == "n":
      game.show_location_items()
    elif userInput == "i":
      game.show_inventory(player_stats)
    elif command_type == "int":
      # Choose appropriate travel location from Navigation options
      try:
        destination_id = game.travel(current_location, location_paths[int(userInput)]['path_id'], player_stats)
        time.sleep(4)
        main(destination_id, player_stats)
      except:
        try:
          destination_id, player_stats = game.travel_to_mob_site(current_location, mob_paths[int(userInput)]['path_id'], player_stats)
          time.sleep(4)
          main(destination_id, player_stats)
        except:
          game.slowPrint("Please enter a valid option.")

    elif userInput == "q":
      print(f"It's been fun, {name}.  I hope you come back soon.")
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
    main(player_stats['location'], player_stats)
