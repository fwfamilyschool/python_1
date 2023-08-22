def room_3():
    print("You are in room three now. Before you there is a throne with what seems to be the skeliton of a king or ruler of some   kind.")
    print("You hear a voice that seems to come from everwhere and nowhere at the same time.")
def room_2():
    print("you are in room two now, there is a table standing before you.")
    
    
def room_1():
    print("You are standing in a room. There is a door. Go though the door?")
    choice = input("Right or Left or Neither: ") 

    if choice == "right":
        print("You go through the door on the right. ")
        room_2()
        
    elif choice == "left":
        print("You go through the door on the left. ")
        room_3()
    elif choice == "neither":
         print("you stay in the room, over the next few days, you feel your sanity slowly slip away, you stay here, in the dark, until you are nothing, but an emty courpes, you feel the very being of your soul become dark and sad. You die all alone, and the only company you have left, are you rats and bugs that fest on your body.")
         quit()
    else:
        print("make a choice: ")



    
def main():
    room_1()
    
if __name__ == "__main__":
    main()