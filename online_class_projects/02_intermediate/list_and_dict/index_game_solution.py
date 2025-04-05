#Create a Python program that helps you practice accessing and manipulating elements in a list. This exercise will help you get comfortable with indexing, slicing, and modifying list elements.

def access_element(lst,index):
       try:
          return lst[index] 
       except IndexError:
          return "Index out of range."
       

def modify_element(lst,index,new_element):
    try:
        lst[index]=new_element
        return lst
    except IndexError:
        return"index out of range"
    
def slice_list(lst,start,end):
    try:
        return lst[start,end]
    except IndexError:
        return "index out of range"
    
def index_game():
    lst=["apple","banana","orange","grape","pineapple"]
    print (f"current list :{lst}")    
    print("Choose the option :  access , modify , slice")
    choice=input("enter operation: ")

    if choice == "access":
        index=input("Enter which index you accessing : ")
        print(access_element(lst,index))
    elif choice == "modify":
        index=input("Enter the element to modifing : ")
        element=input("what is the element : ")
        print(modify_element(lst,index,element)) 

    elif choice == "slice":
        start=input("enter the starting index: ")
        end=input("enter the ending index: ")
        print(slice_list(lst[start,end]))

    else:
        print("Invalid operation")    


index_game()