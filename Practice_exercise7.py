import os

# TODO: @Marc Veslino     - Member 1: Function to gather order details.
# TODO: @Kirby Consultado - Member 2: Function to get the customer's details.
# TODO: @Piadozo Edriane  - Member 3: Function to calculate the total of the orders. Function to apply senior discount.
# TODO: @Gener Andaya     - Member 4: Function to display order summary.
# TODO: @Kevin Barcelos   - Member 5: Main function to coordinate the process

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
"""

# @Marc Veslino (Member1) - Function to get product details.
def get_order_details():
    os.system('cls')
    product_name = []
    price = []
    quantity = [] 
    total = []

    while True:
        name = input("Enter product name: ")
        price_1 = float(input("Enter price: "))
        number_of_items = int(input("Enter quantity: "))
        total_price = price_1 * number_of_items

        product_name.append(name)
        price.append(price_1)
        quantity.append(number_of_items)
        total.append(total_price)
        
        more_items = input("Do you want to add another item? (y/n): ")
        if more_items.lower() != 'y':
            os.system('cls')
            break
    return product_name, price, quantity, total

# @Kirby Consultado (Member2) - Function to get the customer's details.
def get_customer_info():
    customer_name = input("Enter customer name: ")
    senior_id = input("Enter senior ID (leave blank if not a senior citizen): ")
    return customer_name, senior_id

# @Piadozo Edriane (Member 3) - Function to apply senior discount.
def apply_discount(grand_total, senior_id): # Function to calculate the discount if applicable.
    if senior_id:
        return grand_total * 0.9  # 10% discount.
    return grand_total

# @Gener Andaya (Member 4) - Function to display the receipt.
def display_receipt(product_name, price, quantity, total, customer_name, senior_id, grand_total):
    os.system('cls')
    print("\nReceipt")
    print(f"Customer Name: {customer_name}")
    if senior_id:
        print(f"Senior ID: {senior_id}")
    print("\nItems:")
    
     # Iterate using range, accessing list items by index.
    for index in range(len(product_name)):
        print(f"{product_name[index]} - Price: {price[index]}, Quantity: {quantity[index]}, Total: {total[index]}")
    
    print(f"\nGrand Total: {grand_total:.2f}")

# @Kevin Barcelos (Member 5) - Main function to coordinate the process.
def main():
    # Step 1: Get order details from user.
    product_name, price, quantity, total = get_order_details()

    # Step 2: Get customer details
    customer_name, senior_id = get_customer_info()

    # Step 3: Calculate the grand total.
    grand_total = 0
    for value_in_total in total:
        grand_total = grand_total + value_in_total
    
    grand_total = apply_discount(grand_total, senior_id)
    print(grand_total)
    # Step 4: Display the final receipt.
    display_receipt(product_name, price, quantity, total, customer_name, senior_id, grand_total)

main()