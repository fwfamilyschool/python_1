def funds(character):
        print("You have {} gold, {} silver, and {} copper.".format(character['gold'], character['silver'], character['copper']) )
        return


def intro(character):
    character['name'] = input("What's your name? \n")

    print("Welcome, {}, you're about to embark on an amazing adventure! \n".format(character['name']))

    print("You must first select a character class.")
    class_choice = input("Your choices are: Rogue, Cleric, Fighter, or Druid. Choose one to learn more about it: ").lower()

    learn_more = True
    def class_info(class_choice):
        match class_choice:
            case "rogue" : print("The Rogue is skillful, quiet, and smart. He or she wears little armor.")
            case "cleric" : print("The cleric tends to be a healer who can wear light or heavy armor and uses magic to serve others.")
            case "fighter" : print("The fighter likes close combat and does not like being weighed down with heavy armor.")
            case "druid" : print("The druid tries to be one with nature. A strong magic user who can wear light or heavy armor.")
            case other : print("That is not a valid choice.")
        return

    class_info(class_choice)
    
    while learn_more == True:
        more = input("Do you want to know about another class? ")
        if more == "no".lower() or more == "n".lower():
            learn_more = False
            print(str(learn_more))
            break
        elif more == "yes".lower() or more == "y".lower():
            class_choice = input("Choose another class: ")
            class_info(class_choice)
        
    
    choice = input("Would you like to visit the shop? ")

    if choice.lower() == "yes" or choice.lower() == "y":
        shop(character)

    #character['inventory'] = {'armortype' : 'diamond'}

    #print(character)
    #print(character.get('inventory'))
    #print(character['inventory']['armortype'])
    
    #character['inventory'] = {'armorequipped' : False}

    

    equip = input("Would you like to equip your armor? \n")

    def equiparmor(equip):
        if equip.lower() == "yes" or equip.lower() == "y":
            character['AC'] += 3
            character['inventory']['armorequipped'] = True
        return
    
    equiparmor(equip)


    if character['inventory']['armorequipped'] == True:
        print("Your armor is equipped. \n")
        print("Your armor class is now {}. \n".format(character['AC']))
    else:
        print("Your armor class is {}. \n".format(character['AC']))


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
            case 'funds': funds(character)
            case 'list' : list_items(store_inventory)
    

    
def main():
    character = {
        'name':"",
        'class':"",
        'hitpoints':100,
        'inventory':{},
        'AC':15,
        'gold':100,
        'silver':200,
        'copper':200
    }

    intro(character)

if __name__ == "__main__":
    main()