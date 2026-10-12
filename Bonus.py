
secret_code = "4271"


def count_exact(secret_code, player_guess):
    """Count correct digits in the correct position."""
    exact_count = 0

    for position in range(4):
        if secret_code[position] == player_guess[position]:
            exact_count += 1

    return exact_count


def count_misplaced(secret_code, player_guess):
    """Count correct digits in the wrong position."""
    remaining_secret = []
    remaining_guess = []

    for position in range(4):
        if secret_code[position] != player_guess[position]:
            remaining_secret.append(secret_code[position])
            remaining_guess.append(player_guess[position])

    misplaced_count = 0

    for digit in remaining_guess:
        if digit in remaining_secret:
            misplaced_count += 1
            remaining_secret.remove(digit)

    return misplaced_count


def run_game():
    """Run the game with 6 attempts."""
    for attempt in range(6):
        player_guess = input("Enter your 4-digit guess: ")

        exact_count = count_exact(secret_code, player_guess)
        misplaced_count = count_misplaced(secret_code, player_guess)

        print("EXACT:", exact_count)
        print("MISPLACED:", misplaced_count)

        if exact_count == 4:
            print("Congratulations! You cracked the vault!")
            return

    print("Game over! The secret code was", secret_code)


run_game()

print(count_exact.__doc__)
print(count_misplaced.__doc__)
print(run_game.__doc__)
