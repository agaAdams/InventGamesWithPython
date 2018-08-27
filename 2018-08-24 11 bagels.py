#This is a game template for python games

#game description
import

########## Constants ##########

########## Functions ##########
def randomNumber():
  '''
  - make a random number of three digits
  - no repeating digits
  - return number
  '''

def printIntro():
  '''
  - print Intro Text
  '''

def playerGuess():
  '''
  - ask player to guess
  - validate player input
  - only digits 0-9
  - no repeating
  '''

def checkWin(randomNumber, guess):
  '''
  - returns False, if guess is the same as the randomNumber
  '''

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

  global gameState
  gameChoice = ''

  while gameChoice != 'y' and gameChoice != 'n':
      print("Do you want to play again? (y/n)")
      gameChoice = input()

  if gameChoice == 'n':
      gameState = False


########## Game Loop ##########
gameState = True
# remains true for as long, as the player wants to keep playing

while gameState == True:
    ###### Globals ########
    gameRound = True
    # remains true for as long as the game is neither lost or won

########## Round Loop #########
  while gameRound == True:
    # remains true for every round of the game
    for x in xrange(1,10):
      randomNumber = randomNumber()
      printIntro()
      guess = playerGuess()
      gameRound = checkWin(randomNumber, guess)

      if gameRound:
        checkClues(randomNumber, guess)
      else:
        break

    gameRound = False

  # ?does the player want to play again?
  gameChoice()
