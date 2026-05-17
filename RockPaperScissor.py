import random

def get_user_choice():
    user_choice = int(input("Enter your Choice: Type 0 for Rock, 1 for Paper, 2 for Scissor. "))
    if user_choice >= 3 or user_choice <0 :
        print("You Entered an invalid number. You lose.")
        return None
    else:
        return user_choice

def get_computer_choice():
    computer_choice = random.randint( 0,2 )
    print("Computer Choice:")
    print(computer_choice)
    return computer_choice

def determine_winner(user_choice, computer_choice):
    if computer_choice == user_choice:
        return "It's a draw."
    elif computer_choice == 0  and user_choice == 2:
        return "You lose."
    elif user_choice == 0 and computer_choice == 2:
        return "You win."
    elif computer_choice > user_choice:
        return "You lose."
    elif user_choice > computer_choice:
        return "You win."

def play_game():
    user_wins = 0
    computer_wins = 0
    play_again = 'yes'

    while play_again.lower() == 'yes':
        print("Let's play Rock, Paper, Scissors!")
        user_choice = get_user_choice()
        if user_choice is not None:
            computer_choice = get_computer_choice()
            print(f"You chose {user_choice}.")
            print(f"Computer chose {computer_choice}.")
            result = determine_winner(user_choice, computer_choice)
            print(result)

            if 'win' in result.lower():
                user_wins += 1
            elif 'lose' in result.lower():
                computer_wins += 1

            play_again = input("Do you want to play again? (yes/no): ")
    print(f"Total wins: User - {user_wins}, Computer - {computer_wins}")
    
play_game()
