#The Bagels Deduction Game, Chpt#11
import random

########## Constants ##########

########## Functions ##########
def getRandomNumber():
  '''
  - make a random number of three digits
  - no repeating digits
  - return number
  '''
  random3Digits = []
  
  while len(random3Digits) != 3:
    digit = str(random.randint(0,9))
    if digit not in random3Digits:
      random3Digits.append(str(digit))

  return random3Digits

def printIntro():
  '''
  - print Intro Text
  '''
  print('''
    I am thinking of a 3-digit number. Try to guess what it is.
    The clues given are...
    When I say:  That means:
      Bagels      None of the digits is correct.
      Pico        One digit is correct but in the wrong position.
      Fermi       One digit is correct and in the right position.
    I have thought up a number. You have 10 guesses to get it.
    ''')

def playerGuess(round):
  '''
  - ask player to guess
  - validates player input
    - only digits 0-9
    - only 3 digits long
    - no repeating digits
  - returns guessed number
  '''
  guessedNumber = []
  playerInput = ''

  while not playerInput.isdigit() or len(playerInput) != 3:
    print("Guess #", round)
    playerInput = input()
    digitList = list(playerInput)

    for digit in digitList:
      if digitList.count(digit) > 1:
        playerInput = ''

  guessedNumber = digitList

  return guessedNumber

def checkWin(randomNumber, guess):
  '''
  - compare computers random number and players guess
  - returns False, if guess is the same as the randomNumber
  '''
  return randomNumber != guess

def checkClues(randomNumber, guess):
  '''
  - check guess for clues
  - print clues
  '''
  clues = []
  cluesLine = ''

  if len(checkBagels(randomNumber, guess)) == 0:
    cluesLine = 'Bagels'
  else:
    for number in guess:
      if number == randomNumber[guess.index(number)]:
        clues.append('Fermi ')
      elif number in randomNumber:
        clues.append('Pico ')
    clues.sort()
    for item in clues:
      cluesLine = cluesLine + item

  return cluesLine

def checkBagels(randomNumber, guess):
  '''
  - checks if any digits in the guessed number are in the random number
  - returns list of correct guessed numbers
  '''
  bagels = []

  for number in guess:
    if number in randomNumber:
      bagels.append(number)

  return bagels

def gameChoice():
  '''
  - asks the player, whether he wants to play again and validates the input
  - accepts only "y" or "n"
  - sets the gameState accordingly
  '''
  gameChoice = ''

  while gameChoice != 'y' and gameChoice != 'n':
      print("Do you want to play again? (y/n)")
      gameChoice = input()

  if gameChoice == 'y':
      return True

  return False

########## Game Loop ##########
gameState = True
# remains true for as long, as the player wants to keep playing

while gameState == True:
  ###### Globals ########
  gameRound = 1
  winState = False
  randomNumber = getRandomNumber()
  printIntro()

  ########## Round Loop #########
  while gameRound != 11 and winState == False:
    gameRound += 1
    guess = playerGuess(gameRound)

    if randomNumber != guess:
      print(checkClues(randomNumber, guess))
    else:
      winState = True

  if gameRound == 11:
    print("Sorry, you guessed ten times. The secret number was ", randomNumber)
  else:
    print("You got it!")

  # ?does the player want to play again?
  gameState = gameChoice()
