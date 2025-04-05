# guess the number game (user)

import random


def computer_guess(x):

   low=1
   high=x
   feedback=""
   while feedback != "c":
      if low != high:
       guess=random.randint(low,high)
      else:
        guess=low

      feedback=input(f"Is {guess} is too high (H) ,too low(L) or correct (C)".lower())
      if feedback == "h":
         high = guess - 1

      elif feedback == "l":
         low = guess + 1 
    
   print(f"yeah! The computer guess your number , {guess} correct")


computer_guess(50)
