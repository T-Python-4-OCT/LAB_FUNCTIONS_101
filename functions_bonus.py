
secret_code: str = "4271"
max_attempts: int = 6


def count_exact(secret_code: str, guess: str) -> int:
    """Count digits that match in the correct positions."""
    exact = 0

    for index in range(len(secret_code)):
        if secret_code[index] == guess[index]:
            exact += 1

    return exact


def count_misplaced(secret_code: str, guess: str) -> int:
    """Count correct digits that are in the wrong positions."""
    remaining_secret = []
    remaining_guess = []

    for index in range(len(secret_code)):
        if secret_code[index] != guess[index]:
            remaining_secret.append(secret_code[index])
            remaining_guess.append(guess[index])

    misplaced = 0

    for digit in remaining_guess:
        if digit in remaining_secret:
            misplaced += 1
            remaining_secret.remove(digit)

    return misplaced


def run_game(secret_code: str, max_attempts: int) -> None:
    """Run the alien vault guessing game."""
    print("👽 Welcome to the Alien Vault!")
    print("Crack the 4-digit code to unlock the vault.")

    for attempt in range(1, max_attempts + 1):
        guess = input(f"\nAttempt {attempt}/{max_attempts} - Enter your 4-digit guess: ")

        if len(guess) != 4 or not guess.isdigit():
            print("Invalid input! Enter exactly 4 digits.")
            continue

        exact = count_exact(secret_code, guess)
        misplaced = count_misplaced(secret_code, guess)

        print(f"EXACT: {exact}")
        print(f"MISPLACED: {misplaced}")

        if exact == len(secret_code):
            print("🎉 Vault unlocked! You cracked the code!")
            return

    print(f" Access denied! The secret code was {secret_code}.")


run_game(secret_code, max_attempts)
