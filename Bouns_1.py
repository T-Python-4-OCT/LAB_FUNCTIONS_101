"""Alien vault code-breaking game."""


def count_exact(secret_code: str, guess: str) -> int:
    """Return how many digits are both correct and in the same position."""
    return sum(1 for secret_digit, guessed_digit in zip(secret_code, guess) if secret_digit == guessed_digit)


def count_misplaced(secret_code: str, guess: str) -> int:
    """Return how many correct digits are present but in the wrong position."""
    if len(secret_code) != len(guess):
        raise ValueError("Secret code and guess must have the same length.")

    remaining_secret = []
    remaining_guess = []

    for secret_digit, guessed_digit in zip(secret_code, guess):
        if secret_digit != guessed_digit:
            remaining_secret.append(secret_digit)
            remaining_guess.append(guessed_digit)

    misplaced = 0
    for digit in set(remaining_secret):
        misplaced += min(remaining_secret.count(digit), remaining_guess.count(digit))

    return misplaced


def run_game(secret_code: str = "4271", max_attempts: int = 6) -> bool:
    """Run the vault game and return True if the player wins."""
    print("Welcome to the Alien Vault 👽")
    print("Crack the 4-digit code before your 6 attempts run out.")

    for attempt in range(1, max_attempts + 1):
        while True:
            guess = input(f"Attempt {attempt}/{max_attempts}: Enter a 4-digit guess: ")
            if guess.isdigit() and len(guess) == 4:
                break
            print("Invalid input. Please enter exactly 4 digits.")

        exact = count_exact(secret_code, guess)
        misplaced = count_misplaced(secret_code, guess)

        print(f"EXACT: {exact}")
        print(f"MISPLACED: {misplaced}")

        if guess == secret_code:
            print(f"Victory! You cracked the vault in {attempt} attempts.")
            return True

    print(f"Mission failed! The secret code was {secret_code}.")
    return False


def main() -> None:
    """Start the game when the file is run directly."""
    run_game()


if __name__ == "__main__":
    main()
