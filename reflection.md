# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

When I first ran the game, it looked functional on the surface, a number guessing game with a clean interface and a debug panel showing the secret number, attempts, and score. But as soon as I started playing, things fell apart quickly. The hints were inconsistent and misleading, the "New Game" button did nothing after a game over, and the game accepted numbers outside the stated 1–100 range without any error. After asking my AI assistant to trace the hint bug, I found two root causes: the hint messages in `check_guess` are inverted (too low returns "Go LOWER!" instead of "Go HIGHER!"), and on even-numbered attempts `app.py` converts the secret number to a string, which breaks numeric comparison entirely and causes wrong results through a lexicographic fallback.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| Guessed 34, then 45 | Consistent higher/lower hints | Hints contradicted each other | none |
| Clicked "New Game" after game over | Game resets with a new secret number | Game over screen persists, nothing resets | none |
| Guessed 130 (outside 1-100 range) | Input rejected or error shown | Game accepted it and returned "Go Higher" | none |
| Opened developer debug info | Secret number hidden from player | Secret number visible in debug panel | none |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.