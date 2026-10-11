def count_exact(secret, guess):
    """Count digits in the correct positions."""
    count = 0

    for i in range(4):
        if secret[i] == guess[i]:
            count += 1

    return count


def count_misplaced(secret, guess):
    """Count correct digits in the wrong positions."""
    count = 0

    for i in range(4):
        if secret[i] != guess[i]:
            for j in range(4):
                if i != j and secret[i] == guess[j]:
                    count += 1
                    break

    return count


def run_game():
    """Run the Alien Vault game with six attempts."""
    secret = "4271"

    for attempt in range(6):
        guess = input("Enter your guess: ")

        if len(guess) != 4 or not guess.isdigit():
            print("Invalid guess! Enter exactly 4 digits.")
            continue

        exact = count_exact(secret, guess)
        misplaced = count_misplaced(secret, guess)

        print("EXACT:", exact)
        print("MISPLACED:", misplaced)

        if exact == 4:
            print("Congratulations! You cracked the vault!")
            return

    print("Game over! The secret code was", secret)


run_game()
