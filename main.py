import os

"""

Create a file called main.py. The program will ask the user for the following order details:
a. Product Name
b. Price
c. Quantity

After the last detail, it will ask if the user wants to add another item answerable by y for
yes or n for no. If the user enters y, it will ask order details. Otherwise, it will proceed
to the next step. After the orders are completed, the program will ask for the customer name
and senior ID no.(blank if not senior citizen). If the customer is a senior citizen, a 10%
discount will be deducted in the grand total. After that, the program will display the the
following details:

d. Items(product name, price, quantity, total)
e. Customer Name
f. Senior ID No.
g. Grand Total

# Member 1: Function to gather order details.

# Member 2: Function to get customer details.

# Member 4: Function to calculate the total of the orders. Function to apply senior discount.
# Member 5: Function to display order summary.
# Member 3: Main function to coordinate the process

Member 1: @Marc Veslino
Member 2: @Kirby Consultado
Member 3: @Piadozo Edriane
Member 4: @Kevin Barcelos
Member 5: @Jay-ar Andaya

"""
list_of_product = ["Nescafe", "Rebisco", "Lucky Me"]




list_of_product_nescafe =  ["Nescafe Creamy white", "Nescafe Original", "Nescafe Classic"]
price_of_items_nescafe = list_of_product_nescafe.copy()
price_of_items_nescafe[0] = 15
price_of_items_nescafe[1] = 15
price_of_items_nescafe[2] = 15



list_of_items_rebisco = ["Rebisco Honey butter", "Rebisco Butter", "Bravo"]
price_of_items_rebisco = list_of_items_rebisco.copy()
price_of_items_rebisco [0] = 7
price_of_items_rebisco [1] = 8
price_of_items_rebisco [2] = 9



list_of_items_lucky_me = ["Chicken Noodles", "Beef Noodles", "Pork Noodles"]
price_of_items_luckyme = list_of_items_lucky_me.copy()
price_of_items_luckyme [0] = 10
price_of_items_luckyme [1] = 12
price_of_items_luckyme [2] = 12

list_of_order = []


def list_of_order_nescafe(prod_wants, num_of_items):

    if prod_wants == "1":
        print(f"The Items in nescafe: {list_of_product_nescafe}")
        print (f"The price of the item in nescafe ₱ {price_of_items_nescafe}")

    for num in range (0, num_of_items):
        item_ordered = int (input(f"Enter the items you want to order {num + 1}: "))
        list_of_order.append (item_ordered)

    for num in list_of_order:
        if 0 <= num or 0 < len(list_of_product_nescafe):
            value = list_of_product_nescafe[num]
            print (f"The product in the index number: {num} is: {value}")
    

os.system ('cls')

print ("a. Product name")
print ("b. Price")
print ("c. Quantity")


choice = input("Enter your choice: ")

match choice:
    case "a":
        os.system('cls')
        print ("The available product in our store")
        print (list_of_product)
    case "b":
        os.system('cls')
        print ("Price of the product in the store")
        print ("a. For the Nescafe ")
        print ("b. For the Rebisco")
        print ("c. For the Luckyme")

        choice_b = input("Enter your choice: ")

        match choice_b:
            case "a":

                os.system('cls')
                print(f"The Items in nescafe: {list_of_product_nescafe}")
                print (f"The price of the item in nescafe ₱ {price_of_items_nescafe}")
            case "b":

                os.system ('cls')
                print (f"The items in rebisco: {list_of_items_rebisco}")
                print (f"The price of items in rebisco: ₱ {price_of_items_rebisco}")
            case "c":
                
                os.system ('cls')
                print (f"The items in Luckyme: {list_of_items_lucky_me}")
                print (f"The price of items in lucky me: ₱ {price_of_items_luckyme} ")
            case _:
                print ("Invalid choice")


    case "c":
        os.system ('cls')
        print ("a. For nescafe items")
        print ("b. For rebisco items")
        print ("c. For luckyme items")
        choice_c = input("Enter your chosen product: ")

        match choice_c:
            case "a":
                print ("1. For nescafe items")
                print ("2. For rebisco items")
                print ("3. For luckyme items")
                choice_of_prod = input("Enter the choice of product: ")
                quantity_of_items = int(input("Enter the quantity of your item: "))
                list_of_order_nescafe(choice_of_prod, quantity_of_items)
            case "b":
                print ()
    case _:
        print ("Invalid choice")


def senior_discount ():
    pass