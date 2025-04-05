#Fill out the function get_first_element(lst) which takes in a list lst as a parameter and prints the first element in the list. The list is guaranteed to be non-empty. We've written some code for you which prompts the user to input the list one element at a time.


def Get_First_Element(lst):
    """print the first element from the list"""

    print(lst[0])

def Get_lst():
    """promt the user to enter one element on the list at a time and return the resulting list"""
    
    lst=[]
    elem:str=input("Enter an element in the list or press enter to stop")
    
    while elem != "":
        lst.append(elem)
        elem=input("Enter an element or press enter to stop")

        return lst

def main():
    lst=Get_lst()
    Get_First_Element(lst)

if __name__ == "__main__":
    main()    