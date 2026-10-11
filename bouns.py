def count_exact(secret, guess):
    """
    Counts digits that are correct and in the correct position.
    """
    exact = 0

    for i in range(4):
        if secret[i] == guess[i]:
            exact += 1

    return exact


def count_misplaced(secret, guess):
    """
    Counts correct digits that are in the wrong position.
    Each digit is counted only once.
    """
    remaining_secret = []
    remaining_guess = []

    for i in range(4):
        if secret[i] == guess[i]:
            continue

        remaining_secret.append(secret[i])
        remaining_guess.append(guess[i])

    misplaced = 0

    for digit in remaining_guess:
        if digit in remaining_secret:
            misplaced += 1
            remaining_secret.remove(digit)

    return misplaced


def run_game():
    """
    Runs the alien vault game and gives the player 6 attempts.
    """
    secret_code = "4271"
    attempts = 6

    print("Welcome to the Alien Vault!")
    print("Guess the 4-digit secret code.")

    for attempt in range(attempts):
        guess = input("Enter your 4-digit guess: ")

        if len(guess) != 4 or not guess.isdigit():
            print("Please enter exactly 4 digits.")
            continue

        exact = count_exact(secret_code, guess)
        misplaced = count_misplaced(secret_code, guess)

        print("EXACT:", exact)
        print("MISPLACED:", misplaced)

        if exact == 4:
            print("Congratulations! You cracked the vault!")
            return

    print("You failed to crack the vault!")
    print("The secret code was:", secret_code)


run_game()