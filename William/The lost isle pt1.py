def keys_1():
    print("these keys can unlock diferent doors." )

def quit_1(keys):
    quit

def losespot_1(keys):
    print ("you realize that you killed the knight and doomed the village, they burn you at the stake believing that you doomed them on purpose.")
    quit_1

def winspot_1(keys):
    print ("YOU HEALED THE KNIGHT AND SAVED THE VILLAGE!!!!!/n/nYOU WIN!!!!!!")
    quit_1

def path_1(keys):
    print ("as you go down the path you encounter a rabid dog, do you fight it or do you run back to the house?")
    choice = input ("'fight', 'back' or 'wait'")
    
    if choice == ("back"):
        print("you go back")
        room_3(keys)
        
    elif choice == ("fight"):
        print("you kill the dog")
        losespot_1(keys)
        
    elif choice == ("wait"):
        print ("the dog slowly comes to  you and you relize that the dog was not rabid, but was not a dog at all, rather, they were the person you were looking for, and you take it down the path to the witch to heal him")
        winspot_1(keys)
      
def yard_1(keys):
    print ("behind you there is a house, in front of you there is a path")
    choice = input ("go to house or go down path")
    
    if choice == "go to house":
        print ("you are back in the house")
        room_3(keys)
        
    elif choice == "go down path":
        path_1(keys)

def kitchen_1(keys):
    print ("in front of you there is a counter, behind you there is a door.")
    choice = input ("go back")
    
    if choice == ("back"):
        print ("you go back.")        
        room_3(keys)

    else:
        print("unknown comand, please choose 'go to counter' or 'go to door 1' or 'go to door 2'")
        kitchen_1(keys)

def room_3(keys):
    print ("you are in a room, to the left is a kitchen, to the right there is a door, in front of you there is a window, and behind you there is a door.")
    choice = input ("go to kitchen or go to door or go back")
    
    if choice == "go to kitchen":
        print ("you go into the kitchen.")
        kitchen_1(keys)
        
    elif choice == "go to door":
        print ("you are now outside, goodluck!")
        yard_1(keys)
        
    elif choice == "Greensheild":
        print ("hello Greensheild, nice to meet you again and welcome to mundes dessadari. }:)")
        room_3(keys)
        
    elif choice == "go back":
        stairs_1(keys)
        
    else:
        print("unknown comand, please choose 'go to kitchen' or 'go to door' or 'go back'")
        room_3(keys)
    
def stairs_1(keys):
    print("there is are stairs behind you, and in front of you there is a door.")
    choice = input ("open door or go up the stairs: ")
    
    if keys == True:
        if choice == "open door":
            print("you go through the door." )
        room_3(keys)
        
    if keys ==False:
        if choice == "open door":
            print("the door is locked, you can not enter." )
            stairs_1(keys)
    elif choice == "go up stairs":
        print("you go up the stairs." )
        room_2(keys)
        
    else:
        print("unknown comand, please choose 'open door' or 'go up the stairs'")
        stairs_1(keys)

def room_2(keys):
    if keys == False:
        print ("you are in the second room. behind you there is a door,\n in"
"front of you ther is a window, and some keys,\n and to your right is a stairs leading down.")
        
        choice = input ("grab keys or go down stairs or go to the door: ")
        
    elif keys == True:
        print ("you are in the second room. behind you there is a door,\n in front of you there is a window, and to your right is\n a stairs leading down.")
        choice = input ("go down stairs or go to the door: ")
    
    if choice == "grab keys": 
        print("you grab the keys." )
        keys = True
        room_2(keys)
           
    elif choice == "go down stairs":
        print("you go down the stairs.")
        stairs_1(keys)
        
    elif choice == "go to door":
        print("you are back in room 1.")
        room_1(keys)
        
        if keys == True:
                print("unknown comand, please choose 'go down stairs' or 'go to door'")
                room_2(keys)
                
        if keys == False:
                print("unknown comand, please choose 'grab keys' or 'go down stairs' or 'go to door'")
                room_2(keys)

def room_1(keys):
    print("As you wake up you remember that you are here to find the village knight/nwho has been turned into a dog by an evil witch,/nyou are to take the dog to the witch in the village down the path so she can heal him./nThere is a door. Go through the door?")
    choice = input ("yes or no: ")


    if choice == "yes":
        print("you go through the door." )
        room_2(keys)
    elif choice == "no":
        print("you stay in the room and look around, there is no longer a door, you are stuck.")
        quit()
    elif choice == "c.s":
        room_0(keys)
    else:
        print("unknown comand, please choose 'yes' or 'no'")
        room_1(keys)

def room_0(keys):
    print("Please type your name.")
    choice = input("\/ name here \/")
    
    if choice == "greensheild":
        print ("Hello Greensheild!")
        room_1(keys)
    elif choice == "fwfs":
        print ("Ah, your from the FarWestFamilySchool.")
        room_1(keys)
    else:
        print("Hello, and welcome.")
        room_1(keys)

keys = False
room_0(keys)