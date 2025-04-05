#This program counts the number of times each number appears in a list. It uses a dictionary to keep track of the information.

#This program counts the number of times each number appears in a list. It uses a dictionary to keep track of the information.

#get user number

def Get_User_Input():
    User_numbers=[]
    while True :
        User_Input = input("Enter the number: ")
        if User_Input == "":
            break
        #add user input in the list 
        num =int( User_Input)
        User_numbers.append(num)

    return User_numbers

def count_number(num_lst):
    num_dict={}
    for num in num_lst:
        if num not in num_dict:
          num_dict[num] = 1
        else :
          num_dict[num] += 1

    return num_dict

def Print_Count_Number(num_dict):
      for num in num_dict:
          
       print(f"{num} appear in {num_dict[num]} times")


def main():
    """
    Ask the user to input numbers and store them in a list. Once they enter a blank line,
    print out the number of times each number appeared in the list.
    """
    user_numbers = Get_User_Input()
    num_dict = count_number (user_numbers)
    Print_Count_Number(num_dict)


if __name__ =="__main__":
    main()   