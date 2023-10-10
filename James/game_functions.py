#!/usr/bin/env python3
import time
import sys
import json
import random


# class Monster:
#     def __init__(self, name, hp, str, dex, int):
#         self.name = name
#         self.hp = hp
#         self.str = str
#         self.dex = dex
#         self.int = int


# Slow print the text.  For fun
def slowPrint(string, speed=0.00):
  for char in string:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(speed)
  print("\b")


# Get name of location from the location_id
def get_location_info(location_id):
  location_name = "Not Found"

  f = open('game_files/Locations.json')
  data = json.load(f)
  for i in data:
    if data[i]['location_id'] == location_id:
      location_name = data[i]['name']
      location_description = data[i]['description']
      location_type = data[i]['type']
  f.close()

  return(location_name, location_description, location_type)


# Get Monster count of location
def get_monster_count(location_id):
  f = open('game_files/Locations.json')
  data = json.load(f)
  for i in data:
    if data[i]['location_id'] == location_id:
      monster_count = data[i]['maxMonsterCount']
  f.close()

  return(monster_count)


# Get paths from a location based on location_id
def get_paths(location_id):
  # get paths from a location
  paths = []
  path_list = {}

  # read the data from JSON file
  f = open('game_files/Paths.json')
  data = json.load(f)

  # Match paths that have current location as 'location1Key' in path
  for i in data:
    try:
      if location_id == data[i]['location1Key']:
        paths.append(i)
      # elif location_id == data[i]['location2Key']:
      #   paths.append(i)
    except:
      pass
  f.close()

  x = 0
  for path_id in paths:
    destination = data[path_id]['location2Key']
    name, loc_desc, loc_type = get_location_info(destination)
    path_list[x] = {}
    path_list[x]["path_id"] = path_id
    path_list[x]["name"] = name
    path_list[x]["destination"] = destination
    x = x + 1

  return(path_list)


def generate_combat_site(destination_location_id):
  pass


def generate_mob(destination_location_id):
  # read monsters for a given location
  f = open('game_files/MonsterSpawner.json')
  monster_list = json.load(f)
  f.close()

  for monster in monster_list:
    if destination_location_id == monster_list[monster]['locationKey']:
      npc = monster_list[monster]['npcDefKey']

  # generate new monster based on NPC Definition file
  f = open('game_files/NPCDef.json')
  npc_list = json.load(f)
  f.close()
  npc = npc_list[str(npc)]

  mob = {
    'name': npc['name'],
    'strength': random.randrange(npc['strength'][0], npc['strength'][1]),
    'dexterity': random.randrange(npc['dexterity'][0], npc['dexterity'][1]),
    'intelligence': random.randrange(npc['intelligence'][0], npc['intelligence'][1]),
    'itemSpawners': npc['itemSpawners'],
    'hitpoints': random.randrange(npc['hitpoints'][0], npc['hitpoints'][1]),
  }

  return(mob)


def enter_combat(destination_location_id):
  combat_site = generate_combat_site(destination_location_id)
  mob = generate_mob(destination_location_id)
  print(f"A {mob['name']} found you. Time to show him what's for!")


# Explore a location for monsters
def explore(location_id):
  print("You are exploring")
  slowPrint("....",1)
  print("You don't find anything.")
  # enter_combat(location_id)


# Travel to a new location
def travel(current_location_id, path_id, player_stats):
  # read all path data from JSON file
  f = open('game_files/Paths.json')
  location_paths = json.load(f)
  f.close()

  # Get data to calculate if you find a monster
  discoveryChance = location_paths[path_id]['discoveryChance']
  destination_location_id = location_paths[path_id]['location2Key']
  travel_success = random.randint(1, 100)

  name, loc_desc, loc_type = get_location_info(destination_location_id)

  if discoveryChance == 0:
    print(f"You are walking to {name}.")
    slowPrint("....",1)
    ambush = False
  else:
    print(f"You are walking to {name}.  Let's hope you don't get ambushed.")
    slowPrint("....",1)
    if discoveryChance < travel_success:
      ambush = False
    else:
      ambush = True

  if ambush == True:
    print("You have been ambushed.")
    success = enter_combat(destination_location_id)
    if success == True:
      destination_id = destination_location_id
    else:
      destination_id = current_location_id
  else:
    print("You have arrived.")
    destination_id = destination_location_id

  # Update player location in config
  player_config_file = 'game_files/player_stats.json'
  f = open(player_config_file)
  data = json.load(f)
  data[player_stats['name']]['location'] = destination_id

  with open(player_config_file, 'w') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)


  return(destination_id)


# Rest and fill your hitpoints
def rest(player_stats):
  print(f"You feel safe here, so you find a nice spot to take a nap.")

  # Update player location in config
  player_config_file = 'game_files/player_stats.json'
  f = open(player_config_file)
  data = json.load(f)
  data[player_stats['name']]['hitpoints'] = data[player_stats['name']]['max_hp']

  with open(player_config_file, 'w') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

  slowPrint("....",1)
  print("You feel rested.")


# Get player stats for the game.
def get_player_stats(name):
  returning = False
  # read the data from JSON file
  player_config_file = 'game_files/player_stats.json'
  f = open(player_config_file)
  data = json.load(f)

  for i in data:
    if name == i:
      # print(f"Welcome back {name}")
      returning = True
  f.close()

  if returning == False:
    print(f"You must be new here.  Welcome {name}")
    player_stats = {name: {
                          'name': name,
                          'hitpoints': 50,
                          'max_hp': 50,
                          'strength': 5,
                          'dexterity': 5,
                          'intelligence': 5,
                          'left_hand': 'none',
                          'right_hand': 'none',
                          'helmet': 'none',
                          'chestplate': 'none',
                          'leggings': 'none',
                          'gloves': 'none',
                          'boots': 'none',
                          'location': 0
                          }
                    }
    data.update(player_stats)

    # Update player list with new character
    with open(player_config_file, 'w') as f:
      json.dump(data, f, ensure_ascii=False, indent=4)

  return(data[name])


# Get items dropped at current location
def show_location_items():
  print("There doesn't seem to be anything here.")


# Get player inventory
def show_inventory(player_stats):
  print("Currently Equipped:")
  print(f"\thelmet \t\t{player_stats['helmet']}")
  print(f"\tchestplate \t{player_stats['chestplate']}")
  print(f"\tleggings \t{player_stats['leggings']}")
  print(f"\tgloves \t\t{player_stats['gloves']}")
  print(f"\tboots \t\t{player_stats['boots']}\n")
  print(f"\tleft_hand \t{player_stats['left_hand']}")
  print(f"\tright_hand \t{player_stats['right_hand']}")
  print("\nYour current inventory:")
  print("\tNothing.")
