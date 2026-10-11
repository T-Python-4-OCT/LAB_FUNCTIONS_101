print("Welcome to the spaceship.")
print("To open the safe, enter a number")
number_the_safe = "4271"
attempts = 10
def count_number_the_safe (number_the_safe: str, guess: str) -> int:
    """
    Count the digits that are correct AND in the correct position.

    Args:
        number_the_safe: the secret code (4 digits as a string).
        guess: the player's guess (4 digits as a string).

    Returns:
        int: the number of EXACT matches.
    """
    result =0
    for i in range (len(number_the_safe)):
        if number_the_safe [i] == guess [i]:
            result += 1
    return result
def count_misplaced(number_the_safe: str, guess) -> int:
    """
    Count the digits that exist in the secret code but are in the wrong position.
    Each digit in the secret code can only be matched once.

    Args:
        number_the_safe: the secret code (4 digits as a string).
        guess: the player's guess (4 digits as a string).

    Returns:
        int: the number of MISPLACED digits.
    """
    secret_left = []
    guess_left = []
    for i in range(len(number_the_safe)):
        if number_the_safe [i] != guess[i]:
            secret_left.append(number_the_safe[i])
            guess_left.append(guess[i])

    misplaced = 0
    for digit in guess_left:
        if digit in secret_left:
            misplaced += 1
            secret_left.remove(digit)
    return misplaced
def get_valid_guess() -> str:
    """
    Ask the player for a guess until it is exactly 4 digits.

    Returns:
        str: a valid 4-digit guess.
    """
    while True:
        guess = input("Enter your 4-digit guess: ")
        if len (guess) == 4 and guess.isdigit():
            return guess 
        print ("invalid input ! Enter exactly 4 digits.")

def play_game(number_the_safe: str , attempts: int) -> bool:
    """
    Run the game loop: ask for guesses, show the clues, and check for a win.

    Args:
        number_the_safe: the secret code.
        attempts: the maximum number of guesses allowed.

    Returns:
        bool: True if the player cracked the code, False otherwise.
    """
    for attempt in range(1, attempts + 1):
        print (f"\nAttempt {attempt}/{attempts}")
        guess = get_valid_guess()

        exact = count_number_the_safe(number_the_safe, guess)
        misplaced = count_misplaced (number_the_safe, guess)
        print(f"EXACT: {exact} | MISPLACED: {misplaced}")

        if exact == len(number_the_safe):
            return True 
    return False

if play_game(number_the_safe, attempts):
    print ("\nvault unlocked! you win!")
else:
    print (f"\nvault locked forever... the code was {number_the_safe}.")
    