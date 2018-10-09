#This is a reversi game. The player and the computer take turns to place marker so a board. Markers surrounded by 'hostile' markers change to hostile markers.

import sys

########## Constants ##########

########## Functions ##########
def printIntro():
  print("Welcome to Reversi!")
  role = ''

  while role != "x" and role != "o":
    print("Do you want to be X or O?")
    role = input()

  return role

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
  ###### Globals ########
  gameRound = 1
  winState = False
  playerRole = printIntro()

  ########## Round Loop #########
  while gameRound != 64 and winState == False:
    print(gameRound)
    gameRound += 1

  # ?does the player want to play again?
  gameState = gameChoice()
