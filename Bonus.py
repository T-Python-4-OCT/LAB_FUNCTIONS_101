def count_exact(secret: str, guess: str) -> int:
    exact = 0
    for i in range(len(secret)):
        if guess[i] == secret[i]:
            exact += 1
    return exact

def count_misplaced(secret: str, guess: str) -> int:
    secret_list = list(secret)
    guess_list = list(guess)
    misplaced = 0
    
    for i in range(len(secret_list) - 1, -1, -1):
        if guess_list[i] == secret_list[i]:
            secret_list.pop(i)
            guess_list.pop(i)
            
    for digit in guess_list:
        if digit in secret_list:
            misplaced += 1
            secret_list.remove(digit)
            
    return misplaced

def play_alien_vault():
    secret_code = "4271"
    attempts = 6
    
    print("Welcome to the Alien Vault!")
    
    while attempts > 0:
        print(f"\nAttempts remaining: {attempts}")
        player_guess = input("Enter your 4-digit guess: ")
        
        if len(player_guess) != 4 or not player_guess.isdigit():
            print("Invalid input! Please enter 4 digits.")
            continue
            
        if player_guess == secret_code:
            print("Congratulations! You cracked the vault!")
            return
            
        exact = count_exact(secret_code, player_guess)
        misplaced = count_misplaced(secret_code, player_guess)
        
        print(f"EXACT: {exact} | MISPLACED: {misplaced}")
        
        attempts -= 1
        
    print("\nGame over! You ran out of attempts.")

play_alien_vault()