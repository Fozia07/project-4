#Write a program which continuously asks the user to enter values which are added one by one into a list. When the user presses enter without typing anything, print the list.

def main():
    lst=[]
    val:str=input("Enter the element : ")
    while val: #it stop when user give empty value
        lst.append(val)
        val:str=input("Enter the element : ")
       
    print("Here's the list:", lst)

if __name__  == "__main__":
    main()   