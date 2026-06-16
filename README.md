# 🪢 Hangman Game

A classic terminal-based Hangman game built with Python.

---

## 📋 Description

This is a command-line Hangman game where the player tries to guess a hidden word one letter at a time. With each wrong guess, the hangman drawing progresses. You have **6 chances** before the game is over.

---

## 🚀 How to Run

Make sure you have Python 3 installed, then run:

```bash
python hangman.py
```

---

## 🎮 How to Play

1. A random word is chosen from the word list.
2. The word is shown as underscores: `_ _ _ _ _ _`
3. Type a single letter and press Enter to guess.
4. If the letter is in the word, it is revealed in its correct position(s).
5. If the letter is **not** in the word, a part of the hangman is drawn and your remaining guesses decrease by 1.
6. Keep guessing until you either complete the word or run out of chances!

---

## 📸 Sample Output

```
   +---+
   |   |
   0   |
  /|\  |
  / \  |
       |
=========

 Wrong Guesses left: 1
 Letters Guessed : a, e, i, o, p, r, s, t, u

 word  p y _ _ o n
```

---

## 📁 Project Structure

```
hangman.py   # Main game file — all logic lives here
README.md    # Project documentation
```

---

## ⚙️ Features

- Randomly selects a word each round
- Tracks all previously guessed letters
- Validates input (single alphabetic character only)
- Displays the hangman ASCII art stage by stage
- Option to play again after each round

---

## 🗂️ Word List

The current word bank includes:

| Word |
|------|
| hangman |
| python |
| network |
| signal |
| program |

You can expand the list by adding more words to the `WORDS` variable in `hangman.py`:

```python
WORDS = ["hangman", "python", "network", "signal", "program", "your_new_word"]
```

---

## 🛠️ Requirements

- Python 3.x
- No external libraries needed — uses only the built-in `random` module

---

## 💡 Possible Improvements

- Load words from an external `.txt` file for a larger word bank
- Add difficulty levels (easy / medium / hard word lengths)
- Track and display the player's win/loss score across rounds
- Add a hint feature

---

## 👩‍💻 Author

**Pritikka** — [GitHub Profile](https://github.com/pritikka2704)

Built as a Python learning project.
