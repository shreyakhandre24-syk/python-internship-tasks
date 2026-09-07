# Hangman Game

import random

words = ["python", "computer", "programming", "internet", "keyboard"]

word = random.choice(words)

guessed_letters = []

max_attempts = 6
incorrect_guesses = 0

print("================================")
print("       WELCOME TO HANGMAN")
print("================================")

display_word = ["_"] * len(word)

while incorrect_guesses < max_attempts and "_" in display_word:

    print("\nWord:", " ".join(display_word))
    print("Incorrect guesses:", incorrect_guesses)
    print("Remaining attempts:", max_attempts - incorrect_guesses)

    guess = input("Guess a letter: ").lower().strip()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct guess!")

        for i in range(len(word)):
            if word[i] == guess:
                display_word[i] = guess

    else:
        print("Wrong guess!")
        incorrect_guesses += 1

# result
if "_" not in display_word:
    print("\nCongratulations! You won!")
    print("The word was:", word)

else:
    print("\nGame Over!")
    print("The word was:", word)