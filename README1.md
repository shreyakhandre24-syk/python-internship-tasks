# 🎮 Hangman Game

A simple **Hangman Game built using Python**. The player has to guess the hidden word one letter at a time. The player gets a maximum of **6 incorrect attempts**.

## 📌 Project Description

This Python-based Hangman game randomly selects a word from a predefined list. The player guesses letters to reveal the hidden word.

If the player guesses a correct letter, it is displayed in its correct position. If the guess is incorrect, the number of incorrect attempts increases.

The game ends when:

* The player successfully guesses the complete word 🎉
* The player reaches 6 incorrect guesses 💀

## 🛠️ Technologies Used

* **Python**
* `random` module

## ✨ Features

* Random word selection
* Letter-by-letter guessing
* Maximum 6 incorrect attempts
* Prevents duplicate guesses
* Input validation
* Displays remaining attempts
* Shows the final result
* Simple command-line interface

## 📂 Project Structure

```text
Hangman-Game/
│
├── hangman.py
└── README.md
```

## 📝 Words Used

The game randomly selects one word from the following list:

```python
words = ["python", "computer", "programming", "internet", "keyboard"]
```

## ▶️ How to Run

### Step 1: Install Python

Make sure Python is installed on your computer.

Check Python installation using:

```bash
python --version
```

### Step 2: Save the Code

Save the Hangman program as:

```text
hangman.py
```

### Step 3: Run the Program

Open the terminal in the project folder and run:

```bash
python hangman.py
```

## 🎯 How to Play

1. Start the game.
2. A random word will be selected.
3. The hidden word will be displayed using underscores (`_`).
4. Enter one letter at a time.
5. Correct letters will be revealed.
6. Incorrect guesses reduce your remaining attempts.
7. You have a maximum of **6 incorrect guesses**.
8. Guess the complete word before your attempts run out to win.

## 💻 Sample Output

```text
================================
       WELCOME TO HANGMAN
================================

Word: _ _ _ _ _ _
Incorrect guesses: 0
Remaining attempts: 6

Guess a letter: p
Correct guess!

Word: p _ _ _ _ _
Incorrect guesses: 0
Remaining attempts: 6

Guess a letter: z
Wrong guess!

Word: p _ _ _ _ _
Incorrect guesses: 1
Remaining attempts: 5
```

## 🏆 Winning Condition

The player wins when all letters in the hidden word are correctly guessed.

```text
Congratulations! You won!
The word was: python
```

## ❌ Losing Condition

The player loses when they make 6 incorrect guesses.

```text
Game Over!
The word was: computer
```

## 📚 Concepts Used

This project demonstrates the following Python concepts:

* Variables
* Lists
* Loops
* Conditional statements
* `if-else`
* `while` loop
* `for` loop
* Functions from modules
* User input
* String methods
* Random word selection

## 🚀 Future Improvements

The game can be improved by adding:

* Different difficulty levels
* Hangman graphics
* More words
* Hints
* Score system
* Multiple rounds
* Timer
* Categories such as Animals, Countries, Movies, etc.

## 👩‍💻 Author

**Shreya Khandre**

## 📄 License

This project is created for **learning and educational purposes**.
