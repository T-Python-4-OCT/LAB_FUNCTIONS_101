
    
kye = "4271"

def Exact(num):
    '''a function give you the Exact place of a number'''
    count = 0
    for i in range(4):
        if num[i] == kye[i]:
            count += 1
    return count



def MISPLACED(mis):
    ''' a function that told you if there is any corect number but it is not in the corect place'''
    secret_rem = ""
    guess_rem = ""
    for i in range(4):
        if mis[i] != kye[i]:
            secret_rem += kye[i]
            guess_rem += mis[i]
    count = 0
    for char in guess_rem:
        if char in secret_rem:
            count += 1
            secret_rem = secret_rem.replace(char, "", 1)
    return count



def play_game():
    '''function that start the game'''
    attempts = 6
    print("Welcome to the Crack the Alien Vault Game!")
    print("You have 6 attempts to crack the 4-digit code.\n")
    
    for attempt in range(1, attempts + 1):
        guess = input(f"Attempt {attempt}/6 - Enter 4 numbers for the  code: ")
        
        if len(guess) != 4 or not guess.isdigit():
            print("Invalid input. Please enter exactly 4 digits.\n")
            continue
            
        if guess == kye:
            print(f"\n You successfully cracked the vault in attempt {attempt}!")
            return
            
        exact_results = Exact(guess)
        misplaced_results = MISPLACED(guess)
        
        print(f"EXACT: {exact_results} | MISPLACED: {misplaced_results}\n")
        
    print(f"\n[Game Over] You ran out of attempts. The secret code was {kye}.")
    
    
play_game()
    





        
    
    
        
    
    
    