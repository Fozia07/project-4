#In this program we show an example of using dictionaries to keep track of information in a phonebook.

def  read_phone_number():
    phonebook={}

    #user input
    while True:
        names=input("Enter the name: ")
        if names == "":
            break

        numbers=input("Enter the number: ")
        phonebook[names]=numbers

    return   phonebook  

def print_phonebook(phonebook):

    for name in phonebook:
        print(str(name) + " -> " + str(phonebook[name]))

def lookup_number(phonebook):
    while True:
        name=input("Enter the name: ")
        if name == "":
            break
        if name not in phonebook:
            print(f"{name} is not in {phonebook}")
        else:
            print(phonebook[name])    


def main():
    phonebook= read_phone_number()
    print_phonebook(phonebook)    
    lookup_number(phonebook)      


if __name__ == "__main__":
    main()      