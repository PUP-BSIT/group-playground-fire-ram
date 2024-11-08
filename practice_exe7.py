import os

prod_name = []
prod_price = []


def product_name():
    quantity_product = 1

    for num in range (0, quantity_product):

        name_of_prod = input("Enter the name of the produt: ")
        prod_name.append(name_of_prod)

    continue_to_order =input("Enter y for continue n for no: ")


    if continue_to_order == "y":
        quantity_product = 0
        quantity_product = quantity_product + 1  
        name_of_prod = str(input("Enter the name of the produt: "))
        prod_name.append(name_of_prod)
        
    elif continue_to_order == "n":
            print ("Proceed to the next step")


    return " "
def product_price ():

    for num in prod_name:

        price_of_prod = int(input("Enter the price of the product: "))
        prod_price.append (price_of_prod)

    return " "

def product_items ():

    print (f"The items you've ordered is {prod_name} and the price is {prod_price}")

    return " "

def customer_details (name_of_cus, customer_id):

    print (f"Your name is: {name_of_cus}")
    print (f"Your seniord id is: {customer_id}")


while True:

    os.system('cls')
    print ("A. product")
    print ("B. price")
    print ("C. Items")
    print ("")

    choice = input("Enter your choice: ")

    if choice == "exit" or choice == "Exit":
        break
    match choice:
        case "A":
            os.system('cls')
            print (product_name())
            input("Press enter to continue")
        case "B":
            os.system('cls')
            print (product_price())
            input("Press enter to continue")
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