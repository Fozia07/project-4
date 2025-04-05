#There's a small fruit shop nearby your house that you like to buy from. Since you buy several fruit at a time, you want to keep track of how much the fruit will cost before you go. Luckily you wrote down what fruits were available and how much one of each fruit costs.

#Write a program that loops through a dictionary of fruits, prompting the user to see how many of each fruit they want to buy, and then prints out the total combined cost of all of the fruits.

def main():
  fruits={"apple":1.5,"durain":50,"jackfruit":80,"kiwi":1,"rambuton":1.5,"mango":5}
 
  total_cost =0
  for fruits_name in fruits:
    price = fruits[fruits_name]
    buy_amount=int(input("How many ("+ fruits_name +") you want? "))

    total_cost += (buy_amount*price)

  print(f"The total amount is {total_cost}")


if __name__ =="__main__":
    main()  