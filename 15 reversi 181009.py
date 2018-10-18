#This is a reversi game. The player and the computer take turns to place marker so a board. Markers surrounded by 'hostile' markers change to hostile markers.

import sys
import random

########## Constants ##########
WIDTH = 8
HEIGHT = 8
########## Functions ##########
def printIntro():
  playerRole = ''
  aiRole = ''

  print("Welcome to Reversi!")
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
  first = random.choice(roles)
  if first == 'player':
    print("The player will go first.")
  else:
    print("The computer will go first.")
  return first

def firstLine():
  first = '   '
  for i in range(1, WIDTH + 1):
    number = '  ' + str(i) + ' '
    first += number

  return first

def borderLine():
  border = '   +'
  for i in range(1, WIDTH + 1):
    border += '---+'

  return border

def horizontalLine():
  horizontal = '|'
  for i in range(1, WIDTH + 1):
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
  for x in range(0, WIDTH):
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

def onBoard(x, y):
  if x > 0 and x <= WIDTH and y > 0 and y <= HEIGHT:
    return True

def emptyField(x, y):
  empty = True

  for i in range(WIDTH):
    if i == x and y in board[i]:
      empty = False
  return empty

def validLine(x, y, role, other):
  line = False
  directions = [[-1, -1], [0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0]]

  tilesToFlip = []

  for i in directions:
    xDirection, yDirection = directions[i]
    endOfBoard = False
    endOfTiles = False
    while not endOfBoard or not endOfTiles:
      xPosition = x + xDirection
      yPosition = y + yDirection
      if xPosition <= WIDTH - 1 and yPosition <= HEIGHT - 1:
        if board[x + xDirection][y + yDirection] == other:
          tilesToFlip.append([xPosition, yPosition])
          xDirection += xDirection
          yDirection += yDirection
        else:
          endOfTiles = True
      else:
        endOfBoard = True
  #dann, wenn folgendes Feld = role, dann line true

  return line

def checkValidMoves(x, y, role, other):
  '''check if a move is valid: on board, empty field, adjecent to a tile of the other player, with last tile in line of player 
  '''
  valid = False
  message = ''

  if onBoard(x, y) == True:
    if emptyField(x, y) == True:
      if validLine(x, y, role, other) == True:
        valid = True
      else:
        message = "Please choose a move that will turn a line."
    else:
      message = "Please choose an empty field."
  else:
    message = "Please enter a valid move within the borders of the game board."
  return valid, message

def setMarker(role, y, x):
  board[x][y] = role

def playerMove():
  '''takes player input, checks for valid moves, sets tile, turns tiles
  '''
  playerInput = ''
  validInput = False

  while validInput == False:
    print("Enter your move, or type quit to end the game, or hints to show hints.")
    playerInput = input()
    if playerInput == 'quit':
      sys.exit()
    elif playerInput.isdigit() and len(playerInput) == 2:
      x = int(playerInput[0]) - 1
      y = int(playerInput[1]) - 1
      move, message = checkValidMoves(x, y, playerRole, aiRole)
      if move == True:
        validInput = True
        setMarker(playerRole, y, x)
        # turnMarkers()
      else:
        print(message)
    else:
      print("Please enter a valid move: two digits for line and column.")

def aiMove():
  input("Press Enter to see the computer's move.")
  setMarker(aiRole, 2, 2)

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
  while gameRound != (WIDTH * HEIGHT - 4) and endState == False:
    printBoard()
    calculatePoints()
    if turnState == 'player':
      playerMove()
      turnState = 'ai'
    elif turnState == 'ai':
      aiMove()
      turnState = 'player'
    gameRound += 1



  # ?does the player want to play again?
  gameState = gameChoice()
