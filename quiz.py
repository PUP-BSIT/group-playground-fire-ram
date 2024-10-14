import os

# input the choice of number of the user
# choices must be from a to d 
# it should be case sensetive
# it will add 1 point every time it's correct
total_score = 0

while True:
    os.system ('cls')

    print ("1. What is the largest animal in the world")
    print ("2. What part of the body is the most largest")
    print ("3. What animal has the highest death rate")
    print ("4. How many chromosomes does human have")
    print ("5. Where is the largest rainforest in the world")
    print ("Type Quit if your want to quit the quiz")
    choice = input("Enter your choie of problem: ")
    os.system('cls')
    if choice == "Quit" or choice == "quit":
        print (f"Thank you for playing the game, Your total score is: {total_score}")
        break

    match choice:
        case "1":
            os.system('cls')
            print ("Who is the largest animal in the choice ?")
            print ("a). Whale               ""b). Ant")
            print ("c). Eagle               ""d). Greatwhite Shark")
            prob_1 = input ("Enter the correct answer in the problem: ")
            if prob_1 == "A" or prob_1 == "a":
                total_score = total_score + 1
                print ("Your answer is correct")
                input ("Press Enter to continue to the game")
            else:
                print ("Answer is not correct")
                input ("Press Enter to continue to the game")
                
        case "2":
            os.system('cls')
            print ("What part of the body is the most larget ? ")
            print ("a). Heart               ""b). Brain")
            print ("c). Intestine               ""d). Skin")
            prob_2 = input ("Enter the correct answer in the problem: ")

            if prob_2 == "D" or prob_2 == "d":
                total_score = total_score + 1
                print ("Your answer is correct")
                input ("Press Enter to continue to the game")
              
            else:
                print("Answer is not correct")
                input ("Press Enter to continue to the game")

        case "3":
            os.system('cls')
            print ("What is the animahl has the highest death rate")
            print ("a). Shark               ""b). Dog")
            print ("c). Eagle               ""d). Mosquito")
            prob_3 = input("Enter the correct answer in the problem: ")

            if prob_3 == "D" or prob_3 == "d":
                total_score = total_score + 1
                print ("Your answer is correct")
                input ("Press Enter to continue to the game")
                
            else:
                print ("Your answer is incorrect")
                input ("Press Enter to continue to the game")

        case "4":
            os.system ('cls')
            print ("How many total chromosome does human have ?")
            print ("a). 23               ""b). 48")
            print ("c). 32               ""d). 46")
            prob_4 = input ("Enter the correct answer in the problem: ")
            if prob_4 == "D" or prob_4 == "d":
                total_score = total_score + 1
                print ("Your answer in correct")
                input ("Press Enter to continue to the game")
                
            else:
                print ("Your answer is incorrect")
                input ("Press Enter to continue to the game")

        case "5":
            os.system ('cls')
            print ("Where is the largest rainforest in the world ?")
            print ("a). Mexico               ""b). South America")
            print ("c). Africa               ""d). North America")
            prob_5 = input ("Enter the correct answer in the problem: ")
            if prob_5 == "B" or prob_5 == "b":
                total_score = total_score + 1
                print ("Your answer is correct")
                print (f"Your current score is {total_score}")
                input ("Thank you for playing the game")
                break
               
            else:
                print ("Your answer is incorrect")
                print (f"Your current score is {total_score}")
                input ("Thank you for playing the game")
                break

        case _:
            print ("Invalid choice of problem")