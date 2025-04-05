#Write a program that asks a user to enter a number. Your program will then double that number and print out the result. It will repeat that process until the value is 100 or greater.


def main():
    curr_val = 0
    while curr_val <= 100:
       curr_val = int(input("enter the number you want to double it : "))
       curr_val = curr_val ** 2

       print(curr_val)  

    

    print(f"We stop {curr_val} because it is greater than 100")


if __name__ == "__main__":
    main()    