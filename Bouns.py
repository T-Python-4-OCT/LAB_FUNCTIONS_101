def AlienTechnology():
  PlayerGuess = (input('PLEASE GUESS THE SECRET CODE: '))
  SecretCode = '4271'
  RestCode = list(SecretCode)

  if len(PlayerGuess) > 4 or len(PlayerGuess) < 4 or not PlayerGuess.isdigit():
    print('ENTER EXACTLY 4 DIGITS PLEASE!')
    return

  Exact = 0
  for number in range(4) :
    if PlayerGuess[number] == SecretCode[number] :
      Exact += 1
      RestCode.remove(PlayerGuess[number])

  Misplaced = 0
  for number in range(4) :
    if PlayerGuess[number] != SecretCode[number] :

      if PlayerGuess[number] in RestCode :
        RestCode.remove(PlayerGuess[number])
        Misplaced += 1

  print('EXACT:', Exact)
  print('MISPLACED:', Misplaced)
  
  if PlayerGuess[number] == SecretCode[number] :
    print('PERFECT GUESS!')
    
AlienTechnology()