import os

data_record = {
    "Name": [],
    "Age": [],
    "Role": [],
    "Major": [],
    "Average": [],
} 

def list_of_dict():
    for key in data_record:
        print(f"{key}: {data_record[key]}")

    return " "

def add_in_dict(range_of_dict):
    os.system('cls')
    for num in range (0, range_of_dict):
        name_of_stud = str(input("Enter the name you want to add: "))
        data_record["Name"].append(name_of_stud)

        age_of_stud = str(input("Enter the age of the student: "))
        data_record["Age"].append(age_of_stud)

        role_of_stud = str(input("Enter the role of the student in classroom: "))
        data_record["Role"].append(role_of_stud)
    
        major_of_stud = str(input("Enter the major course of the student: "))
        data_record["Major"].append(major_of_stud)

        gen_ave_of_stud = str(input("Enter the general average of the student: "))
        data_record["Average"].append(gen_ave_of_stud)
        print(" ")

    return " "

def update_in_dict():
    print("Follow the format (Name, Age, Role, Major, Average) ")
    new_info = input("Enter the list you want to update: ")
    if new_info in data_record:
        key_info = int(input(f"Enter the key index you want to update (0 - {len(data_record[new_info]) - 1}): "))
        new_value = input(f"Enter the new value for {new_info}: ")
        data_record[new_info][key_info] = new_value
    else:
        print("No data record in dictionary")
    
    return " "

def delete_in_dict():
    list_info = input("Enter the information you want to delete in this dictionary (Name, Age, Role, Major, Average): ")

    if list_info in data_record:
        remove_data = input("Enter the data you want to remove: ")
        print("The data is removed.")
        data_record[list_info].remove(remove_data)
        
        if data_record[list_info] in data_record:
            print("The data is removed. ")
        else:
            print("No data is available, please check the list.")
    else:
        print("No data is available, please check the list.")

    return " "

def search_of_dict(search_list):
    if search_list in data_record:
        print("The list is on dictionary.")
        print(f"Do you want to continue searching on {search_list} ? ")
        choice = input("Type 'Y' or 'y' to continue, 'X' or 'x' to stop: ")

        if choice == "Y" or choice == "y":
            key_finder = int(input(f"Enter the key index you want to find (0 - {len(data_record[search_list]) - 1}): "))
            data_record[search_list][key_finder]
            value = data_record[search_list][key_finder]
            print(f"The index that you have entered is {value}")
        else:
            exit       
    else:
        print("The list is not on dictionary.")

    return " "

while True:
    os.system('cls')
    print("Student Information Records")
    print("1. List All")
    print("2. Add")
    print("3. Update")
    print("4. Delete")
    print("5. Search")
    print("6. Exit")

    choice = input("Enter your choice in the menu (1-6): ")

    if choice == "6":
        break

    match choice:
        case "1":
            os.system('cls')
            print(list_of_dict())
            input("Press enter to continue")

        case "2":
            os.system('cls')
            range_of_dictionary = int(input("How many student(s) information you want to add: "))
            add_in_dict(range_of_dictionary)
            input("Press enter to continue")
            
        case "3":
            os.system('cls')
            print(update_in_dict())
            input("Press enter to continue")
        
        case "4":
            os.system('cls')
            print(delete_in_dict())
            input("Press enter to continue")

        case "5":
            os.system('cls')
            print("Follow the format (Name, Age, Role, Major, Average) ")
            search_input = input("Enter the list you want to search in the dictionary: ")
            print(search_of_dict(search_input))
            input("Press enter to continue")
        
        case _:
            os.system('cls')
            print("Invalid choice")