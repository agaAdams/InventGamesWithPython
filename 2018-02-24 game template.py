#This is a game template for python games

#game description
import

########## Constants ##########

########## Functions ##########
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

  # ?does the player want to play again?
  gameChoice()
