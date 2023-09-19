def Living_room (character):
    print("You are staying at home for a quiet late night, you are watching various channels on your Samsung television, and you hear suspicious banging sounds in your basement. Do you walk over to the door to the downstairs and investigate the strange sounds?")
    choice = input("Choose yes or no.")
    while choice != "yes" or choice != "no":
        if choice == "yes":
            print ("You grab your flashlight, and open the basement door slowly, but find that there is nothing causing noise, anymore.")
            Basement(character)
        elif choice == "no":
            print ("You turn away from the door and continue to watch TV, but, you see a shadow outside! You now wish you would have checked downstairs, for the thing that was making such racket!")
            print ("The thing swoops toward the window, and with a sickening sound of shattering glass, you behold a Twisted Demon! with a ear grating shriek from its dry throat, it devours you! *You Died!*")
            Living_room()
        else: choice = input("choose yes or no: ")


def Basement(character):
    choice = input("You enter the basement, and turn the lights on. you try to take a step, when a large, gaping hole opens in the ground. you fall for a long amount of time, then, you meet the ground without injury, and see that you might have fallen into some sort of tunnel! a sword lying on the ground has an eerie glow to it. Would you like to pick it up, or leave it there?")
    if choice == "pick up":
         print ("You have picked up the sword, it feels chilly to the touch, but can now light your way through the cave! you proceed on through the dark tunnel, when you notice something odd about the walls. the tunnel slowly widens into a large room.")
    elif choice == "leave sword":
            print ("You have left the sword where it is. you proceed on through the dark room.")
    if choice == "read paper":
            print ("'Hello, and welcome to Cave Crawler, World Underground! this game mainly deals with basic combat strategy, problem solving, and putting your intellect to good use. this note is also a clue to the 'Tuff' Maze. head east, south, south, west, east, west, north, east, this is where you fight the three-headed grue, south, east, this is where the salt-shelled spider crab is, and, north, west, north, east, and, south. now, you have solved the 'Tuff' Maze! have fun defeating the Infernal Skull Dragon! Don't die!' A large opening waits in front of you, do you go through the dark tunnel?")
            if choice == "yes":
                print("The tunnel is growing darker, and you get the feeling that something is watching your movements, and is probably waiting to strike. Do you still want to proceed on, or go back, and get the glowing sword?")
            if choice == "no":
               choice == input ("You continue walking through the dark halls, and also seem to still feel unsettled about what may be lurking around, you hear ominous noises, and also hear whisperings in the walls, suddenly, some unseen force flew straight through the wall, you start to feel choked, and draw your sword, seemingly from thin air, and swipe at the air! *You gained 20 Telerium!*...you feel relieved of oxegen deprivation, and stare marvellingly at the sword and its loyalty towards you... would you like to press on, with courage in your soul, or CHICKEN OUT!? ")
            if choice == "proceed":

'''
def Tuff_Maze():
    print ("You have come to the 'Tuff' Maze - clever, huh?... the entrance seems suspicious, but the feeling of adventure flares up inside you, you head inside, and you find the paths to the east, and north. which way to go?")
    if choice1 == "north":
            print ("Dead End. you have come to a dead end in the maze.")
    elif choice1 == "east":
            print ("First Quarter; there are openings to your left, heading east and south, and west. where to go?")
            if choice2 == "south":
                 print ("Second Quarter; You find openings to the south and and northern sides of the quarter. choose which direction to go.")
            while True:
                if choice2 == "south":
'''                     


def main():
    character = {
         'name' : '',
         'telerium' : 100,
         'inventory' : {},
    }
    character['name'] = input("Enter your name.")
    
    print("\n Welcome, " + character['name'] + "!")
    print("\n Here we go!")

    Living_room(character)


if __name__ == "__main__":
     main()





















