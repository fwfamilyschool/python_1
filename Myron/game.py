def room_0():
    print("You have traveled far and wide to get here, the fortress of Galmore. the riches and knowledge\
    in there may be able to help you in your quest for finding the orogins of your past. You're faced\
    with a choice, go forward or turn back.Be warned to go further may mean certain doom. you turn to\
    your companion and you remember what they had told you.'I will follow were you lead and do all I can\
    to help and protect you. But I can not make this choice for you.'")
    choice = input("forward or back: ") 

    if choice == "forward":
        print("you decide that to go back now would be foulish you have come this far, you might as well\
continue forward, you gather your corage and enter. ")
        room_1()
        
    elif choice == "back":
        print("You decide to go back nothing is worth dying for, even the mistoryes of your past, as you\
leave you wonder what might have happend had you gone forward.")
        room_2()
    else:
        print("choice is invalid:")
        room_0()

def room_2():
    print("")
def room_1():
    print("as you enter the fortress you hear a soft scraping sound, you turn around and to your horror\
the entrance is colapsing, you try to rush out but its to late. As the dust clears you realize that you\
should not have come here, now you will have to find another exit. As you are trying to think about what\
to do your companion grabs your attantion, they gesture showing you that there are two paths to go, one to the left and\
 one to the right.")
     
    choice = input("left or right:")
    if choice == "left":
        print("you go left:")
        room_3()
def room_3():
    print("you are at street three")
    print("You look around the , on the left there is what looks to be an old shop, to the  right there is a house. There is also more street.")
    
    choice = input("left right forward back:")
    if choice == "left":
        print("you go left:")
        room_9()
    if choice == "right":
        print("you go right:")
        room_5()
    if choice == "forward":
        print("you go forward:")
        room_7()
    if choice == "back":
        print("you go back:")
        room_1()
def room_9():
    print("you enter the home")
    print("As you enter the home you notice that there is a thick layer of dust over the    floor, you see a door and a staircase.")

    choice = input("door, stairs or back:")
    if choice == "door":
        print("you go through the door:")
        room_9a()

def room_9a():
    print("as you go through the door a deep stench hits you in the face")
    print("You look around and you notice rusted pots and ketchen utensles.")
    print("You also see a door across the room.") 

def room_7():
    print("you continue down the street") 
    
def room_5():
    print("you enter the shop")
if __name__ == "__main__":
  room_0()