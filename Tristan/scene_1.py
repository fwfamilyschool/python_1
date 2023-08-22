
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
    print("The coastal town of Sandpoint has faced few trials and dangers over the course of its forty-two year history, but unfortunately, that is all about to change. Unknown to the town’s founders, they chose to build their community over the ruins of an ancient stronghold once used as laboratory and prison, a place where horrifi c experiments and unholy explorations into what divides man from monster took place. These are the Catacombs of Wrath, one of several such sites used by Runelord Alaznist’s apprentices during Thassilon’s height, a place where arcanists explored and perfected the stolen arts of lifeshaping and fleshwarping. When Thassilon fell, these catacombs went dormant, but the one buried under Sandpoint was not fated to stay that way.")
    direction = input()
    if direction == "down":
        print("The chasm before you drops off at an very steep angle. You can continue or go back.")
    else:
        print("you fall to your death.")     
    
def main():
    ironville()
    iron_mine_entrance()


if __name__ == "__main__":
    main()








   