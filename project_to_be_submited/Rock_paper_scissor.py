#Rock paper and scissor game on python project

import random 
print("-"*60)
print("Lets play Rock ,Paper or Scissor")
print("-"*60)

while True:
  user_choice=input("select your weapon (Rock , paper or scissor): ").lower()
  
  if user_choice not in ["rock", "paper", "scissor"]:
    print("It,s  not a valid choice ....")

  computer_choice = random.choice(["rock", "paper", "scissor"])
  print(f"you choose :{user_choice}")
  print(f"computer choose: {computer_choice}")
    
  if (user_choice == computer_choice):
      print("it's a tie! ")
  elif (
      (user_choice == "rock" and computer_choice == "scissor") or
      (user_choice == "scissor" and computer_choice == "paper") or
      (user_choice == "paper" and computer_choice == "rock")
    ):
      print("you win ...")
  else:
      print("you lost, the computer win...")
    
  play_again=input("you want to play again? (yes/no): ").lower()

  if play_again != "yes" : 
      print("thank you for playing")
  break

