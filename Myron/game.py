def room_2():
    print("")
def room_1():
    print("as you enter the fortress you hear a soft scraping sound, you turn around and to your horror the entrance is colapsing, you try to rush out but its to late. As the dust clears you realize that you should not have come here, now you will have to find another exit. As you are trying to think about what to do your companion grabs your attantion, they gesture showing you that there are two paths to go ")
    
    
def room_0():
    print("You have traveled far and wide to get here, the fortress of Galmore. the riches and knowledge in there may be able to help you in your quest for finding the orogins of your past. You're faced with a choice, go forward or turn back.Be warned to go further may mean certain doom. you turn to your companion and you remember what they had told you.                       'I will follow were you lead and do all I can to help and protect you. But I can not make this choice for you.'")
    choice = input("forward or back: ") 

    if choice == "forward":
        print("you decide that to go back now would be foulish you have come this far, you might as well continue forward, you gather your corage and enter. ")
        room_1()
        
    elif choice == "back":
        print("You decide to go back nothing is worth dying for, even the mistarys of your past, as you leave you wonder what might have happend had you gone forward.")
        room_2()
    elif choice == "neither":
         print("")
         quit()
    else:
        print("make a choice: ")



    
def main():
    room_0()
    
if __name__ == "__main__":
    main()