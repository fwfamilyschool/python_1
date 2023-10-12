def Cliff_Valley_1(character):
    print("\n")
    print("GRAND CLIFF VALLEY")
    print("You are in this lovely valley with a lot of prosperity, and in the distance A BIG range of cliffs, a narrow entrance can be seen, do you want to go inside?")
    decide = input("yes or no?")
    if decide == "yes":
        Narrow_Cave(character)

    elif decide == "no": print("\n")
    print("Hate to break it to you but... CHICKEN!!")

def Narrow_Cave(character):
    print("\n")
    print("NARROW CAVE")
    decide = input("you are in a Cold narrow cave but who knows if anyone else has been in here. There is a tunnel north here and there\'s a skeleton, a kind of trophy shelve and a template with gothic lettering on your left. Do you want to look?")
    if decide == "yes":
        print("\n")
        print("It says:" + "WELCOME TO LABYRINTH IN THE CLIFFSIDE! This is an Amazingly adventurous game full of choices, problem-solving and danger, there are many great victories ahead so enjoy and don\'t die! The shelve is empty. And the skeleton has a brass lantern, a long piece of rope and an elvish sword.Do you want to take the items?")
        decide = input("Yes or no?")
        if decide == "yes":
            print("\n")
            print("Taken.")
            
            Hydra_Ravine(character)
    elif decide == "no":
        print("You leave the body.\n")
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
        response = input("do you accept this gift?")


        if response == "yes":
            print("\n")
            print("Taken.")
            Loud_Room(character)





 
def Loud_Room(character):
    print("\n")
    print("LOUD ROOM")
    decide = input("You are in a big rectangular room. Nothing else seems to be in here except a platinum bar in the middle. There are tunnels heading southeast and north from here.")
    if decide == "echo":
        print("\n")
        print("The acoustics of the room stop subtly.")
        Forge_Quarters(character)
    else:
        while decide != "echo":
            print(decide + ", " + decide + "...")
            continue



def Forge_Quarters(character):
    print("\n")
    print("FORGE QUARTERS")
    decide = input("You are in a very hot room, there are forges everywhere and the rancid smell of sulphur. There's paths going north, southwest and east.")
    if decide == ("north"):
        Iron_Dungeon(character)
    elif decide == ("southwest"):
        Reflect_Room(character)
    elif decide == ("east"):
        



        def Iron_Dungeon(character):
            print("\n")
            print("IRON DUNGEON (Northern)")
    decide = input("You enter this low lit room. You notice there are rows and rows of containment cells. there are large tunnels ahead to west, south and a ladder up.")
    if decide == ("up ladder"):
        Reflect_Room




def Reflect_Room(character):
    print("\n")
    print("REFLECT ROOM")
    decide = input("You are in a HUGE room, it looks like the wall ahead is made of a glossy ivory surface. Do you wish to investigate?")





    














def main():
    character = {
        'name' : '',
        'hitpoints' : '120',
        'inventory' : {},
    }

    name = input("WHO IS THIS?")
    response = input("Hello " + name + ", " + "Do you want to start the game?" )
    if response == "yes":
        print("\n")
        print("                                           |-----------------------------------|                                                  ")
        Cliff_Valley_1(character)


if __name__ == "__main__":
        main()















































































