import os

def get_oder_details():
    os.system("cls")
    name = []
    quantity = []
    price = []
    total = []

    while True: 
        product_name = input("Enter the product: ")
        quant = int(input("Enter the quantity: "))
        price_prod = float(input("Enter the price: "))
        total_price = price_prod * quant

        name.append(product_name)
        quantity.append(quant)
        price.append(price_prod)
        total.append(total_price)

        more_orders = input("Do you want to add more orders? (y/n): ")
        if more_orders != 'y':
            break

    return name, quantity, price, total

def get_costumer_details():
    costumer_name = input("Costumer name: ")
    senior_id = int(input("Senior id: "))
    if senior_id:
        return costumer_name, senior_id
    return costumer_name, senior_id

def senior_discount(senior_id, grand_total):
    if senior_id:
        grand_total = grand_total * 0.9
        return grand_total 
    return grand_total

def display_receipt(name, quantity, price, total,costumer_name, senior_id, grand_total):
    print("\nReceipt\n")
    print(f"Name: {costumer_name}")
    if senior_id:
        print(f"Senior ID: {senior_id}")
    
    print("\nItems\n")
    for i in range(len(name)):
        print(f"Name: {name[i]} - Price: {price[i]} - Quantity: {quantity[i]} - Total: {total[i]}")

    print(f"GRAND TOTAL: {grand_total}")

#main
name, quantity, price, total = get_oder_details()
grand_total = 0.00
for i in total:
    grand_total = grand_total + i
print(grand_total)
costumer_name, senior_id = get_costumer_details()
grand_total = senior_discount(senior_id, grand_total)

display_receipt(name, quantity, price, total,costumer_name, senior_id, grand_total)