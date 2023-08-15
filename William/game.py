def room_2():
   print("you have enterd the second room.")

def room_1():
    print("You are standing in a room. There is a door. Go through the door?")
    choice = input ("yes or no: ")


    if choice == "yes":
        print("you go through the door." )
        room_2()
    elif choice == "no":
        print("you stay in the room and look around, there is no longer a door, you are stuck.")
        quit()
    else:
        print("unknown comand, please choose 'yes' or 'no'") 
    

 
    
def main():
    while True:
        room_1()
        
if __name__==  "__main__":
    main()