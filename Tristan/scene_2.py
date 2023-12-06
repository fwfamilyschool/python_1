# Tristan's run





# my_list = "alpha beta gamma delta foo bar baz".split()

#
# words = input('Enter some words: ').split()

#
# for word in words:

# if word not in my_list:

# print('"', word, '" is not in the list', sep='')

# break

# else:

# verb = 'are all' if len(words) > 1 else 'is'

# print(' and '.join(words), verb, 'in the list!')


# splintmall

#iron longsword

#shield


# Do a while loop or a case and break statement


def main():
  ironville()
  iron_mine_entrance()
  main_room()
  oval_room()
  room_3()
  room_4()

def ironville():
  print("""Welcome to Ironville where the highest quality iron ore is
  mined and shipped to build the kingdom. You can go east, west, or
  south""")
  direction = input('what do you want to do?')
  if direction == 'east':
    print('in front of you you see a crossroads. You can go east west or south')
  else:
    print('You exit the town and head to the mine.')

def iron_mine_entrance():
  print("""You walk up to the mine entrance you see a group of 10 soldiers.
  You see a sign it reads "danger Orcs! Goblins! you see a set of rails
  leading into the mine.""")
  action = input("Choose enter or leave: ")
  if action == "enter":
    print("""Entering the mine you see you see a pickaxe on the ground.
    The air it is damp. The rails are blocked by a barricade.""")
    action = input ("do You want take the pickaxe?")
    if action == "yes":
      print("you use the pickaxe to break throughthe barricade.")
    # else action = input (" you take apart the barricade of stone ")
  else:
    
    print("you go back to Ironville...coward")
    ironville()

def main_room():
  print("""You see a Goblin in the middle of the room. He has his back
  to you. Since he heard you break throught the barricade he quickly turns
  around. """)
  action = input ("Option: Attack, talk or sneak by Gobblin")
  if action == "attack":
    print("You attack the goblin")
    print("You defeat the goblin")
  else:
    print(" Talk to goblin")
    print("the goblin attacks")

def oval_room():
  print("enter an oval room. There are 2 Goblins in the room")
  action = input ("attack, Talk or leave")
  # Choose: ("attack and you Succeed")
  if action == "Room":
    print("""Looking around There is iron in the walls and loose rock
    on the ground I notice the walls are all solid with no other exit.""")
  else:
    print("go to main_room ")
    
def room_3():
  print("Return to Main room")
  action = input ("Enter tunnels on East, West or South.")
  choose: ("south")
  print ("You proceed to tunnel to the South")
  print("""you see torches in this tunnel Heading south, deeper in the
  mine, thare is 2 orcs amd you see wood holding the
  roof and you see.""")
  
def room_4():
  print("Heading south, deeper in the mine, you see 2 orcs.")
  Options: ("attack, Talk, Sneak or Leave")
  Choose: ("attack and you Succeed")
  
# def room_5():
#   print("""Continuing down the tunnel. Options: Continue forward or Turn East. Choose: turn East""")
#
# def room_6():
#   print("""Leads you to another room that has 2 Orcs and 1 Gobblin.
# Options: attack, Talk, or Leave Choose: attack and you Succeed""")
#
# def room_7():
#   print("""Return to the main hallway. Options: Head North back to entrance,
#   Head East back to room, Head south going further in mine.""")
#
# def room_8():
#   print("""Choose: Head south going further in mine Entering another room
#   you meet another human. They are able to heal you""")
#
# def room_9():
#   print("""Return to Main room. Options: Enter tunnels on East, West or South.
#   Choose: You proceed to tunnel to the West. or you go south then you see 3 goblin""")
#   if name == "main":

main()