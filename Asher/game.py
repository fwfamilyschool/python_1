#/usr/bin/python
def room_3(name):
    while True:
        choice_3 = input("left or right\n")
        if choice_3 == "left":
            print("you ram into a wall and the train runs you over")
            quit()
        elif choice_3 == "right":
            print("you get out of the way just in time. do you go down the hall or follow the train.")
            quit()
        else:
            print("please type left or right")
            room_3(name)

def room_1(name):
  print(f"You are going home from the mall, when you forget which house is your house.")
  print("so do you go into the house on the left or the house on the right?")

  while True:
      choice = input("left or right\n")
      if choice == "left":
        print("you get home safely, but there is a big deep hole in your floor, and you accidentally drop an apple down it. \ndo you jump down and grab it or do you go back to the mall")
        room_2(name)
        
      elif choice == "right":
        print("its locked")
      else:
        print("please type left or right")
        

def room_2(name):
    choice_2 = input("jump or mall\n")
    if choice_2 == "mall":
        print("you go to the mall and buy an apple\n")
        room_1(name)
    elif choice_2 == "jump":
        print("you jump down the hole and mid air grab the apple. but then you hit the ground. it feels like metal, then you realilze that you are on a train track and there is a train coming.dodge left or dodge right")
        room_3(name)
    elif choice_2 == "no":
        print("do it.")
        room_2(name)
    else:
        print("please type jump or mall")
        room_2(name)
    
    
def main():
    name = input("put your name!\n")
    
    print(f"hi {name}")
    
    room_1(name)


if __name__ == "__main__":
    main()
