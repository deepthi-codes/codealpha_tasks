import random

# Hangman Game - CodeAlpha Internship Project

words = ["python", "computer", "programming", "student", "developer"]

word = random.choice(words)
guessed_letters = []
attempts = 6

print("=" * 65)
print("       WELCOME TO HANGMAN")
print("=" * 65)
print("Guess the hidden word one letter at a time!")
print("You have", attempts, "wrong attempts available.")

while attempts > 0:
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word.strip())

    if all(letter in guessed_letters for letter in word):
        print("Congratulations! You guessed the word:", word)
        break

    guess = input("Enter a letter: ").lower().strip()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct guess!")
    else:
        attempts -= 1
        print("Wrong guess! Attempts left:", attempts)

else:
    print("\nGame over! The word was:", word)

print("\nThank you for playing Hangman!")