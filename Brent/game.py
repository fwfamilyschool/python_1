from random import randint

def funds(character):
        print("Let\'s roll to see how much money you\'ll have to start with.")
        input("Press Enter to begin. ")
        character['funds']['gold'] = randint(100,300)
        print("You have {} gold.").format(character['funds']['gold'])
        return


def intro(character):
    character['name'] = input("What's your name?: ")

    print("Welcome, {}, you're about to embark on an amazing adventure! \n".format(character['name']))

    print("You must first select a character class.")
    class_choice = input("Your choices are: Rogue, Cleric, Fighter, or Druid. Choose one to learn more about it: ")

    learn_more = True
    def class_info(class_choice):
        match class_choice.lower():
            case "rogue" : print("The Rogue is skillful, quiet, and smart. He or she wears little armor.")
            case "cleric" : print("The cleric tends to be a healer who can wear light or heavy armor and uses magic to serve others.")
            case "fighter" : print("The fighter likes close combat and does not like being weighed down with heavy armor.")
            case "druid" : print("The druid tries to be one with nature. A strong magic user who can wear light or heavy armor.")
            case other : print("That is not a valid choice.")
        return

    class_info(class_choice)
    
    while learn_more == True:
        more = input("Do you want to learn about another class? ")
        if more.lower() in  "no":
            learn_more = False
            print(str(learn_more))
            break
        elif more.lower() in "yes":
            class_choice = input("Choose another class: ")
            class_info(class_choice)
        
    
    choice = input("Would you like to visit the shop? ")

    if choice.lower() == "yes" or choice.lower() == "y":
        shop(character)


def shop(character):
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("*                                 *")
    print("*    Welcome to Ye Olde Shoppe!   *")
    print("*                                 *")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("\n")

    store_inventory = {
        'armor' : ['diamond', 'iron', 'leather'],
        'melee weapons' : ['sword', 'mace', 'battle axe'],
        'ranged weapons' : ['javelin', 'longbow', 'crossbow'],
        'potions' : ['healing', 'swiftness', 'poison'],
        'other' : ['torch', 'rope', 'lantern']
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
    

    
def main():
    character = {
        'name':"",
        'class':"",
        'hitpoints':100,
        'inventory':{},
        'AC':15,
        'funds':{},
    }

    intro(character)

if __name__ == "__main__":
    main()