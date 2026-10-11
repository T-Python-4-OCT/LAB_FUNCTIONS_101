code = None

def calculates_exact_digits(code, secret_code="4271"):
    """
    Calculates the number of exact digit matches between code and secret_code.
    Args:
        code (str): The code entered by the user.
        secret_code (str, default="4271"): The secret code to compare against.
    Returns:
        int: The number of digits that match in both value and position.
    """
    exact_count = 0
    for i in range(len(code)):
        if code[i] == secret_code[i]:
            exact_count += 1
    return exact_count

def calculates_misplaced_digits(code, secret_code="4271"):
    """
    Calculates the number of misplaced digit matches between code and secret_code.
    Args:
        code (str): The code entered by the user.
        secret_code (str, default="4271"): The secret code to compare against.
    Returns:
        int: The number of digits that match in value but not in position.
    """
    misplaced_count = 0
    remaining_code = ""
    remaining_secret = ""

    # Keep only digits that are NOT exact matches
    for i in range(len(code)):
        if code[i] != secret_code[i]:
            remaining_code += code[i]
            remaining_secret += secret_code[i]

    # Count remaining misplaced digits
    for i in remaining_code:
        if i in remaining_secret:
            misplaced_count += 1

            position = remaining_secret.find(i)

            remaining_secret = (
                remaining_secret[:position]
                + remaining_secret[position + 1:]
            )

    return misplaced_count

def run_game(secret_code="4271"):
    """
    Runs the alien vault game.
    Args:
        secret_code (str, default="4271"): The secret code of the vault.
    Returns:
        bool: True if the player wins, otherwise False.
    """
    attempts = 0

    while attempts < 6:
        code = input("Enter a secret code (4 characters): ")

        if len(code) != 4 or not code.isdigit():
            print("Invalid code. Please enter exactly 4 characters.")
            continue
    
        attempts += 1

        exact_digits = calculates_exact_digits(code , secret_code)
        misplaced_digits = calculates_misplaced_digits(code, secret_code)

        attempts_left = 6 - attempts
        aliens = "👽" * attempts_left

        spaces = 22 - (attempts_left * 2)

        print("+----------------+--------------------+------------------------+")
        print("|  Exact digits  |  Misplaced digits  |     Attempts left      |")
        print("+----------------+--------------------+------------------------+")
        print(f"| {exact_digits:^14} | {misplaced_digits:^18} | {aliens}{' ' * spaces} |")
        print("+----------------+--------------------+------------------------+")

        if exact_digits == 4:
            print("👽👽👽 Vault unlocked! 👽👽👽")
            return True

    print("🔴 ACCESS DENIED 🔴")
    return False

run_game()