
#create a mad lib library 
print("***** MAD LIB LIBRARY*****")
print("Make a fun with this mad library put some noun verb and adjective ")

Adjective=str(input("enter any adjective : "))
Verb=str(input("Enter any verb : "))
Noun=str(input("Enter any noun: "))


def main():
   mad_lib= (f"A {Adjective} {Noun} {Verb} over the fence. ")
   print (mad_lib)


if __name__ =="__main__":
   main()
