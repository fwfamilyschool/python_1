#!/usr/bin/python3
# Author: James Sperry
# Last Updated, 2023-08-28
import subprocess


def not_trust_witch():
    game_text = "You see the witch and run away.  You trip on a a snake and fall into a pit of dispare.  You are sad, and crying.  You die."

    print(game_text)
    subprocess.run(["say", game_text])

    quit()
    
    
def trust_witch():
    game_text = "You trust the witch, and she gives you candy and a ride home.  You are safe."

    print(game_text)
    subprocess.run(["say", game_text])

    quit()


def go_bubble(name):
    game_text = "You swim a bit lower, and you enter the area surrounded by the air bubble. It's much larger than it looked from the outside."

    print(game_text)
    subprocess.run(["say", game_text])

    quit()


def go_pond(name):
    game_text = "You jump into the pond fully clothed.  Perhaps you should have prepared a little more.  Anyway, you see a light shining down in the depths.  As you swim closer, you notice a large air bubble that doesn't seem to be rising.  The light is coming from the air bubble. As you reach it, you stretch your arm out, and it's able to pass through.  Do you enter the bubble, and explore, or do you swim back up?\n"

    print(game_text)
    subprocess.run(["say", game_text])

    choice = input("enter or swim\n> ")
    if choice == "enter":
        go_bubble(name)
    elif choice == "swim":
        start_spot(name)
    else:
        print("Please type 'enter' or 'swim'.\n")


    quit()


<<<<<<< HEAD
def go_left():
    game_text = "You head to the meadow, and there's a lion there.  It see's you and eats you.  You have died, and nobody knows where you are. You should have left a note.\n"

    print(game_text)
    subprocess.run(["say", game_text])

    quit()
    
    
def go_right(name):
    game_text = f"You go deeper into the forest, against all common sense.  After a half hour of stumbling through the forest, \nyou come upon an old run down house. You shout, 'Hello, is anyone home?'. An old witch comes out.  The witch says, 'Hello {name}, I've been expecting you.'\n"

    print(game_text)
    subprocess.run(["say", game_text])

    while True:
        game_text = "Do you trust the witch, or run away?"

        print(game_text)
        subprocess.run(["say", game_text])

        choice = input("trust or run\n> ")
        if choice == "trust":
            trust_witch()
        elif choice == "run":
            not_trust_witch()
        else:
            print("Please type left or right.\n")


def start_spot(name):
    game_text = f"{name}, you find yourself by a pond in a dark forest.  \nIt is day time, but there is little light because of the trees. You see a path to the left, leading to a meadow, and a path to the right, leading deeper into the woods.  You could also jump into the pond.\n"

    print(game_text)
    subprocess.run(["say", game_text])

    while True:
        subprocess.run(["say", "Do you go left, right, or jump?"])
        choice = input("left, right or jump?\n> ")
        if choice == "left":
            print("You go left.\n")
            go_left()
        elif choice == "right":
            print("You go right.\n")
            go_right(name)
        elif choice == "jump":
            print("You jump into the pond.\n")
            go_pond(name)
        else:
            print("Please type left, right or jump.\n")
=======
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
>>>>>>> 66c8f36c8438c5dac9729ed156438fc7442ce5b9


def main():
    character = {
        'name': "unknown",
        'hitpoints': 50,
        'inventory': []
    }
    # name variable is just a name.  Age is the age of the person
    game_text = "What is your name?"
    subprocess.run(["say", game_text])
    name = input("What is your name? \n> ")
<<<<<<< HEAD
=======
    character['name'] = name

    # print("Hi " + name + ", how are you?")
    print(f"Hi {character['name']}, how are you?")
>>>>>>> 66c8f36c8438c5dac9729ed156438fc7442ce5b9
    
    start_spot(character)


if __name__ == "__main__":
    main()
