#This is a game template for python games

#game description
import random

########## Constants ##########

########## Functions ##########
def randomNumber():
  '''
  - make a random number of three digits
  - no repeating digits
  - return number
  '''
  random3Digits = []
  
  while len(random3Digits) != 3:
    digit = random.randint(0,9)
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
  - validate player input
  - only digits 0-9
  - only 3 digits long
  - no repeating digits
  - return guessed number
  '''
  guessedNumber = []

  playerInput = ''

  while not playerInput.isdigit() or len(playerInput) != 3:
    print("Guess #", round)
    print("Please enter a 3-digit number. No repeating digits.")
    playerInput = input()
    for x in range(len(playerInput)):
      # digitList = list(playerInput)
      if list(playerInput).count(list(playerInput)[x]) > 1:
        playerInput = ''
        break

  guessedNumber = list(playerInput)
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
  x = 1
  randomNumber = randomNumber()
  print(randomNumber)
  printIntro()

  ########## Round Loop #########
  for x in range(1,11):
    guess = playerGuess(x)

    if randomNumber != guess:
      checkClues(randomNumber, guess)
    else:
      break

  if x == 11:
    print("Sorry, you guessed ten times. The secret number was ", randomNumber)
  else:
    print("You got it!")

  # ?does the player want to play again?
  gameState = gameChoice()
