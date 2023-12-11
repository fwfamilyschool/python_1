def Cliff_Valley_1(character):
    print("\n")
    print("GRAND CLIFF VALLEY")
    print("You are in this lovely valley with a lot of prosperity, and in the distance A BIG range of cliffs, a narrow entrance can be seen, do you want to go inside?")
    decide = input("yes or no?\n")
    if decide == "yes":
        Narrow_Cave(character)
    elif decide == "no": 
        print("\n")
        print("Hate to say it, but... CHICKEN!!")

def Narrow_Cave(character):
    print("\n")
    print("NARROW CAVE")
    decide = input("you are in a Cold narrow cave but who knows if anyone else has been in here. There is a tunnel north here and there\'s a skeleton, a kind of trophy shelve and a template with gothic lettering on your left. Do you want to look?\n")
    if decide == "yes":
        print("\n")
        print("It says:" + "WELCOME TO LABYRINTH IN THE CLIFFSIDE! This is an Amazingly adventurous game full of choices, problem-solving and danger, there are many great victories ahead so enjoy and don\'t die! The shelve is empty. And the skeleton has a brass lantern, a long piece of rope and an elvish sword.Do you want to take the items?")
        decide = input("Yes or no?")
        if decide == "yes":
            print("\n")
            print("Taken. \n")
        elif decide == "no":
            print("You leave it alone.\n")
    decide = input("You see a crack in the wall to the north that opens up into a wide passage. You hear water in that direction.\n")
    if decide == "north": 
        Hydra_Ravine(character)


def Hydra_Ravine(character):
    print("\n")
    print("HYDRA RAVINE")
    decide = input("You are on a ledge overhanging a Ravine! there's a stone bridge heading east going along the ravine.")
    if decide == "east":
        Serpent_Arena(character)

def Serpent_Arena(character):
    print("\n")
    print("SERPENT ARENA")
    decide = input("you approach a big structure that seems to be made out of black metal. A fearsome-looking hydra is waiting in the middle, do you wish to fight it?")
    if decide == "yes":
        print("\n")
        print("You charge at the Hydra! Your sword crashes down brutally and knocks it into dreamland!")
    elif decide == "no":
        print("\n")
    response = input("Do you want to finish the Hydra off?")

    if response == "no":
        print("\n")
        print("The Hydra, grateful and confused, thanks you and slithers behind one of the grooves an brings out a beutiful crystal hydra skull and wants you to have it.")
        response = input("do you accept this gift?\n")

        if response == "yes":
            print("\n")
            print("Taken. \n")
    print("The hydra thanks you for your mercy. He vows to help you when you are in need.")
    if response == "look":
        print("You are in the middle of a big arena, there are bridges northeast and west from here.")
    elif response == "northeast":
        Loud_Room(character)

 
def Loud_Room(character):
    print("\n")
    print("LOUD ROOM")
    decide = input("You are in a big rectangular room. Nothing else seems to be in here except a platinum bar in the middle. There are tunnels heading southeast and north from here.\n")
    if decide == "echo":
        print("\n")
        decide = input("The acoustics of the room stop subtly.\n ")
        if decide == ("north"):
            pass
        elif decide == "pick up bar":
            print("\n")
            print("Taken.")
    else:
        while decide != "echo":
            print(decide + ", " + decide + "...")




def Forge_Quarters(character):
    print("\n")
    print("FORGE QUARTERS")
    decide = input("You are in a very hot room, there are forges everywhere and the rancid smell of sulphur. There's paths going north, southwest and east.\n")
    if decide == ("north"):
        Iron_Dungeon_Northern(character)
    elif decide == ("southwest"):
        Reflect_Room(character)
    elif decide == ("east"):

        



        def Iron_Dungeon_Northern(character):
            print("\n")
            print("IRON DUNGEON (NORTHERN)")
    decide = input(" You are in the northern part of the room, as you enter this low lit room. You notice there are rows and rows of containment cells. there are large tunnels ahead to west, south and a ladder up.\n")
    if decide == ("up ladder"):
        Reflect_Room
    elif decide == ("south"):
        Iron_Dungeon_Southern(character)
    elif decide == "west": 
        Grand_Geyser(character)





def Reflect_Room(character):
    print("\n")
    print("REFLECT ROOM")
    decide = input("You are in a HUGE room, it looks like the wall ahead is made of a glossy ivory surface. Do you wish to investigate")
    if decide == "yes":
        print("You come in front of this substance and you dont see any thing except a broken mirror shard that looks like a arrowhead on the floor by your feet.")
    if decide == "take":
        print('Taken, you try and look for how it broke and and you find somthing out of the ordinary')
        print('it looks like this: It looks like a key hole.')
    print('  _______  ')
    print(' /       \ ')    
    print(' |   |   |')
    print(' \______ /  ')





def Iron_Dungeon_Southern(character):
    print("\n")    
    print("IRON DUNGEON (SOUTHERN)")
    decide = input("You are in the southern part of the dungeon, a lot of cells as usual. there aren't any passages but what you do notice is a ")




def Grand_Geyser(character):
    print("\n")
    print("GRAND GEYSER")





























































def main():
    character = {
        'name' : '',
        'hitpoints' : '120',
        'inventory' : {},
    }

    character['name'] = input("WHO IS THIS?\n")
    response = input("Hello, " + character['name'] + "," + " do you want to start the game?\n")
    if response == "yes":
        print("\n")
        print("                                           |-----------------------------------|                                                  ")
        Cliff_Valley_1(character)


if __name__ == "__main__":
        main()

