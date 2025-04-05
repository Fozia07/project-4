#Guess the number game python project (computer)

import random

def main():

    number= random.randint(1,10)
    guess=0 
    while guess != number:
       guess=int(input("Guess the number : "))
       if guess > number:
            print("Sorry your guess is too high!")
       elif guess < number:
            print("Sorry your guess is too low! ")

    print(f"Congraulation! you won your guess {number} and it is right")


if __name__ == "__main__":
    main()            
