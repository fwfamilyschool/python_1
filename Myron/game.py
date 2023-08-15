def room_2():
    print("you are in room two now")
    
    
def room_1():
    print("You are standing in a room. There is a door. Go though the door?")
    choice = input("Yes or No: ") 

    if choice == "yes":
        print("You go through the door. ")
        room_2()
        
    elif choice == "no":
         print("you stay in the room, over the next few days, you feel your sanity slowly slip away, you stay here, in the dark, until you are nothing, but an emty courpes, you feel the very being of your soul become dark and sad. You die all alone, and the only company you have left, are you rats and bugs that fest on your body.")
         quit()
    else:
        print("make a choice: ")



    
def main():
    while True:
        room_1()
    
if __name__ == "__main__":
    main()