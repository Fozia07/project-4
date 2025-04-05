#Write a program which asks a user for their age and lets them know if they can or can't vote in the following three fictional countries.

#Around the world, different countries have different voting ages. In the fictional countries of Peturksbouipo, Stanlau, and Mayengua, the voting ages are very different:

#the voting age in Peturksbouipo is 16 (in real life, this is the voting age in, for example, Scotland, Ethiopia, and Austria)

#the voting age in Stanlau is 25 (in real life this is the voting age in the United Arab Emirates)

#the voting age in Mayengua is 48 (in real life, as far as we can tell, this isn't the voting age anywhere)

#Your code should prompt the for their age and print whether or not they can vote in Peturksbouipo, Stanlau, or Mayengua.

#Here's a sample run of the program (user input is in blue):

#How old are {you? 20 You can vote in Peturksbouipo where the voting age is 16. You cannot vote in Stanlau where the voting age is 25. You cannot vote in Mayengua where the voting age is 48.

Peturksbouipo:int=16
Stanlau:int=25
Mayengue:int=48

def main():
   
   #user input
   age=int(input("how old are you"))    

   if age >= Peturksbouipo:
      print(f"you can vote in Peturkshbouipo where the voting age is {Peturksbouipo}")   
   else :
      print(f"you can not vote in Perturksbouipo where the voting age is {Peturksbouipo} ")
   
   
   if age >=  Stanlau:
      print(f"you can vote in stanlau where the voting age is {Stanlau}")   
   else :
      print(f"you can not vote in stanlau where the voting age is {Stanlau} ")
             
   if age >=  Mayengue:
      print(f"you can vote in Mayengue where the voting age is{Mayengue}")   
   else :
      print(f"you can not vote in Mayengue where the voting age is {Mayengue} ")
             

if __name__ == "__main__" :
    main()           