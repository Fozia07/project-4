# Hangman python project


import random

word=["apple","canada","flower","loin","cabbage"]

choice=random.choice(word)
attempt=6
print("-"*60)
print("Python Hangman Project ")
print("_"*60)
guess_letters=[]
print("_"*len(choice))

while attempt > 0:
   guess=input("Guess the letter : ").lower()

   if len(guess) != 1 or not guess.isalpha():
    print("write one alphabet only")
    continue
   if guess in guess_letters:
     print("This letter already guess choose anoter letter")
     continue

   guess_letters.append(guess)

   if guess in choice:
     print("Correct guess!")

   else:
     attempt -= 1
     print(f"Wrong {attempt} attempt remaining")

   display_word= "".join(letter if letter in guess_letters else "_"for letter in choice)    
   
   print(display_word)

   if "_" not in display_word:
     print(f"Congratulation! the correct word is {choice}")
     break
else:
  print(f"Game over! coreect word is {choice}")   