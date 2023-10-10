from random import randint

# a function that gives the player a starting amount of money
def funds(character):
    input("\nPress Enter to begin. ")
    character['funds']['gold'] = randint(100,300)
    print(character['funds']['gold'])
    funds = character['funds']['gold']
    if funds > 200:
        print(f"\nFortune favors you! You have {character['funds']['gold']} gold.")
    elif funds > 100:
        print(f"\nNot too shabby! You have {character['funds']['gold']} gold.")
    else:
        print(f"\nYou have {character['funds']['gold']} gold. Better than a stick in the eye!")

    return

# a function that prints out a character's inventory
#def inventory(character):
    

# a function that has the player choose a character class
def character_class(final_class_choice, character):
    choice_made = False
    while choice_made == False:
        match final_class_choice.lower():
            case "rogue":
                character['class'] = 'rogue'
                choice_made = True
            case "fighter":
                character['class'] = 'fighter'
                choice_made = True
            case "cleric":
                character['class'] = 'cleric'
                choice_made = True
            case "druid":
                character['class'] = 'druid'
                choice_made = True
            case other:
                final_class_choice = input("\nI didn't understand your response. Please try again: ")
    return


# A function that informs a player about different classes.
def class_info(class_choice):
    class_input = False
    while class_input == False:
        match class_choice.lower():
            case "rogue": 
                print("\nThe Rogue is skillful, quiet, and smart. He or she wears little armor.")
                class_input = True
            case "cleric": 
                print("\nThe cleric tends to be a healer who can wear light or heavy armor and uses magic to serve others.")
                class_input = True
            case "fighter": 
                print("\nThe fighter likes close combat and does not like being weighed down with heavy armor.")
                class_input = True
            case "druid": 
                print("\nThe druid tries to be one with nature. A strong magic user who can wear light or heavy armor.")
                class_input = True
            case other:
                class_choice = input("\nThat is not a valid choice. Try again: ")
    return class_choice

# a function that introduces the player to the game
def intro(character):
    character['name'] = input("What's your name? ")

    print("\nWelcome, {}, you're about to embark on an amazing adventure! \n".format(character['name']))

    print("\nWe'll start out by seeing how much money you have.")
    funds(character)

    print("\nYou must now select a character class. \n")
    class_choice = input("Your choices are: Rogue, Cleric, Fighter, or Druid. Choose one to learn more about it: ")
    
    class_info(class_choice)
    
    learn_more = True
    while learn_more == True:
        more = input("Do you want to learn about another class? ")
        if more.lower() in  "no":
            learn_more = False
            final_class_choice = input("Now choose your class: ")      
            character_class(final_class_choice, character)                
        elif more.lower() in "yes":
            class_choice = input("Choose another class: ")
            class_info(class_choice)

    opening(character)    
    
    # choice = input("Would you like to visit the shop? ")

    # if choice.lower() == "yes" or choice.lower() == "y":
    #     shop(character)

def opening(character):
    print("\nYou're sitting in a hard wooden chair. Your hands are tied behind your back. You can't see thanks to a hood over your eyes.")
    choice = input("What do you do?\n")
    tied = True
    while tied == True:
        match choice.split():
            #case["inventory"]:
            #    inventory(character)
            case ["cut"]:
                if "knife" in character['weapons']:
                    print("Whoever put you here missed the knife up your sleeve.")
                    print("You use the keen blade to cut the rope around your hands.")
                    print("You take the hood off to reveal your surroundings - a dingy cell with a lone torch barely lighting the space.")
                    tied = False
                    continue
                else: print("You don't have anything to cut with.")
            case ["untie"]:
                if character['class'] == 'rogue':
                    print("Your fingers find the knots, and after a few moments, your hands are free.")
                    print("You take the hood off to reveal your surroundings - a dingy cell with a lone torch barely lighting the space.")
                    tied = False
                    continue
                else:
                    print("Your fingers can't quite figure out how to loosen the knots.")
            case ["yell"]:
                print("\nYou summon the guard who says, \"Shut it!\" He kicks you in the gut, knocking the wind out of you.")
            case ["break"]:
                if character['class'] == 'fighter':
                    print("You stand up and jump, falling hard and splitting the wooden chair.")
                    print("Once free, you can bring your hands to your front and use your teeth to bite the knots loose.")
                    print("You take the hood off to reveal your surroundings - a dingy cell with a lone torch barely lighting the space.")
                tied = False
                continue
            case other:
                print("That doesn't seem to work.")
        choice = input()

# a function that provides the player with the ability to purchase items
def shop(character):
    print("\n")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("*                                 *")
    print("*    Welcome to Ye Olde Shoppe!   *")
    print("*                                 *")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("\n")

    store_inventory = {
        'armor' : {'diamond' : 80, 'iron':60, 'leather': 40},
        'melee weapons' : {'sword' : 65, 'mace' : 50, 'battle axe' : 70},
        'ranged weapons' : {'javelin' : 40, 'longbow' : 75, 'crossbow' : 50},
        'potions' : {'healing' : 100, 'swiftness' : 100, 'poison' : 100},
        'other' : {'torch' : 2, 'rope' : 1, 'backpack' : 10}
    }

    def list_items(store_inventory):
        for item in store_inventory:
            print(item)
        return

    choice = ""
    while choice == "":
        choice = input("Type 'funds' to see how much money you have. Otherwise type 'list' to see what we have in stock today: ")
        match choice:
            case 'funds': print(character['funds'])
            case 'list' : list_items(store_inventory)
            case other : print("\nHey, let's keep things civil, all right?")
    

    
# the main function that sets the foundation for the game
def main():
    character = {
        'name': "",
        'class': "",
        'hitpoints': 100,
        'inventory': {},
        'AC': 13,
        'funds': {},
        'spells': [],
        'armor':"",
        'weapons': []
    }

    intro(character)

if __name__ == "__main__":
    main()