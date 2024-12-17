import os

def marc_information():
    os.system("cls")
    while True:
        print(f"\033[1;35m{'=' * 50}")
        print("             Hello, I'm Marc D. Vesliño               ")
        print("1. Basic Information")
        print("2. Goals")
        print("3. Comment Teammate 1")
        print("4. Comment Teammate 2")
        print("5. Comment Teammate 3")
        print("6. Comment Teammate 4")
        print("0. Exit")
        print(f"\033[1;35m{'=' * 50}")

        menu_choice = int(input("Enter your choice: "))
        
        
        if menu_choice == 0:
            break  

        match menu_choice:
            case 1:
                os.system("cls")
                print("                                                         Basic Information                                   ")
                print("I’m Marc Veslino, a 19-year-old student studying Information Tech2321nology."
                      " I’ve always had a passion for creativity, especially when it comes to web design."
                      " I’m skilled in using Figma and Photoshop, and I enjoy designing and developing websites using HTML, CSS, and JavaScript."
                      " Alongside my studies, I enjoy watching anime, playing basketball, and, of course, watching movies—activities that help me unwind and stay inspired.")
                input("Press enter to continue")
                os.system("cls")


            case 2:
                os.system("cls")
                print("                                                 Goals                                               ")
                print("1. Achieve stability across all aspects of life, including financial security and personal growth.")
                print("2. Maintain a healthy body and mind to ensure long-term well-being.")
                print("3. Provide for and support my family, ensuring their happiness and security.")
                print("4. Live with purpose and stay aligned with my true calling.")
                print("5. Give back to my community through acts of kindness and service.")
                print("6. Cultivate a strong and loving family bond.")
                print("7. Build a joyful and supportive family environment, where love and happiness thrive.")
                input("Press enter to continue")
                os.system("cls")


            case 3:
                os.system("cls")
                print("Comment Teammate 1")
                input("Press enter to continue")
                os.system("cls")

            case 4:
                os.system("cls")
                print("Comment Teammate 2")
                input("Press enter to continue")
                os.system("cls")


            case 5:
                os.system("cls")
                print("Comment Teammate 3")
                input("Press enter to continue")
                os.system("cls")


            case 6:
                os.system("cls")
                print("Comment Teammate 4")
                input("Press enter to continue")
                os.system("cls")

            case _:
                print("Invalid input.")
                input("\nPress enter to continue.")