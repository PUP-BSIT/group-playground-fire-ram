import os
#INSTRUCTIONS
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
# Member 3: Function to calculate the total of the orders. Function to apply senior discount.
# Member 4: Function to display order summary.
# Member 5: Main function to coordinate the process

Member 1: @Marc Veslino
Member 2: @Kirby Consultado
Member 3: @Piadozo Edriane
Member 4: @Jay-ar Andaya
Member 5: @Kevin Barcelos

"""
#Marc
def add_order():
    orders = []
    while True:
        product_name = input("Product name: ")
        price = float(input("Price: "))
        quantity = int(input("Quantity: "))
        orders.append({
            "product_name": product_name,
            "price": price,
            "quantity": quantity,
            "total": price * quantity
        })
        if input("Add another item? (y/n): ").lower() != 'y':
            print(orders[0])
            break
    return orders

#Kirby & Edriane
def costumer_detail():
    pass
#Gener
def order_summary():
    pass
#Kevin
def main():
    pass

add_order()


