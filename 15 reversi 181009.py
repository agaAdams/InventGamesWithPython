#This is a reversi game. The player and the computer take turns to place marker so a board. Markers surrounded by 'hostile' markers change to hostile markers.

import sys

########## Constants ##########
WIDTH = 8
HEIGHT = 8
########## Functions ##########
def printIntro():
  print("Welcome to Reversi!")
  role = ''

  while role != "x" and role != "o":
    print("Do you want to be X or O?")
    role = input()

  return role

def firstLine():
  first = '   '
  for x in range(1, WIDTH + 1):
    number = '  ' + str(x) + ' '
    first += number

  return first

def borderLine():
  border = '   +'
  for x in range(1, WIDTH + 1):
    border += '---+'

  return border

def horizontalLine():
  horizontal = '|'
  for x in range(1, WIDTH + 1):
    horizontal += '   |'

  return horizontal

# def numberLine():
#   for x in range(1, HEIGHT + 1):
#     number = ' ' + str(x) + ' '

def printBoard():
  print(firstLine())
  for x in range(1, HEIGHT + 1):
    print(borderLine())
    print('   ' + horizontalLine())
    print(' ' + str(x) + ' ' + horizontalLine())
    print('   ' + horizontalLine())
  print(borderLine())

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
  while gameRound != (WIDTH * HEIGHT) and winState == False:
    print(gameRound)
    printBoard()
    gameRound += 1

  # ?does the player want to play again?
  gameState = gameChoice()
