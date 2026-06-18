# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable.

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: _"How do I keep a variable from resetting in Streamlit when I click a button?"_
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

The game is a number guessing game built with Streamlit where the player tries to guess a secret number between 1 and 100 within a limited number of attempts.

Bugs found:

- Hint messages were inverted: guessing too low returned "Go LOWER!" and guessing too high returned "Go HIGHER!"
- On even-numbered attempts, the secret number was converted to a string, breaking numeric comparison and causing wrong hints through lexicographic fallback
- The "New Game" button did not reset the game state after a game over
- The game accepted numbers outside the 1-100 range without rejecting them
- The secret number was visible in the Developer Debug Info panel

Fixes applied:

- Swapped the hint messages in `check_guess` so they return the correct direction
- Removed the string conversion logic that was corrupting even-numbered attempts
- Moved `check_guess` and related functions into `logic_utils.py` and updated the import in `app.py`

## 📸 Demo Walkthrough

1. User opens the game and sees a prompt to guess a number between 1 and 100
2. User guesses 40 and the game returns "Go HIGHER!" since the secret is 85
3. User guesses 70 and the game returns "Go HIGHER!" again
4. User guesses 90 and the game returns "Go LOWER!"
5. User guesses 85 and the game returns "Correct!" with balloons and a final score

## 🧪 Test Results

pytest

======================================= test session starts ========================================

platform win32 -- Python 3.14.0, pytest-9.0.3, pluggy-1.6.0

collected 5 items
tests\test_game_logic.py ..... [100%]
====================================== 5 passed in 0.15s =======================================

## 🚀 Stretch Features

- [ ] No stretch features completed for this submission
