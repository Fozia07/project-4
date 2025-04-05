#Simulate rolling two dice, and prints results of each roll as well as the total.

import random

def main():
      
    dice1=random.randint(0,6)
    dice2=random.randint(0,6)
    
    print(f"First dice {dice1}")
    print(f"Second dice {dice2}")

    sum=dice1 + dice2

    print(f"the sum of two dice is {sum}")
    
    
if __name__ =='__main__':
    main()