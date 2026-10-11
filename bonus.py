def count_exact(secret: str, guess: str) -> int:
  exact_count = 0
  for i in range(len(secret)):
    if guess[i] == secret[i]:
      exact_count += 1
  return exact_count

def count_misplaced(secret: str, guess: str) -> int:
  misplaced_count = 0
  secret_list = list(secret)
  guess_list = list(guess)

  
  for i in range(len(secret_list) - 1, -1, -1):
    if guess_list[i] == secret_list[i]:
      secret_list.pop(i)
      guess_list.pop(i)

 
  for g in guess_list:
    if g in secret_list:
      misplaced_count += 1
      secret_list.remove(g) 

  return misplaced_count

def play_game():
  secret_code = "4271"
  attempts = 6

  print("Welcome to Crack the Alien Vault!")
  print("You have 6 attempts to guess the 4-digit secret code.")

  for attempt in range(1, attempts + 1):
    guess = input(f"\nAttempt {attempt}/6 - Enter your 4-digit guess: ")

    if guess == secret_code:
      print(" Victory! You cracked the alien vault!")
      return

    exact = count_exact(secret_code, guess)
    misplaced = count_misplaced(secret_code, guess)

    print(f"EXACT: {exact} | MISPLACED: {misplaced}")

  print("\n Game Over! You ran out of attempts. The vault remains locked.")

play_game()