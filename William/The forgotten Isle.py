def keys_1():
    print("these keys can unlock three diferent doors." )
    
def stairwell_1(keys):
    print("there is a stair well behind you, and in front of you there is a door.")
    choice = input ("open door or go up the stairwell: ")
    
    if choice == "open door":
        print("the door is locked, you can not enter." )
        
    elif choice == "go up stairwell":
        print("you go up the stairwell." )
        room_2()

def room_2(keys):
    if keys == False:
        print ("you are in the second room. to your left is a door, a window, and some keys, to your right is a stairwell leading down, and a window, in front of you there is a window.")
        choice = input ("grab keys or go to the stairwell or go through the door: ")
    elif keys == True:
        print ("you are in the second room. to your left is a door, and a window, to your right is a stairwell leading down, and a window, in front of you there is a window.")
        choice = input ("go down stairwell or go through the door: ")
    
    if choice == "grab keys": 
        print("you grab the keys." )
        keys = True
        room_2(keys)
        
        
    elif choice == "go down the stairwell":
        print("you go down the stairwell." )
        stairwell_1()


def room_1(keys):
    print("You are standing in a room. There is a door. Go through the door?")
    choice = input ("yes or no: ")


    if choice == "yes":
        print("you go through the door." )
        room_2(keys)
    elif choice == "no":
        print("you stay in the room and look around, there is no longer a door, you are stuck.")
        quit()
    else:
        print("unknown comand, please choose 'yes' or 'no'") 
    

 
    
def main():
    keys = False
    room_1(keys)
        
if __name__==  "__main__":
    main()