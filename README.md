# 🎯 Number Guessing Game (CLI)

A fun and interactive command-line number guessing game built with Python!  
Test your intuition and logic as you try to guess a secret number in a limited number of attempts.

---

## 🕹️ How the Game Works

- A random number is generated between a minimum and maximum range.
- You have a set number of attempts to guess the correct number.
- After each guess, you’ll receive a hint:
  - 📉 "Too low!" – try a higher number.
  - 📈 "Too high!" – try a lower number.
  - ✅ "Correct!" – you nailed it!
- The game ends when you guess correctly or run out of attempts.

---

## Getting Started

### ✅ Requirements

- Python 3.6 or higher

### To Run the Game

Open a terminal and run:

```bash
python main.py
```

## Project Structure

``` bash
number_guessing_game/
│
├── main.py                 # Entry point to run the game
├── config.py               # Game configuration settings (e.g. number range, max attempts)
├── game/
│   ├── __init__.py
│   ├── logic.py            # Core logic (generate number, check guess)
│   └── cli.py              # Command-line interface and user interaction
│
├── tests/
│   ├── __init__.py
│   └── test_logic.py       # Unit tests for the game logic
│
└── README.md               # This file
```

## Ideas for Improvement

Want to take it further? Here are a few ideas:
- Add difficulty levels (easy, medium, hard)
- Keep track of and display the number of attempts used
- Let players restart the game after finishing
- Add colorized text for feedback using libraries like colorama
- Make a web or GUI version using Flask or Tkinter