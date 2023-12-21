# hangman.py
import random

def display_partial_word(word, guessed_letters):
    partial_word = ""
    for letter in word:
        if letter in guessed_letters:
            partial_word += letter
        else:
            partial_word += "-"
    return partial_word

def hangman_game():
    print("HANGMAN")

    while True:
        print('Type "play" to play the game, "exit" to quit: ', end="")
        user_choice = input().lower()

        if user_choice == "exit":
            break
        elif user_choice == "play":
            play_game()
        else:
            print("Invalid choice. Please enter 'play' to play the game or 'exit' to quit.")

def play_game():
    # Список слів
    word_list = ['python', 'java', 'javascript', 'php']

    # Випадково вибране слово
    secret_word = random.choice(word_list)

    guessed_letters = set()

    # Кількість дозволених помилок
    max_attempts = 8
    attempts_left = max_attempts

    while "-" in display_partial_word(secret_word, guessed_letters) and attempts_left > 0:
        print(display_partial_word(secret_word, guessed_letters))
        print(f"Attempts left: {attempts_left}")
        print("Input a letter: > ", end="")
        guessed_letter = input().lower()

        if len(guessed_letter) == 1 and guessed_letter.isalpha() and guessed_letter.islower():
            if guessed_letter in guessed_letters:
                print("You've already guessed this letter")
            elif guessed_letter in secret_word:
                print("No improvements")
                guessed_letters.add(guessed_letter)
            else:
                print("That letter doesn't appear in the word")
                attempts_left -= 1
        else:
            if len(guessed_letter) != 1:
                print("You should input a single letter")
            elif not guessed_letter.islower():
                print("Please enter a lowercase English letter")

    if "-" not in display_partial_word(secret_word, guessed_letters):
        print(f"{secret_word}\nYou guessed the word!\nYou survived!")
    else:
        print("You lost!")

if __name__ == "__main__":
    hangman_game()
