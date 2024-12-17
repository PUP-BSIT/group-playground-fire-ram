import random
import os

unset_option = -1
exit_option = 0

class CardGame:
    list_of_account = []
    def __init__(self, name, pin, age, balance_user):
        self.name = name
        self.pin = pin
        self.age = age
        self.balance_user = balance_user

    def create_account (self):
        num_account = int(input("Enter the number of account: "))
        for num in range (num_account):
            print(f"Account number {num}")
            user_name = str(input("Enter your username: "))
            user_pin = str(input("Enter your user pin: "))
            user_age = int(input("Enter your age: "))
            user_balance = 0
            account = CardGame(user_name, user_pin, user_age, user_balance)
            CardGame.list_of_account.append(account)

    def user_information(self):
            print (f"Your name is: {self.name}")
            print (f"Your user pin is: {self.pin}")
            print (f"Your age is: {self.age}")
            print (f"Your current balance is: {self.balance_user}")
    
    def user_information_display ():
        account_finder = int(input("Enter a number to find your account "
                                   + "start from 0: "))
        if CardGame.list_of_account:
            CardGame.list_of_account[account_finder].user_information()
        else:
            print ("No accounts found")

    def registerd_account ():
        print ("List of account")
        if CardGame.list_of_account:
            for account in CardGame.list_of_account:
                account.user_information()
                print ("-" * 30)
        else:
            print ("No accounts")

    def input_balance (self):
        if self.age >= 18 and self.balance_user <= 0:
            print ("Please input a balance")
            user_input_balance = int(input("Top up : "))
            self.balance_user += user_input_balance
            print (f"Your total balance is: {self.balance_user}")
        elif self.age <= 17:
            print ("Age restricted")
            return
    
    def input_balance_display ():
        choce_account = int(input("Enter your number of account: "))
        if CardGame.list_of_account:
            CardGame.list_of_account[choce_account].input_balance()
        else:
            print("No accound found")

    def card_game (self):
        if self.balance_user > 0:
            print ("Card game Baccarat")
            choice = input("Y to continue N to return to main menu: ")

            if choice == "Y":
                place_bet = input("Placebet (Banker/Player): ")
                money_bet = int(input("Enter your bet: "))
                card_one = random.randint(1, 9)
                card_two = random.randint(1,9)
                card_three = random.randint(1,9)
                card_four = random.randint(1,9)
                result_banker = (card_one + card_two) % 10
                result_player = (card_three + card_four) % 10

                print (f"The result of banker: {result_banker}")
                print (f"The result of player: {result_player}")

                if place_bet == "Banker":
                    if result_banker > result_player:
                        print ("Congratulations you win")
                        self.balance_user += money_bet
                    elif result_banker < result_player:
                        print ("Sorry you lose")
                        self.balance_user -= money_bet

                    elif result_player == result_banker:
                        print ("It's a draw")
                        self.balance_user = self.balance_user

                if place_bet == "Player":
                    if result_player > result_banker:
                        print ("Congratulations you win")
                        self.balance_user += money_bet
                    elif result_player < result_banker:
                        print ("Sorry you lose")
                        self.balance_user -= money_bet
                    elif result_player == result_banker:
                        print ("It's a draw")
                        self.balance_user = self.balance_user
        else:
            print ("Thank you")
            pass

    def card_game_display ():
        choce_account = int(input("Enter your number of account: "))
        if CardGame.list_of_account:
            CardGame.list_of_account[choce_account].card_game()
        else:
            print("No accound found")
            


    def menu():
        os.system("cls")
        main_choice = unset_option
        while main_choice != exit_option:
            main_choice = CardGame.display_choice()
            CardGame.process_choice(main_choice)

    def display_choice ():
        os.system("cls")
        print ("1. Create account")
        print ("2. Information")
        print ("3. Registered account")
        print ("4. Input a balance")
        print ("5. Card game")
        print ("0. Exit")

        return int(input("Enter your choice: "))

    def process_choice (main_choice):
        match main_choice:
            case 1:
                os.system("cls")
                game = CardGame("", "", 0, 0)
                game.create_account()
                input()
            case 2:
                os.system("cls")
                CardGame.user_information_display()
                input()
            case 3:
                os.system("cls")
                CardGame.registerd_account()
                input()
            case 4:
                os.system("cls")
                CardGame.input_balance_display()
                input()
            case 5:
                os.system("cls")
                CardGame.card_game_display()
                input()
            case _:
                return

