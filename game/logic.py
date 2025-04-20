# logic.py
# Handles core game logic (e.g., number generation, checking guesses)

import random
from config import MIN_NUMBER, MAX_NUMBER

def generate_number():
    """
    Generate a random number between MIN_NUMBER and MAX_NUMBER.
    """
    return random.randint(MIN_NUMBER, MAX_NUMBER)

def check_guess(secret_number, user_guess):
    """
    Compare user's guess with the secret number.
    Return:
        - "correct" if guessed right
        - "low" if guess is too low
        - "high" if guess is too high
    """
    if secret_number == user_guess:
        return "correct"
    elif secret_number > user_guess:
        return "low"
    else:
        return "high"
