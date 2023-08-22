#!/usr/bin/python
# Author: James Sperry
# Last Updated, 2023-08-05

def not_trust_witch():
    print("You see the witch and run away.  You trip on a a snake and fall into a pit of dispare.  You are sad, and crying.  You die.")
    quit()
    
    
def trust_witch():
    print("You trust the witch, and she gives you candy and a ride home.  You are safe.")
    quit()


def go_left():
    print("You head to the meadow, and there's a lion there.  It see's you and eats you.  You have died, and nobody knows where you are. You should have left a note.\n")
    quit()
    
    
def go_right(name):
    print("You go deeper into the forest, against all common sense.  After a half hour of stumbling through the forest, \nyou come upon an old run down house. ")
    print("You shout, 'Hello, is anyone home?'\n An old witch comes out.  The witch says, 'Hello, {name}, I've been expecting you.'\n")
    
    while True:
        print("Do you trust the witch, or run away?")
        choice = input("trust or run\n> ")
        if choice == "trust":
            trust_witch()
        elif choice == "run":
            not_trust_witch()
        else:
            print("Please type left or right.\n")


def start_spot(name):
    print(f"{name} finds themself by a pond in a dark forest.  \nIt is day time, but there is little light because of the trees.")
    print("You see a path to the left, leading to a meadow, and a path to the right, leading deeper into the woods.\n")
    
    while True:
        choice = input("left or right?\n> ")
        if choice == "left":
            print("You go left.\n")
            go_left()
        elif choice == "right":
            print("You go right.\n")
            go_right(name)
        else:
            print("Please type left or right.\n")


def main():
    # name variable is just a name.  Age is the age of the person
    name = input("What is your name? \n> ")

    # print("Hi " + name + ", how are you?")
    print(f"Hi {name}, how are you?")
    
    start_spot(name)


if __name__ == "__main__":
    main()
