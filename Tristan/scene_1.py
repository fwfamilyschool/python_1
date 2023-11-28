
# Tristan's run





inventory_list = ['rations', 'armor', 'weapons']

# splintmall
#
# iron longsword
#
# shield

# Do a while loop or a case and break statement




def ironville():
    print("""Welcome to Ironville where the highest quality iron ore is
    mined and shipped to build the kingdom.""")
    direction = input('what do you what to do? go south east west north')
    if direction == 'east':
        print('in front of you you see a crossroads. You can go east west or south')
    else:
        print('You exit the town and head to the mine.')    

     
    
def main():
    ironville()
#     my_list = "alpha beta gamma delta foo bar baz".split() 
#  
# words = input('Enter some words: ').split() 
#  
# for word in words: 
#     if word not in my_list: 
#         print('"', word, '" is not in the list', sep='') 
#         break 
# else: 
#     verb = 'are all' if len(words) > 1 else 'is' 
#     print(' and '.join(words), verb, 'in the list!')



def iron_mine_entrance():
    print("""You walk up to the mine entrance you see a group of 10 soldiers.
You see a sign it reads "danger Orcs! Goblins! you see a set of rails
leading into the mine.""")
    action = input("Choose enter or leave: ")
    if action == "enter":
        iron_mine_room()
def iron_mine_room():
        print("""Entering the mine you see you see a pickaxe on the ground.
The air is damp. The rails are blocked by a barricade.""")
        action = input ("Do You want take the pickaxe?")
        if action == "yes":
            print("You use the pickaxe to break through the barricade.")
        else: 
            action = input ("You take apart the barricade of stone ")
    else:
        print("You go back to Ironville...coward")
        leave = ironville()
         main_room():

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
        print("The goblin attacks")
    oval_room()
def oval_room():
    print("""Enter an oval room. There are 2 Goblins in the room:
    Options: attack, Talk  or leave
        Choose: attack and you Succeed""")
    action = input ("Option: look in room")
    if action == "Room": 
        print("""Looking around There is iron in the walls and loose rockon
the ground I notice the walls are all solid with no other exit.""")
    else:
        print("Go to next room")
    room_3()
    
def room_3():
    print("""Return to Main room
*Options: Enter tunnels on East, West or South.
Choose: You proceed to tunnel to the South""")
    print("""You see torchis in this tunnel Heading south, deeper in the
    mine,you see 2 orcs amd you see wood holding the roof and
    you see.""")
 room_4()   
def room_4():
    print("""Heading south, deeper in the mine, you see 2 orcs.
Options: attack, Talk, Sneak or Leave
Choose: attack and you Succeed""")
    
def room_5():
    print("""Continuing down the tunnel. Continue forward or Turn East.
Choose: turn East""") ("""You see wood holding the roof and you see torchis
on the wall and you see the ground is rocky""")

def room_6():
    print("""Leads you to another room that has 2 Orcs and 1 Gobblin. 
Options: attack, Talk, or Leave
Choose: attack and you Succeed""") ("""After you attack them you see iorn in the walls and on
    the floor thare is rooks and ther is wood holding the roof and you see and you see the ground is rocky""")
    ("""Return to the main hallway.
 Head North back to entrance, Head East back to room, Head south going further in mine.
Head south going further in mine
Entering another room you meet another human. They are able to heal you. and you see torchis in this room
and you see
wood holding the roof and you see and you see the ground is rocke""")
def room_7():
    print("""Return to the main hallway.
Options: Head North back to entrance, Head East back to room, Head south
going further in mine.""")
def room_8():
    print("""Choose: Head south going further in mine
Entering another room """)
def room_9():
    print("""Enter tunnels on East, West or South.Choose: You proceed to
tunnel to the West. or you go south then you see 3 goblin  you see a big room with
and you see mose you see a  chest you open the chest in the ther is a gratsword
and you see  wood holding the roof and you see and you see the ground is smoth
you return to the main hallway you go down the stairs you see 3 goblins in the
room you attack them and you go in a another room you see orcs and goblin gardingther
boss it is a orc you attack all of them and you see mose on the ground  wood holding
the roof and you see and you see the ground is smoth""")

if __name__ == "__main__":
    main()








   