import os 

def gener():

    while True:
        os.system('cls')
        print("================= Andaya's Menu ==================")
        print("=                                                =")
        print("= Hello Everyone! My name is Gener A. Andaya Jr. =")
        print("=                                                =")
        print("= 1. My basic info.                              =")
        print("= 2. My personal goals.                          =")
        print("= 3. Comment from teammate 1.                    =")
        print("= 4. Comment from teammate 2.                    =")
        print("= 5. Comment from teammate 3.                    =")
        print("= 6. Comment from teammate 4.                    =")
        print("= 7. Exit.                                       =")
        print("==================================================")
        
        choice = input("Enter your choice (1-7): ")
       
        match choice:
            case "1":
                print("\n")
                print("================== My Basic Info ===================")
                print("=                                                  =")
                print("= Name: Gener A. Andaya Jr.                        =")
                print("= Age: 20 years old.                               =") 
                print("= Sex: Male.                                       =")
                print("= Birthday: September 17, 2004.                    =")
                print("= Civil Status: Single.                            =")
                print("= Religion: Baptist.                               =")
                print("= Course: Diploma in Information Technology (DIT). =")
                print("=                                                  =")
                print("====================================================")
                input("\nPlease press enter key to continue!")
            case "2":
                print("\n")
                print("=========== My Personal Goals ============")
                print("=                                        =")
                print("= - Finish my studies in College.        =")
                print("= - Secure a stable job in the IT field. =")
                print("= - Own a house and cars.                =")
                print("= - Establish my own business.           =")
                print("=                                        =")
                print("==========================================")
                input("\nPlease press enter key to continue!")
            case "3":   
                print("\nTeammate 1 Barcelos: ")
                input("\nPlease press enter key to continue!")
            case "4":
                print("\nTeammate 2 Veslino: ")
                input("\nPlease press enter key to continue!")
            case "5":
                print("\nTeammate 3 Consultado: ")
                input("\nPlease press enter key to continue!")
            case "6":
                print("\nTeammate 4 Piadozo: ")
                input("\nPlease press enter key to continue!")
            case "7":   
                print ("\nExiting Menu. Goodbye!\n")
                break
            case _:
                print("\nInvalid choice. Please try again.")
                input("\nPlease press enter key to continue!")