
# Tristan's run

import random


money = 50 
inventory_list = ['rations', 'armor', 'weapons']

# splintmall
#
# iron longsword
#
# shield

# Do a while loop or a case and break statement

d20 = random.randint(1,20)
goblin_ac = 16


def ironville():
    print('Welcome to Ironville where the highest quality iron ore is mined and shipped to build the kingdom. You can go east, west, or south')
    direction = input('what do you what to do? ')
    if direction == 'east':
        print('in front of you you see a crossroads. You can go east west or south')
        print(d20)
        if d20 > goblin_ac:  
   
            print('hit')
    else:
        print('You exit the town and head to the mine.')    

def iron_mine_entrance():
    print(".")
    direction = input(" you Entering the mine you see a pickaxe. 
Options: grab pickaxe or use fist to break through the bareakade.
Choose: You pick up the pickaxe and use it to break through the wall")
    if direction == "south":
        print("Enter MainRoom
	Option: attack, talk or sneak by Gobblin
		Choose: You attack the goblin.")     
    
def main():
    ironville()
    iron_mine_entrance()

def iron_mine_entrance():
    print("""you Entering the mine you see a pickaxe. 
Options: grab pickaxe or use fist to break through.
Choose: You pick up the pickaxe and use it to break through the wall.""")
    direction = input()
     

def room_1():
    print("""Enter MainRoom
	Option: attack, talk or sneak by Gobblin
		Choose: You attack the goblin.""")
        
def room_2():
    print("""enter an oval room. There are 2 Goblins in the room:
	Options: attack, Talk  or leave
		Choose: attack and you Succeed""")
def room_3():
    print("""Return to Main room
*Options: Enter tunnels on East, West or South.
Choose: You proceed to tunnel to the South""")
def room_4():
    print("""Heading south, deeper in the mine, you see 2 orcs.
Options: attack, Talk, Sneak or Leave
		Choose: attack and you Succeed""")
def room_5():
    print("""Continuing down the tunnel.
Options: Continue forward or Turn East.
Choose: turn East""")
def room_6():
    print("""Leads you to another room that has 2 Orcs and 1 Gobblin. 
Options: attack, Talk, or Leave
		Choose: attack and you Succeed""")
def room_7():
    print("""Return to the main hallway.
	Options: Head North back to entrance, Head East back to room, Head south going further in mine.""")
def room_8():
    print("""Choose: Head south going further in mine
Entering another room you meet another human. They are able to heal you""")
def room_9():
    print("""Return to Main room
*Options: Enter tunnels on East, West or South.
Choose: You proceed to tunnel to the West. or you go south then you see 3 goblin""")

if __name__ == "__main__":
    main()








   