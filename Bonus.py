secret = "1234"

def count_exact(secret, guess):
    exact = 0
    for i in range(4):
        if secret[i] == guess[i]:
            exact += 1
    return exact

def count_misplaced(secret , guess):
    misplaced =0
    used = [False, False, False, False]
    for i in range (4):
        if secret [i]==guess[i]:
            used[i]=True

    for i in range(4):
        if secret[i] != guess[i]:
            for j in range (4):
                if secret[j]==guess[i]and not used[j]:
                    misplaced +=1
                    used[j]=True
                    break
    return misplaced

def play_game(secret):
    for attempt in range(1, 11):
        print("Attempt", attempt, "of 10")
        guess = input("Enter your 4-digit guess: ")

        while len(guess) != 4 or not guess.isdigit():
            print("Invalid input. Enter exactly 4 digits.")
            guess = input("Enter your 4-digit guess: ")

        exact = count_exact(secret, guess)
        misplaced = count_misplaced(secret, guess)
        print("EXACT:", exact, "| MISPLACED:", misplaced)

        if exact == 4:
            return True
    return False

if play_game(secret):
    print("Vault unlocked! You cracked the code!")
else:
    print("Vault locked forever... The code was", secret)