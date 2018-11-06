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
  print("Do you want to play again? (y/n)")
  if input() == 'y':
    return True
  else:
    sys.exit()

########## Game Loop ##########
gameState = True
# remains true for as long, as the player wants to keep playing

while gameState == True:
  '''basic game loop'''
  ###### Globals ########
  gameRound = 1
  endState = False
  printIntro()

  ########## Round Loop #########
  while endState == False:
    '''basic round loop'''

  # ?does the player want to play again?
  gameState = gameChoice()
