#!/usr/bin/python3
# Author: James Sperry
# Last Updated, 2023-09-06

import subprocess
import sys

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


if __name__ == "__main__":
    main()
