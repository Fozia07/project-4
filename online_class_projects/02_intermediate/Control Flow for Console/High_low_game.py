#We want you to gain more experience working with control flow and Booleans in Python. To do this, we are going to have you develop a game! The game is called High-Low and the way it's played goes as follows:

#Two numbers are generated from 1 to 100 (inclusive on both ends): one for you and one for a computer, who will be your opponent. You can see your number, but not the computer's!

#You make a guess, saying your number is either higher than or lower than the computer's number

#If your guess matches the truth (ex. you guess your number is higher, and then your number is actually higher than the computer's), you get a point!

#These steps make up one round of the game. The game is over after all rounds have been played.

import random

Round = 5

def main():
 print("******HIGH LOW GAME****")
 your_score=0
for Round in range(Round):
    print(f"**Round {Round + 1}***")
    computer_number=random.randint(1,100)
    my_number=random.randint(1,100)

    print(f'your number is {my_number}')

    #asked the user to guess the number is high and low

    choice=input("Do you think your number is higher or lower than the computer's?:  ")
    
   # winner possibility
    Higher_and_correct= choice == "Higher" and my_number > computer_number
    lower_and_correct= choice == "lower"  and my_number < computer_number
   
    if Higher_and_correct or lower_and_correct : 
      print(f"your guess is right the computer number is {computer_number}")
    else:
       print(f"your guess is wrong the computer number is {computer_number}")
    


if __name__ == "__main__":   
     main()