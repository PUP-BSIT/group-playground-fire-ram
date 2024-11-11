import os

data_record = {
    "name": ["Gerald"],
    "age": ["19"],
    "role":["President"],
    "major":["Information Technology"],
    "average":["1.75"],
}

def list_of_dict():
    for key in data_record:
        print (f" {key} : {data_record[key]}")
    return " "

def add_in_dict (range_of_dict):
    os.system('cls')
    for num in range (0, range_of_dict):
        name_of_stud = str(input("Enter the number of the name you want to add: "))
        data_record["name"].append(name_of_stud)

        age_of_stud = str(input("Enter the age of the student: "))
        data_record["age"].append(age_of_stud)

        role_of_stud = str(input("Enter the role of the student in classroom: "))
        data_record["role"].append(role_of_stud)
    
        major_of_stud = str(input("Enter the major of the student: "))
        data_record["major"].append (major_of_stud)

        gen_ave_of_stud = str(input("Enter the general ave of the student: "))
        data_record["average"].append (gen_ave_of_stud)
        return " "

def update_in_dict ():
    new_info = input("Enter the list (name, age, role, major, average) you want to update: ")
    if new_info in data_record:
        new_value = input (f"Enter the new value for {new_info}: ")
        key_info = int(input("Enter the key index you want to update: "))
        data_record[new_info][key_info] = new_value
    else:
        print ("No data record in dictionary")
    return " "

def delete_in_dict ():
    list_info = input("Enter the list you want to make changes (name, age, role, major, average): ")

    if list_info in data_record:
        remove_data = input("Enter the data you want to remove: ")
        print ("The data is remove")
        data_record[list_info].remove (remove_data)
        
    else:
        print ("No data is available please check List all")

    return " "

def search_of_dict(search_list):
    if search_list in data_record:
        print ("List is on our record")
        print (f"Do you want to continue searching on {search_list}: ")
        choice = input("Print Y or y to continue X or x to stop: ")

        if choice == "Y" or choice == "y":
            key_finder = int (input("Enter the key index you want to find starting from 0: "))
            data_record[search_list][key_finder]
            value = data_record[search_list][key_finder]
            print (f"The index that you have enter is: {value}")
        else:
            exit       
    else:
        print ("List is not on record")

        return " "

while True:
    os.system ('cls')
    print ("Student Information Records")
    print ("1. List all")
    print ("2. Add")
    print ("3. Update")
    print ("4. Delete")
    print ("5. Search")
    print ("6. Exit")

    choice = input("Enter your choice in the menu: ")

    if choice == "6":
        break

    match choice:
        case "1":
            os.system ('cls')
            print (list_of_dict())
            input("Press enter to continue")

        case "2":
            os.system('cls')
            range_of_dictionary = int(input("How many student information you want to add: "))
            add_in_dict (range_of_dictionary)
            input("Press enter to continue")
            
        case "3":
            os.system ('cls')
            print (update_in_dict())
            input("Press enter to conitue")
        case "4":
            os.system ('cls')
            print (delete_in_dict())
            input("Press enter to continue")

        case "5":
            os.system('cls')
            search_input = input("Enter the list you want to search Enter the list (name, age, role, major, average): ")
            print (search_of_dict(search_input))
            input("Press enter to continue")
        case _:
            os.system ('cls')
            print ("Invalid choice")