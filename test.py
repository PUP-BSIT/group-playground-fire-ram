import os 
# TODO: Member 1 - Function to get product details
def get_order_details():
    os.system('cls')
    orders = []
    while True:
        product_name = input("Enter product name: ")
        price = float(input("Enter price: "))
        quantity = int(input("Enter quantity: "))
        total = price * quantity
                        #KEY : VALUE
        orders.append({"product_name": product_name,
                       "price": price, 
                       "quantity": quantity,
                       "total": total}
                    )
        
        # TODO: Member 2 - Ask user if they want to add another item
        more_items = input("Do you want to add another item? (y/n): ")
        if more_items.lower() != 'y':
            os.system('cls')
            break
    return orders

# TODO: Member 3 - Function to get customer information and check for senior citizen
def get_customer_info():
    customer_name = input("Enter customer name: ")
    senior_id = input("Enter senior ID (leave blank if not a senior citizen): ")
    return customer_name, senior_id

# TODO: Member 3 - Function to calculate discount if applicable
def apply_discount(grand_total, senior_id):
    if senior_id:
        return grand_total * 0.9  # 10% discount
    return grand_total

# TODO: Member 4 - Function to display the receipt
def display_receipt(orders, customer_name, senior_id, grand_total):
    os.system('cls')
    print("\nReceipt")
    print(f"Customer Name: {customer_name}")
    if senior_id:
        print(f"Senior ID: {senior_id}")
    print("\nItems:")
    for order in orders:
        print(f"{order['product_name']} - Price: {order['price']}, Quantity: {order['quantity']}, Total: {order['total']}")
    print(f"\nGrand Total: {grand_total:.2f}")

# TODO: Member 5 - Main function to coordinate the process
def main():
    # Step 1: Get order details from user
    orders = get_order_details()

    # Step 2: Get customer details
    customer_name, senior_id = get_customer_info()

    # Step 3: Calculate the grand total
    grand_total = sum(order['total'] for order in orders)
    grand_total = apply_discount(grand_total, senior_id)

    # Step 4: Display the final receipt
    display_receipt(orders, customer_name, senior_id, grand_total)

main()