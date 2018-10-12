#This is a reversi game. The player and the computer take turns to place marker so a board. Markers surrounded by 'hostile' markers change to hostile markers.

import sys
import random

########## Constants ##########
WIDTH = 8
HEIGHT = 8
########## Functions ##########
def printIntro():
  print("Welcome to Reversi!")
  playerRole = ''
  aiRole = ''

  while playerRole != "x" and playerRole != "o":
    print("Do you want to be X or O?")
    playerRole = input()

  playerRole = playerRole.upper()

  if playerRole == 'X':
    aiRole = 'O'
  else:
    aiRole = 'X'
  return playerRole, aiRole

def randomizeTurn():
  roles = ['player','ai']
  playerRole = random.choice(roles)
  if playerRole == 'player':
    print("The player will go first.")
  else:
    print("The computer will go first.")
  return playerRole

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

def makeNewBoard():
  for x in range(WIDTH):
    board.append([])
    for y in range(HEIGHT):
      board[x].append(' ')
  board[3][3] = 'X'
  board[4][3] = 'O'
  board[3][4] = 'O'
  board[4][4] = 'X'

def printBoard():
  print(firstLine())
  for x in range(0, HEIGHT):
    print(borderLine())
    print('   ' + horizontalLine())
    print(' ' + str(x + 1) + ' |', end='')
    for y in board[x]:
      print(' ' + y + ' |', end='')
    print()
    print('   ' + horizontalLine())
  print(borderLine())

def calculatePoints():
  xPoints = 0
  oPoints = 0

  for x in range(WIDTH):
    for y in board[x]:
      if y == 'X':
        xPoints += 1
      elif y == 'O':
        oPoints += 1

  if playerRole == 'X':
    print("You have %s points. The computer has %s points." % (xPoints, oPoints))
  else:
    print("You have %s points. The computer has %s points." % (oPoints, xPoints))

def playerMove():
  playerInput = ''
  validInput = False

  while validInput == False:
    print("Enter your move, or type quit to end the game, or hints to show hints.")
    playerInput = input()
    if playerInput == 'quit':
      sys.exit()
    elif playerInput.isdigit() and len(playerInput) == 2:
      if int(playerInput[0]) > 0 and int(playerInput[0]) <= WIDTH and int(playerInput[1]) > 0 and int(playerInput[1]) <= HEIGHT:
        y = int(playerInput[0]) - 1
        x = int(playerInput[1]) - 1
        if checkFields(x, y) == False:
          validInput = True
          setMarker(playerRole, y, x)
        else:
          print("This field is already taken.")

def setMarker(role, y, x):
  board[x][y] = role

def checkFields(x, y):
  for line in range(WIDTH):
    if line == x and y in board[line]:
      return True
  return False

def aiMove():
  input("Press Enter to see the computer's move.")
  setMarker(aiRole, 2, 2)

def checkPossibleMoves():
  pass
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
  endState = False
  board = []
  makeNewBoard()
  playerRole, aiRole = printIntro()
  turnState = randomizeTurn()

  ########## Round Loop #########
  while gameRound != (WIDTH * HEIGHT) and endState == False:
    printBoard()
    calculatePoints()
    if turnState == 'player':
      playerMove()
      turnState = 'ai'
    elif turnState == 'ai':
      aiMove()
      turnState = 'player'
    gameRound += 1
    endState = checkPossibleMoves()

  # ?does the player want to play again?
  gameState = gameChoice()
