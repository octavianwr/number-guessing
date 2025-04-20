# cli.py
# Handles user interaction via the command-line interface (CLI)

from game.logic import generate_number, check_guess
from config import MAX_ATTEMPTS

def start_game():
    """
    Run the game loop:
    - Generate a secret number
    - Ask for guesses
    - Give feedback
    - End game on win or attempts over
    """
    secret_number = generate_number()
    for attempt in range(MAX_ATTEMPTS-1):
        print("Number of attempts:", MAX_ATTEMPTS-attempt)
        user_guess = int(input("Enter your guessed number:"))
        guess_result = check_guess(secret_number, user_guess)
        if guess_result == "correct":
            print("Correct!")
            break
        elif guess_result == "low":
            print("Too low!")
        else:
            print("Too high!")
    if attempt == MAX_ATTEMPTS-1:
        print("Max attempt reached, you lose!")
