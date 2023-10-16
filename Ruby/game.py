def intro (character):
    print("\n")
    print("==========================")
    print("Welcome to Queen's Gambit!")
    print("==========================")
    print("\n" * 2)

    character['name'] = input("Good hero, what art thou called? ")
    print("")
    print("Hail, " + character['name'] + ", you have been chosen to embark on an epic quest.")
    print("\n Please take this armor: ")
    character['inventory'].update({'armor':'Ruby Armor'})
    print("\nYou've gained " + character['inventory']['armor']+ "!")
    door_choice = input("\nNow, there are 4 doors, first door is the Magical Forest, the second door is the Dragon Layer, the third door is the Arena, and last door is you're old house but, you don't remember this house you have never heard of it, never saw it. but you lived in it before. sadly you don't know who your parents are. but, in one of these door you will find them. Now my Champion, which door wilt thou goest in? (Enter the place name.) ")
    choice_not_made = True
    while choice_not_made:
        if "forest" in door_choice:
            choice_not_made = False
            magical_forest(character)
        elif "dragon" in door_choice:
            choice_not_made = False
            dragon_lair(character)     
        elif "arena" in door_choice:
            choice_not_made = False
            arena(character)
        elif "house" in door_choice:
            choice_not_made = False
            old_house(character)
        else:
            door_choice = input("Uh Oh, please type with a calm face, voice and body. Or receive a Negative Consequence! Thank you! ")

def magical_forest(character):
    print (" You land in a pool of water but, you are not wet. ")
    print (" To the left of you, there are 64 apples scatterd around. To the right of you, there is some old riding tack. To the front of you, there is a Unicorn. To the back of you is the pool that you landed in. Which way doest thou go? ")
def dragon_lair(character):
    print ("You teleport")

def arena(character):
    pass

def old_house(character):
    pass


def main():
    character = {
        'name': "Player",
        'health': 100,
        'inventory': {'armor':"None"}
    }
    intro(character)


if __name__ == "__main__":
    main()

























































