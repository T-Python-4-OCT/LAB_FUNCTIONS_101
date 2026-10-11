def count_exact(secret: str, guess: str) -> int:
    """Return how many digits are correct and in the correct position."""
    exact = 0

    for i in range(len(secret)):
        if secret[i] == guess[i]:
            exact += 1
    return exact
def count_misplaced(secret: str, guess: str) -> int:
    """Return how many digits are correct but in the wrong position."""
    matched = 0

    for digit in "0123456789":
        secret_count = secret.count(digit)
        guess_count = guess.count(digit)

        if secret_count < guess_count:
            matched += secret_count
        else:
            matched += guess_count

    return matched - count_exact(secret, guess)


def run_game():
    """Run the alien vault game with up to 6 valid guesses."""
    secret = "4520"
    attempts = 0

    print("Welcome to the Alien Vault!")
    print("You have 6 attempts to crack the 4-digit code.")

    while attempts < 6:
        guess = input("Enter your 4-digit guess: ").strip()

        if len(guess) != 4 or not guess.isascii() or not guess.isdigit():
            print("Please enter exactly 4 digits.")
            continue

        attempts += 1

        exact = count_exact(secret, guess)
        misplaced = count_misplaced(secret, guess)

        print(f"EXACT: {exact}")
        print(f"MISPLACED: {misplaced}")

        if exact == 4:
            print("You cracked the code! The vault is unlocked!")
            return

        print(f"Attempts remaining: {6 - attempts}")

    print(f"You ran out of attempts! The secret code was {secret}.")


run_game()