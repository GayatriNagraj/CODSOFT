import random

user_score = 0
computer_score = 0

while True:
    print("Welcome to Rock-Paper-Scissors Game!")
    user_choice = input("Please choose rock, paper, or scissors: ").lower()
    while user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        user_choice = input("Please choose again: ").lower()

    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    print(f"Computer chooses {computer_choice}.")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        print("You win!")
        user_score += 1
    else:
        print("Computer wins!")
        computer_score += 1

    print(f"Your score: {user_score}, Computer's score: {computer_score}")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        print("Thank you for playing!")
        break
