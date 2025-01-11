import random

# List of words for the game
word_list = ["python", "hangman", "programming", "developer", "computer", "software","keyboard", "internet"]
 

def get_random_word():
    """Select a random word from the word list."""
    return random.choice(word_list)

def print_word(word, guessed_letters):
    """Print the current state of the word with underscores for unguessed letters."""
    display = [letter if letter in guessed_letters else '_' for letter in word]
    print(" ".join(display))

def check_guess(guess, word, guessed_letters):
    """Check if the guess is correct, update the guessed letters, and return the result."""
    if guess in guessed_letters:
        print(f"You've already guessed the letter '{guess}'")
        return False
    
    if guess in word:
        guessed_letters.add(guess)
        print(f"Good guess! The letter '{guess}' is in the word.")
        return True
    else:
        print(f"Oops! The letter '{guess}' is not in the word.")
        return False

def hangman_game():
    # Initialize game variables
    word = get_random_word()
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect_guesses = 6  # You can set the number of allowed incorrect guesses

    print("Welcome to Hangman!")

    # Main game loop
    while incorrect_guesses < max_incorrect_guesses:
        print("\nCurrent word: ", end="")
        print_word(word, guessed_letters)

        print(f"\nIncorrect guesses left: {max_incorrect_guesses - incorrect_guesses}")
        guess = input("Guess a letter: ").lower()

        # Validate input (single alphabet character)
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a valid single letter.")
            continue
        
        # Check the guess and update game state
        if not check_guess(guess, word, guessed_letters):
            incorrect_guesses += 1

        # Check if the player has guessed all letters
        if all(letter in guessed_letters for letter in word):
            print(f"\nCongratulations! You've guessed the word: {word}")
            break
    else:
        print(f"\nSorry! You've run out of guesses. The word was: {word}")

# Run the game
hangman_game()
