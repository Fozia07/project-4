#Fill out the function get_last_element(lst) which takes in a list lst as a parameter and prints the last element in the list. The list is guaranteed to be non-empty, but there are no guarantees on its length.

def Get_last_element(lst):
    """print the last element in the list"""
    print(lst[len(lst)- 1])


def Get_lst():
    """promt the user to enter one element in the list at a time and return resulting list"""

    elem:str=input("Enter an element on the list or presst enter to stop")

    while elem != "":
        elem:str=input("Enter an element onthe list or enter to stop ")
        
        lst=[]
        lst.append(elem)

        return lst


def main():
    lst=Get_lst()
    Get_last_element(lst)  

if __name__ =="__main__":
    main()