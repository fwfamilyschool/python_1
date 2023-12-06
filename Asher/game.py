#/usr/bin/python
def room_3(name):
    while True:
        choice_3 = input("left or right\n")
        if choice_3 == "left":
            print("you ram into a wall and the train runs you over")
            quit()
        elif choice_3 == "right":
            print("you get out of the way just in time. do you go down the hall or follow the train.")
            room_4(name)
        elif choice_3 == "up":
            print(". .\n o")
            room_3(name)
        elif choice_3 == "down":
            print(". .\n -")
            room_3(name)
        else:
            print("you didnt think in time and the train ran you over")
            quit()

def room_4(name):
    while True:
        choice_4 = input("hall or train.\n")
        if choice_4 == "hall":
            print(f"you go down the hall and while walking you remember that the train had a sign that said {name}.")
            print("you get to the train station counter and you see a man there. what do you say?")
            talking_to_man_at_train_station_counter(name)
        elif choice_4 == "train":
            print("you run into a wall and go unconsious. a train runs you over. you die.")
            quit()
        else:
            print("please type hall or train")
            room_4(name)
            


def talking_to_man_at_train_station_counter(name):
        choice_5 = input("(0)how do i get out of here?\n(1)can i get a ride?\n(2)blub\n")
        if choice_5 == "0":
            print("he says you can't and pulls out a glock 19 and shoots you.")
            quit()
        elif choice_5 == "1":
            print("he says only if you have some fruit. do you give him your apple?\n")
            do_you_give_him_your_apple(name)
        elif choice_5 == "2":
            print("he pulls out a glock 19 and shoots you.")
            quit()
        else:
            print("please type 0, 1 or 2")
            talking_to_man_at_train_station_counter(name)

def do_you_give_him_your_apple(name):
    choice_6 = input("yes or no\n")
    if choice_6 == "yes":
        print("you give him your apple and he gives you a ride home\n")
        print("you get home. you are walking into your house when a goblin jumps on you and you knocks you unconcious.\n \n \n you wake up in a cell with none of your stuff")
        quit()
    elif choice_6 == "no":
        print("he says that if you are not going to get a ride then die then he pulls out a glock 19 and shoots you")
        quit()
    else:
        print("please type yes or no")
        do_you_give_him_your_apple(name)



    
    







def room_1(name):
  print(f"You are going home from the mall, when you forget which house is your house.")
  print("so do you go into the house on the left or the house on the right?\n")

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
        print("you jump down the hole and mid air grab the apple. but then you hit the ground. it feels like metal, then you\n realilze that you are on a train track and there is a train coming. dodge left or dodge right")
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
