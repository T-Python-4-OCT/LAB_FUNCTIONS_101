def count_exact(secret_code, guess):
    exact_count = 0

    for index in range(len(secret_code)):
        if secret_code[index] == guess[index]:
            exact_count += 1

    return exact_count

def count_misplaced(secret_code, guess):
    remaining_secret_digits = []
    remaining_guess_digits = []

    for index in range(len(secret_code)):
        if secret_code[index] != guess[index]:
            remaining_secret_digits.append(secret_code[index])
            remaining_guess_digits.append(guess[index])

    misplaced_count = 0

    for digit in remaining_guess_digits:
        if digit in remaining_secret_digits:
            misplaced_count += 1
            remaining_secret_digits.remove(digit)

    return misplaced_count


def run_game(secret_code, max_attempts):
    print("Try to unlock the vault! The code has 4 digits.")

    for attempt in range(1, max_attempts + 1):
        guess = input(f"Attempt {attempt} of {max_attempts}: ")

        if len(guess) != 4 or not all("0" <= digit <= "9" for digit in guess):
            print("Please enter a 4-digit code.")
            continue

        exact = count_exact(secret_code, guess)
        misplaced = count_misplaced(secret_code, guess)

        print(f"EXACT: {exact}")
        print(f"MISPLACED: {misplaced}")

        if exact == len(secret_code):
            print("Your answer is correct! The vault is unlocked.")
            return True

    print(f"You ran out of attempts.")
    return False


run_game("4271", 6)