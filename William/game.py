def keys_1():
    print("these keys can unlock diferent doors." )
    
def room_4(keys):
    print ("in front of you there is a table with a sword on it, to your left there is some leather armor, and behind you there is a door")
    choice = input ("grab sword, or grab armor, or go to door.")
    
    if choice == ("grab sword")
    
    elif choice == ("grab amor")
    
    elif choice == ("go to door")
    
def kitchen_1(keys):
    print ("in front of you there is a counter with a waterskin on it, behind you there is a door, and to your right there is a another door.")
    choice = input ("go to counter or go to door 1 *behind you* or go to door 2 *to your left*")
    
    if choice == ("go to counter")
        print ("you go to the counter.")        
        kitchen_1(keys)
        
    elif choice == ("go to door 1")
        print ("you go to room_3")
        room_3
    
     if keys ==False:
        if choice == "go to door 2":
            print("the door is locked, you can not enter." )
    
     if keys == True:
        if choice == "go to door 2":
            print("you go through the door." )
            room_4
        
    else:
        print("unknown comand, please choose 'go to counter' or 'go to door 1' or 'go to door 2'")
        kitchen_1(keys)
        
def yard_1(keys):
    quit
    
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
        print ("hello Greensheild, nice to meet you again and welcome to mundes disadari. }:)")
        room_3(keys)
        
    elif choice == "go back"
        stairs_1(keys)
        
    else:
        print("unknown comand, please choose 'go to kitchen' or 'go to door' or 'go back'")
        room_3(keys)
    
def stairs_1(keys):
    print("there is a stairs behind you, and in front of you there is a door.")
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
            else:
                print("unknown comand, please choose 'go down stairs' or 'go to door'")
                room_2(keys)
                
        if keys == False:
                print("unknown comand, please choose 'grab keys' or 'go down stairs' or 'go to door'")
                room_2(keys)

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
        room_1(keys)

 
    
def main():
    keys = False
    room_1(keys)
        
if __name__==  "__main__":
    main()