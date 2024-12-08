import os
from colorama import Fore 

def kevin():
    while True:
        print(Fore.LIGHTYELLOW_EX + "\nHello everyone! I am Kevin Joseph V. Barcelos")
        print(Fore.LIGHTGREEN_EX + "1. Basic Information")
        print("2. Goals")
        print("3. To Do List (Mini task :>)")
        print("0. To go back")
        menu_choice = int(input("Enter your choice: "))
        print(Fore.RESET)
# Ito pang reset  Pwede kung irereeset mo din. Parang sa c++ lang
        match(menu_choice):
            case 1:
                os.system('cls')
                print(Fore.BLUE + "\nName: Kevin Joseph V. Barcelos")
                print("Age: 19")
                print("Sex: Male")
                print("Birthday: February 18, 2005")
                print("Civil Status: Single")
                input("\nPress Enter to continue.")
            case 2:
                os.system('cls')
                print(Fore.LIGHTYELLOW_EX + "\n Goals")
                print("\nLong Term Goals: ")
                print("1. Finish College.")
                print("2. Get a job.'")
                print("3. Invest in assests.")
                print("4. Get a house.")
                print("5. Fall in love.")

                print("\nShort Term Goals: ")
                print("1. Study Python.")
                print("2. Pass this semester with good grades.")
                print("3. Learn Data Analyst Skills.")
                print("4. Get a part time job.")
                print("5. Have fun while coding :>")
                input("\nPress Enter to continue. ")
            case 3:
                to_do_list()
            case 0:
                break
            case _: 
                print("Invalid Choice. Try Again.")
                input("\nPress Enter to continue.")
            
def add_task(tasks):
    task = input("Enter a new task: ")
    tasks.append({"task": task, "done": False})
    print(f"Task '{task}' added!")

def view_tasks(tasks):
    if not tasks:
        print("No tasks in the list.")
    else:
        print("\nYour Tasks:")
        for idx, t in enumerate(tasks, start=1):
            status = "Done" if t["done"] else "Not Done"
            print(f"{idx}. {t['task']} - {status}")

def mark_task_done(tasks):
    if not tasks:
        print("No tasks to mark as done.")
        return
    
    view_tasks(tasks)
    task_num = int(input("Enter the task number to mark as done: "))
    if 1 <= task_num <= len(tasks):
        tasks[task_num - 1]["done"] = True
        print(f"Task '{tasks[task_num - 1]['task']}' marked as done!")
    else:
        print("Invalid task number.")

def to_do_list():
    tasks = []
    while True:
        os.system('cls')
        print("\nTo-Do List Menu:")
        print("1. Add a Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Exit")
        choice = int(input("Choose an option: "))

        match (choice):
            case 1:
                add_task(tasks)
                input("\nPress Enter to continue. ")
            case 2:
                view_tasks(tasks)
                input("\nPress Enter to continue. ")
            case 3:
                mark_task_done(tasks)
                input("\nPress Enter to continue. ")

            case 4:
                print("Goodbye!")
                break
            case _:
                print("Invalid choice. Please try again.")