



import random

def main():
    number = random.randint(1,99)

    print("I am thinking a number between 0 to 99 ... ")
    
    guess_number=int(input("Guess the number: "))

    while guess_number != number:
     
       if guess_number > number:
          print( "its too high")
       else:
           print("its too low")    
       
       print() 
       guess=int(input("Guess a new number"))
    
    print(f"Congratulation you guess the number it a {number}")


if __name__ == "__main__":
    main()        