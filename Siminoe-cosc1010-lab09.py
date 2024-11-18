# Forrest Siminoe
# UWYO COSC 1010
# 11/17/24
# Lab 09
# Lab Section: 13
# Classes
# For this assignment, you will be creating two classes:
# One for Pizza
# One for a Pizzeria


# You will be creating a Pizza class. It should have the following attributes:
# - Size
# - Sauce
# - Toppings, which should be a list
# You need to create one method that corresponds with each of the above attributes
# which returns the corresponding attribute, just the value.
# For the size and toppings attributes, you will need to have a method to set them.
# - For Size, ensure it is an int > 10 (inches)
#   - If it is not, default to a 10" pizza (you can store ten). These checks should occur in init as well.
# - For toppings, you will need to add the toppings.
#   - This method needs to be able to handle multiple values.
#   - Append all elements to the list.
# Create a method that returns the amount of toppings.
# In your __init__() method, you should take in size and sauce as parameters.
# - Sauce should have a default value of red.
# - Size will not have a default value; use the parameter with the same safety checks defined above (you can use the set method).
# Within __init__(), you will need to:
# - Assign the parameter for size to a size attribute.
# - Assign the parameter for sauce to the attribute.
# - Create the toppings attribute, starting off as a list only holding cheese.
class Pizza:
    def __init__(self, size, sauce="red"):
        self.sauce = sauce
        self.toppings = ["cheese"]
        self.setSize(size)
    def setSize(self, size):
        if size < 10:
            self.size = 10 
        else:
            self.size = size
    def getSize(self):
        return self.size
    def setSauce(self, sauce):
        self.sauce = sauce
    def getSauce(self):
        return self.sauce
    def addToppings(self, toppings):
        for topping in toppings:
            self.toppings.append(topping)
    def getToppings(self):
        return self.toppings
    def getAmountOfToppings(self):
        return len(self.toppings)


class Pizzeria:
    price_per_topping = 0.30
    price_per_inch = 0.60
    def __init__(self):
        self.orders = 0
        self.pizzas = []
    def placeOrder(self):
        self.orders += 1
        size = int(input("Please enter the size of pizza, as a whole number. The smallest size is 10\n"))
        sauce = input("What kind of sauce would you like?\nLeave blank for red sauce\n")
        if not sauce:
            sauce = "red"
        toppings = []
        while True:
            topping = input("Please enter the toppings you would like, leave blank when done\n")
            if topping == "":
                break
            toppings.append(topping)
        pizza = Pizza(size, sauce)
        pizza.addToppings(toppings)
        self.pizzas.append(pizza)
        self.getReceipt(pizza)
    def getPrice(self, pizza):
        size_price = pizza.getSize() * Pizzeria.price_per_inch
        topping_price = pizza.getAmountOfToppings() * Pizzeria.price_per_topping
        return size_price + topping_price
    def getReceipt(self, pizza):
        print(f"\nYou ordered a {pizza.getSize()}\" pizza with {pizza.getSauce()} sauce and the following toppings:")
        for topping in pizza.getToppings():
            print(f"                                                                  {topping}")
        size_price = pizza.getSize() * Pizzeria.price_per_inch
        topping_price = pizza.getAmountOfToppings() * Pizzeria.price_per_topping
        total_price = size_price + topping_price
        print(f"You ordered a {pizza.getSize()}\" pizza for {size_price}")
        print(f"You had {pizza.getAmountOfToppings()} topping(s) for ${topping_price}")
        print(f"Your total price is ${total_price}\n")

    def getNumberOfOrders(self):
        return self.orders
def main():
    pizzeria = Pizzeria()
    while True:
        user_input = input("Would you like to place an order? Type 'exit' to exit\n")
        if user_input.lower() == 'exit':
            break
        pizzeria.placeOrder()
    print(f"\nTotal number of orders placed: {pizzeria.getNumberOfOrders()}")
main()

# - Declare your pizzeria object.
# - Enter a while loop to ask if the user wants to order a pizza.
# - Exit on the word `exit`.
# - Call the placeOrder() method with your class instance.
# - After the order is placed, call the getReceipt() method.
# - Repeat the loop as needed.
# - AFTER the loop, print how many orders were placed.


# Example output:
"""
Would you like to place an order? exit to exit
yes
Please enter the size of pizza, as a whole number. The smallest size is 10
20
What kind of sauce would you like?
Leave blank for red sauce
garlic
Please enter the toppings you would like, leave blank when done
pepperoni
bacon

You ordered a 20" pizza with garlic sauce and the following toppings:
                                                                  cheese
                                                                  pepperoni
                                                                  bacon
You ordered a 20" pizza for 12.0
You had 3 topping(s) for $0.8999999999999999
Your total price is $12.9

Would you like to place an order? exit to exit
"""