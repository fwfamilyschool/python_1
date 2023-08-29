def keys_1():
    print("these keys can unlock diferent doors." )
    
def room_3(keys):
    print ("you are in a room, to the left is a kitchen, to the right there is a door, and in front of you there is a window.")
    choice = input ("go to kitchen or go to door")
    
    if choice == "go to kitchen":
        print ("in front of you there is a counter, there is nothing behind you, you die.")
        quit
        
    elif choice == "go to door":
        print ("you are now outside, you have escaped the house, congrats, you win!")
        quit
        
    elif choice == "hello, my name is greensheild":
        print ("hello Greensheild, nice to meet you again and welcome to mundes disadari. \n v \n ''")
    
def stairwell_1(keys):
    print("there is a stairwell behind you, and in front of you there is a door.")
    choice = input ("open door or go up the stairwell: ")
    
    if keys == True:
        if choice == "open door":
            print("you go through the door." )
        room_3(keys)
        
    if keys ==False:
        if choice == "open door":
            print("the door is locked, you can not enter." )
     
    elif choice == "go up stairwell":
        print("you go up the stairwell." )
        room_2(keys)

def room_2(keys):
    if keys == False:
        print ("you are in the second room. behind you there is a door,\n in front of you ther is a window, and some keys,\n and to your right is a stairwell leading down.")
        choice = input ("grab keys or go down stairwell or go to the door: ")
        
    elif keys == True:
        print ("you are in the second room. behind you there is a door,\n in front of you there is a window, and to your right is\n a stairwell leading down.")
        choice = input ("go down stairwell or go to the door: ")
    
    if choice == "grab keys": 
        print("you grab the keys." )
        keys = True
        room_2(keys)
           
    elif choice == "go down stairwell":
        print("you go down the stairwell.")
        stairwell_1(keys)
        
    elif choice == "go to door":
        print("you are back in room 1.")
        room_1(keys)

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