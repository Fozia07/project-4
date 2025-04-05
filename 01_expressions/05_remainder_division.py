#Ask the user for two numbers, one at a time, and then print the result of dividing the first number by the second and also the remainder of the division.


First_number:int=int(input("Enter integer to be divided :  "))
Second_number:int=int(input("Enter an integer divided by : "))

divide:float = First_number/Second_number
reminder:float= First_number % Second_number

print(f"The result of division is {divide} and the reminder is {reminder}")