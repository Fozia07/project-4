#Write a program that asks the user for the lengths of the two perpendicular sides of a right triangle and outputs the length of the third side (the hypotenuse) using the Pythagorean theorem!
#BC ** 2 = AB ** 2 + AC ** 2


import math

AB:float=float(input("Enter the length of AB: ")) #AB is one side lenght of triangle
AC:float=float(input("Enter the length of AC: ")) #AC is second the lenght of triangle

BC:float=math.sqrt((AB**2)+(AC**2))

print(f"lenght of AB = {AB}")
print(f"lenght of AC = {AC}")
print(f"The hypotenuse is {BC}")