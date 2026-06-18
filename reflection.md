# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

When I first ran the game, it looked functional on the surface, a number guessing game with a clean interface and a debug panel showing the secret number, attempts, and score. But as soon as I started playing, things fell apart quickly. The hints were inconsistent and misleading, the "New Game" button did nothing after a game over, and the game accepted numbers outside the stated 1–100 range without any error. After asking my AI assistant to trace the hint bug, I found two root causes: the hint messages in `check_guess` are inverted (too low returns "Go LOWER!" instead of "Go HIGHER!"), and on even-numbered attempts `app.py` converts the secret number to a string, which breaks numeric comparison entirely and causes wrong results through a lexicographic fallback.

**Bug Reproduction Log**

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| Guessed 34, then 45 | Consistent higher/lower hints | Hints contradicted each other | none |
| Clicked "New Game" after game over | Game resets with a new secret number | Game over screen persists, nothing resets | none |
| Guessed 130 (outside 1-100 range) | Input rejected or error shown | Game accepted it and returned "Go Higher" | none |
| Opened developer debug info | Secret number hidden from player | Secret number visible in debug panel | none |

---

## 2. How did you use AI as a teammate?

I used Claude as my AI coding assistant throughout this project. When I described the hint bug, guessing 12 against a secret of 85 and getting "Go Lower," Claude correctly identified two root causes: the hint messages in `check_guess` were swapped, and a separate bug was converting the secret to a string on even-numbered attempts, which broke numeric comparison entirely. I verified this by reading the code myself and confirming the logic matched Claude's explanation. However, when Claude generated the pytest tests, it wrote assertions like `assert result == "Win"`, which failed immediately because `check_guess` returns a tuple, not a plain string. I caught this by running pytest, reading the error output, and correcting the assertions to `assert result[0] == "Win"`.

---

## 3. Debugging and testing your fixes

I decided a bug was fixed when both the automated tests passed and the live game behaved correctly in the browser. After fixing the inverted hints and moving `check_guess` into `logic_utils.py`, I ran `pytest` and all 5 tests passed, which confirmed the function was returning the right outcomes for winning, too high, and too low guesses. I also ran the game with Streamlit and manually tested guesses above and below the secret number to confirm the hints made sense. Claude helped generate the initial test structure, but I had to correct the assertions myself after they failed, which showed me that AI-generated tests still need to be read and verified before trusting them.

---

## 4. What did you learn about Streamlit and state?

Streamlit works differently from most frameworks. Every time a user clicks a button or types something, the entire script runs again from the top. This means any variable you define normally gets reset on every interaction. Session state is how Streamlit remembers things across those reruns: it acts like a small storage box that persists between script executions. So if you want to keep track of a score, a secret number, or how many attempts a player has made, you store it in `st.session_state` instead of a regular variable. Without it, the game would forget everything the moment a user clicked submit.

---

## 5. Looking ahead: your developer habits

One habit I want to carry forward is adding FIXME comments before touching any code. Marking the exact location of the problem before asking AI to fix it kept me focused and made the AI's suggestions more targeted. One thing I would do differently is run the code manually before trusting any AI-generated tests, since the pytest assertions Claude wrote looked correct but failed immediately. This project changed how I think about AI-generated code: it can identify problems and explain logic accurately, but it makes assumptions about return types and structure that you have to verify yourself. The code looking right and the code being right are not the same thing.