#make it playable

import random

def rock_paper_scissors():
    # List of possible moves
    choices = ['rock', 'paper', 'scissors']
    
    # Ask the player for their move
    player_choice = input("Choose rock, paper, or scissors: ").lower()

    # Check if the player's choice is valid
    if player_choice not in choices:
        print("Invalid choice! Please choose 'rock', 'paper', or 'scissors'.")
        return

    # Computer randomly selects a move
    computer_choice = random.choice(choices)

    # Show both choices
    print(f"\nYou chose: {player_choice}")
    print(f"Computer chose: {computer_choice}")

    # Determine the winner
    if player_choice == computer_choice:
        print("It's a tie!")
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'scissors' and computer_choice == 'paper') or \
         (player_choice == 'paper' and computer_choice == 'rock'):
        print("You win!")
    else:
        print("You lose!")

# Play the game
rock_paper_scissors()

