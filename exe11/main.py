from ourpackage import consultado
import os


while True:
    os.system('cls')
    print("MODULES")
    print("1. Consultado")
    print("2. Vesliño")
    print("3. Piadozo")
    print("4. Barcelos")
    print("5. Andaya")
    print("0. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 0:
        break

    match choice: 
        case 1:
            os.system('cls')
            print("NUMBER TO WORD and WORD TO NUMBER CONVERTER")
            print("1. Number to Word")
            print("2. Word to Number")
            choice = input("Enter your choice: ")

            match choice:
                case '1':
                    number = int(input("Enter a number: "))
                    print(consultado.num_to_word_func(number))
                case '2':
                    word = str(input("Enter a number word: "))
                    print(consultado.word_to_num_func(word))
                case _:
                    print("Invalid input, try again.")
            input("Press any key to continue.")
        case 2:
            os.system('cls')
            pass
        case 3:
            os.system('cls')
            pass
        case 4:
            os.system('cls')
            pass
        case 5:
            os.system('cls')
            pass
        case _:
            print("Invalid choice.")