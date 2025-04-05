# Simulate rolling two dice, three times. Prints the results of each die roll. This program is used to show how variable scope works.

import random

def roll_dice ():
    dice1=random.randint(0,6)
    dice2=random.randint(0,6)

    total:int=dice1 + dice2
    print(f'dice 1: {dice1}')
    print(f"dice 2: {dice2}")
    print(f"The total of two dice is {total}")
if __name__ == "__main__":

 roll_dice() 
 roll_dice() 
 roll_dice() 
