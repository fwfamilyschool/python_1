#!/usr/bin/python
# Author: James Sperry
# Last Updated, 2023-08-05

def not_trust_witch():
    print("You see the witch and run away.  You trip on a a snake and fall into a pit of dispare.  You are sad, and crying.  You die.")
    quit()
    
    
def trust_witch():
    print("You trust the witch, and she gives you candy and a ride home.  You are safe.")
    quit()


def go_meadow(character):
    print("You head to the meadow, and there's a lion there.  It notices you and raises it's head to stair you straight in the eye.  You feel a challenge.\n Do you fight, or flee?")
    
    choice = input("fight or flee\n> ")
    if choice == "flee":
        print("You turn around and sprint as fast as you can.  \nFortunatley, it's much quicker than you, and pounces on you with no trouble.  Fortunate for him, not for you. It eats you.  You have died, and nobody knows where you are. You should have left a note.\n")
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
    print(f"{character['name']}, you find yourself by a pond in a dark forest.  \nIt is day time, but there is little light because of the trees.")
    print("You see a path to the left, leading to a meadow, and a path to the right, leading deeper into the woods.\n")
    
    choice = input("left or right?\n> ")
    if choice == "left":
        print("You go left.\n")
        go_meadow(character)
    elif choice == "right":
        print("You go right.\n")
        go_right(character)
    else:
        print("Please type left or right.\n")
        start_spot(character)


def main():
    character = {
        'name': "unknown",
        'hitpoints': 50,
        'inventory': []
    }
    # name variable is just a name.  Age is the age of the person
    name = input("What is your name? \n> ")
    character['name'] = name

    # print("Hi " + name + ", how are you?")
    print(f"Hi {character['name']}, how are you?")
    
    start_spot(character)


if __name__ == "__main__":
    main()
