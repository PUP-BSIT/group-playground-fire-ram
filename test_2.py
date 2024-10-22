import os 



# TODO: Member 1 - Function to get product details
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
                        #KEY : VALUE
        product_name.append(name)
        price.append(price_1)
        quantity.append(number_of_items)
        total.append(total_price)
        
        # TODO: Member 2 - Ask user if they want to add another item
        more_items = input("Do you want to add another item? (y/n): ")
        if more_items.lower() != 'y':
            os.system('cls')
            break
    return product_name, price, quantity, total

# TODO: Member 2 and 3 - Function to get the customer's information and check for senior citizen discount if applicable.
def get_customer_info():
    customer_name = input("Enter customer name: ")
    senior_id = input("Enter senior ID (leave blank if not a senior citizen): ")
    return customer_name, senior_id

def apply_discount(grand_total, senior_id): # Function to calculate the discount if applicable.
    if senior_id:
        return grand_total * 0.9  # 10% discount
    return grand_total

# TODO: Member 4 - Function to display the receipt
def display_receipt(product_name, price, quantity, total, customer_name, senior_id, grand_total):
    os.system('cls')
    print("\nReceipt")
    print(f"Customer Name: {customer_name}")
    if senior_id:
        print(f"Senior ID: {senior_id}")
    print("\nItems:")
     # Iterate using range, accessing list items by index
    for index in range(len(product_name)):
        print(f"{product_name[index]} - Price: {price[index]}, Quantity: {quantity[index]}, Total: {total[index]}")
    
    print(f"\nGrand Total: {grand_total:.2f}")

# TODO: Member 5 - Main function to coordinate the process
def main():
    # Step 1: Get order details from user
    product_name, price, quantity, total = get_order_details()

    # Step 2: Get customer details
    customer_name, senior_id = get_customer_info()

    # Step 3: Calculate the grand total
    grand_total = 0
    for value_in_total in total:
        grand_total = grand_total + value_in_total
    
    grand_total = apply_discount(grand_total, senior_id)
    print(grand_total)
    # Step 4: Display the final receipt
    display_receipt(product_name, price, quantity, total, customer_name, senior_id, grand_total)

main()