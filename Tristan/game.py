import random

money = 50
inventory_list = ['rations', 'armor', 'weapons']

# splintmall
# iron longsword
# shield


#Do a while loop or a case and break statement


d20 = random.randint(1,20)
goblin_ac = 18


def ironville():
    print('''Welcome to Ironville where the highest quality iron ore is mined
    and shipped to build the kingdom. You can go east, west, or south''')
    direction = input('Where do you want to go? ')
    if direction == 'east south west ':
        if east: 
            print('in front of you see a crossroads. You can go east west or south')
        if south:     
            print(d20)
        
        if d20 > goblin_ac:
            print('hit')
    else:
        print('You exit the town and head to the mine.')

s
def main():
    ironville()
    iron_mine_entrance()


if __name__ == "__main__":
    main()
    