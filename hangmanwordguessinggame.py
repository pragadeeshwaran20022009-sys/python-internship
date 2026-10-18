
import random

# List of words
WORDS = [
    "python", "computer", "programming", "electronics",
    "developer", "keyboard", "internet", "science",
    "hangman", "college"
]

# ASCII gallows stages
HANGMAN = [
    """
      +---+
      |   |
          |
          |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\\  |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\\  |
     /    |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\\  |
     / \\  |
          |
    =========
    """
]


def display_word(word, guessed_letters):
    """Display guessed letters and hide the remaining letters."""
    return " ".join(
        letter if letter in guessed_letters else "_"
        for letter in word
    )


def play_hangman():
    word = random.choice(WORDS).upper()
    guessed_letters = set()
    wrong_guesses = set()
    max_attempts = 6

    print("=" * 40)
    print("     HANGMAN WORD GUESSING GAME")
    print("=" * 40)
    print("Guess the hidden word one letter at a time!")
    print(f"You have {max_attempts} incorrect guesses allowed.")

    while len(wrong_guesses) < max_attempts:
        mistakes = len(wrong_guesses)

        print(HANGMAN[mistakes])
        print("\nWord:", display_word(word, guessed_letters))
        print("Guessed letters:",
              " ".join(sorted(guessed_letters | wrong_guesses))
              or "None")
        print("Attempts remaining:", max_attempts - mistakes)

        # Check whether the player has won
        if all(letter in guessed_letters for letter in word):
            print("\nCongratulations! You guessed the word:", word)
            return

        guess = input("\nEnter a letter: ").strip().upper()

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter exactly one alphabet letter.")
            continue

        # Prevent duplicate guesses
        if guess in guessed_letters or guess in wrong_guesses:
            print("You already guessed that letter. Try another!")
            continue

        # Process the guess
        if guess in word:
            guessed_letters.add(guess)
            print("Correct guess!")
        else:
            wrong_guesses.add(guess)
            print("Incorrect guess!")

    # Display final stage and reveal the word
    print(HANGMAN[max_attempts])
    print("\nGame over! You ran out of attempts.")
    print("The correct word was:", word)


if __name__ == "__main__":
    play_hangman()
