#Write a function that takes a list of numbers and returns the sum of those numbers.

def Add_Many_number(numbers):
      num=0
      for number in numbers:
        
        num += number

      return num

def main():
     numbers:list[int] =[4,2,5,6,1]
     sum_of_number = Add_Many_number (numbers)
     print(sum_of_number)
    
    
if __name__ =='__main__':
      main()