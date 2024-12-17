import os
import random

def edriane():
    while True:
        os.system('cls')
        print ("Your Teammate :)")
        print ("1. Who am I ?")
        print ("2. What's your thought to me as a teammate :>")
        print ("3. Rate my function")
        print ("0. Exit")
        user_choice = int(input("Enter your choice of number: "))

        if user_choice == 0:
            print ("Thanks B)")
            break

        match user_choice:
            case 1:
                while True:
                    os.system("cls")
                    print ("I am Edriane")
                    print ("a. Birthday          b"". Hobby")
                    print ("c. Favorite movie    d"". Favorite Series")
                    print ("e. Word of Wisdom    f"". Dream")
                    print ("g. Exit")
                    know_me = input("Enter your choice: ")
                    
                    if know_me == "g":
                         print ("Thank you B)")
                         break
                        
                    match know_me:
                        case "a":
                                os.system('cls')
                                print ("My birthday is January 1 2005")
                                present = str (input("Do you have a gift for me Y/N ?: "))

                                if present == 'Y':
                                    print ("Ahhh thank you :*")
                                    input()
                                elif present == "N":
                                    print ("NOOO")
                                    input()
                                    
                        case "b":
                                os.system('cls')
                                print ("My hobby is playing online games")
                                input("Press enter to continue")
                        case "c":
                                os.system('cls')
                                print ("My favorite movie is Whiplash")
                                input("Press enter to continue")
                        case "d":
                                os.system('cls')
                                print ("My favorite series is Breaking bad and Better Call Saul")
                                input("Press enter to continue")
                        case "e":
                                os.system('cls')
                                print ("Let it happen")
                                input("Press enter to continue")
                        case "f":
                            os.system('cls')
                            print ("Become a Game Developer")
                            print ("Develop a game that will remember me")
                            input("Press enter to continue")
                        case _:
                            os.system('cls')
                            print ("Invalid choice")
            case 2:
                os.system('cls')
                why_o_why = ["Am I not good teammate ?", "Enter again >:(", "Why not press Y ?","Why press N 8-< ?"]
                while True:
                    choice_team = str(input("Am I a good team mate Y/N ?: "))
                    random_comment = random.randint(0,3)

                    if choice_team == "N":
                        print (why_o_why[random_comment])
                        input()
                    elif choice_team == "Y":
                        print ("Thank you B)")
                        input()
                        break
            case 3:
                  os.system('cls')
                  rate_my_module = int(input("Enter your rate 1-10: "))
                  if rate_my_module == 10:
                       print ("Thanks B)")
                       input()
                  elif rate_my_module >= 5 and rate_my_module <= 9:
                       print ("Why :(")
                       input()
                  elif rate_my_module >= 0 and rate_my_module <= 4:
                       print ("k")
                       input ()
            case _:
                print ("Invalid choice")
    return " "

edriane()