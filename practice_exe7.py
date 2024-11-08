import os

prod_name = []
prod_price = []
total = []

def order_details():
    
    grand_total_order = []
    
    while True:
        name_of_prod = input("Enter the name of the produt: ")
        prod_name.append(name_of_prod)
        quantity_product =int(input("Enter the quantity of the product: "))
        price_of_prod = int (input("Enter the price of product: "))
        prod_price.append (price_of_prod)
        total_order = price_of_prod * quantity_product
        total.append(total_order)

        grand_total_order = 0
        for value_in_total in total:
             grand_total_order += value_in_total
        
        print (grand_total_order)
        continue_to_order =input("Enter y for continue n for no: ")
                    
        if continue_to_order == "n":
                        break
        
    
    print (f"The product: {prod_name} cost {prod_price}: {grand_total_order}")
    return " "

def product_items ():

    print (f"The items you've ordered is {prod_name} and the price is {prod_price}")

    return " "

def customer_details (name_of_cus, customer_id):

    print (f"Your name is: {name_of_cus}")
    print (f"Your seniord id is: {customer_id}")


while True:

    os.system('cls')
    print ("A. Order")
    print ("B. price")
    print ("C. Items")
    print ("")

    choice = input("Enter your choice: ")

    if choice == "exit" or choice == "Exit":
        break
    match choice:
        case "A":
            os.system('cls')
            print (order_details())
            input("Press enter to continue")
        case "B":
            os.system('cls')
            print (" ")
        case "C":
            os.system('cls')
            print (product_items())
            print ("A. Name")
            print ("B. Seniord Id num")
            choice_nest = input("Enter your choice: ")
            match choice_nest:
                case "A":
                    os.system('cls')
                    name_of_cus = input("Enter your name: ")
                    seniord_id_num = input("Enter your seniord Id num: ")
                    print (customer_details(name_of_cus, seniord_id_num))
                case "B":
                    print (" ")
                case _:
                    print ("Invalid choice")
            input("Press enter to continue")
        case _:
            print ("Invalid choice")