#This is a game template for python games

#game description
import

########## Constants ##########

########## Functions ##########
def gameChoice():
  '''
  - asks player, whether he wants to play again and validates the input
  - accepts only "y" or "n"
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
  printIntro()

  ########## Round Loop #########
  while gameRound != 11 and winState == False:

  # ?does the player want to play again?
  gameState = gameChoice()
