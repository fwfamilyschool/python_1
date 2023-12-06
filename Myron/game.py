def copper_sword():
    print("A short sword made from copper. might be usefull." )




def room_0():
    print("You have traveled far and wide to get here, the fortress of Galmore. the riches and knowledge in there may be able to help you in your quest for finding the orogins of your past. You're faced with a choice, go forward or turn back.Be warned to go further may mean certain doom. you turn to your companion and you remember what they had told you.'I will follow were you lead and do all I can to help and protect you. But I can not make this choice for you.'")
    choice = input("forward or back: ") 

    if choice == "forward":
        print("you decide that to go back now would be foulish you have come this far, you might as well continue forward, you gather your corage and enter. ")
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
    print("as you enter the fortress you hear a soft scraping sound, you turn around and to your horror the entrance is colapsing, you try to rush out but its to late. As the dust clears you realize that you should not have come here, now you will have to find another exit. As you are trying to think about what to do your companion grabs your attantion, they gesture showing you that there is a road to go down, one to the left.")
     
    choice = input("go left:")
    if choice == "left":
        print("you go left:")
        room_3()
def room_3():
    print("you are at street three")
    print("You look around the , on the left there is what looks to be a house, to the  right there is a shop. The street continues as well.")
    
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
    print("As you enter the home you notice that there is a thick layer of dust over the floor, you see a door and a staircase.")

    choice = input("door, stairs or back:")
    if choice == "door":
        print("you go through the door:")
        room_9a()

def room_9a():
    print("as you go through the door a deep stench hits you in the face")
    print("You look around and you notice rusted pots and ketchen utensles.")
    print("You also see a door across the room.") 
    choice = input("go through the door, go back or investigate.:")
    
def room_7():
    print("you continue down the street") 
    
def room_5(copper_sword = False,jammed_door = True, key = False):
    print("you enter the shop")
    print("as you enter the shop you look and see that there is a rack of old rusted swords, sheilds that have crumbled to nothing and a single short sword made from copper. on your left there is what apperes to be a back room. there is also a wooden chest.")
    print("Grab the sword, go through the door or try to open the chest")
    choice = input("Grab sword, back room, open chest:")
    
    if choice == "Grab sword":        
        print("you grab the sword")
        copper_sword = True
        room_5(copper_sword)
        room_5()
    #if copper_sword == True
    
    elif choice == "open chest":
        print("you go to open the chest but its locked. maybe there is a key somewhere.")
        print("Grab the sword, go through the door or try to open the chest")
        room_5()
    elif choice == "back room":
        if jammed_door == True:
            print("you go towards the door and push on it, it doesn't move")
            jamed_door = False
            room_5(jammed_door)
        else:
            print("the door is open")
            
    choice = input("push on the door harder or stop pushing.:")
    if choice == "push harder":
        print("you push on the door harder and the door slowly opens")
    elif choice == "stop pushing":
        print("you stop pushing on the door.")
    
    
    if __name__ == "__main__":
        room_0()
        
room_0()