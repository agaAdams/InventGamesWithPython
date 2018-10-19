#This is a reversi game. The player and the computer take turns to place marker so a board. Markers surrounded by 'hostile' markers change to hostile markers.

import sys
import random

########## Constants ##########
WIDTH = 8
HEIGHT = 8
########## Functions ##########
def makeNewBoard():
  '''creates a new board data structure, sets four set up markers'''
  for x in range(WIDTH):
    board.append([])
    for y in range(HEIGHT):
      board[x].append(' ')
  board[3][3] = 'X'
  board[4][3] = 'O'
  board[3][4] = 'O'
  board[4][4] = 'X'

def printIntro():
  '''prints welcome message, sets and returns player's and computer's role'''
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
  '''randomizes and returns first turn'''
  roles = ['player','ai']
  first = random.choice(roles)
  if first == 'player':
    print("The player will go first.")
  else:
    print("The computer will go first.")
  return first

def firstLine():
  '''creates and returns first line of game board'''
  first = '   '
  for i in range(1, WIDTH + 1):
    number = '  ' + str(i) + ' '
    first += number

  return first

def borderLine():
  '''creates and returns border line of game board fields'''
  border = '   +'
  for i in range(1, WIDTH + 1):
    border += '---+'

  return border

def horizontalLine():
  '''creates and returns horizontal seperator line of game board fields'''
  horizontal = '|'
  for i in range(1, WIDTH + 1):
    horizontal += '   |'

  return horizontal

def printBoard():
  '''prints game board'''
  print(firstLine())
  for line in range(0, HEIGHT):
    print(borderLine())
    print('   ' + horizontalLine())
    print(' ' + str(line + 1) + ' |', end='')
    for x in range(0, WIDTH - 1):
      print(' ' + board[x][line] + ' |', end='')
    print()
    print('   ' + horizontalLine())
  print(borderLine())

def calculatePoints():
  '''calculates and prints player's and computer's points'''
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
  '''checks if tile within game board borders'''
  if x > 0 and x <= (WIDTH - 1) and y > 0 and y <= (HEIGHT - 1):
    return True

def emptyField(x, y):
  '''checks if field empty'''
  if board[x][y] == ' ':
    return True

def checkLines(x, y, role, other):
  '''
  - checks field for valid lines in all directions
  - returns check and list of tiles to flip in all directions
  '''
  line = False
  directions = [[-1, -1], [0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0]]
  flippedTiles = []

  for i in directions:
    if line == False:
      line, tiles = validLine(i, x, y, role, other)
    else:
      _, tiles = validLine(i, x, y, role, other)
    for tile in tiles:
      flippedTiles.append(tile)

  return line, flippedTiles

def validLine(direction, x, y, role, other):
  '''
  - checks valid line in given direction
  - returns check and tiles to flip in one direction
  '''
  valid = False
  tilesToFlip = []
  endOfBoard = False
  endOfTiles = False
  xDirection, yDirection = direction

  while not endOfBoard and not endOfTiles:
    xPosition = x + xDirection
    yPosition = y + yDirection
    if xPosition <= WIDTH - 1 and yPosition <= HEIGHT - 1:
      if board[xPosition][yPosition] == other:
        tilesToFlip.append([xPosition, yPosition])
        xDirection += xDirection
        yDirection += yDirection
      elif board[xPosition][yPosition] == role and len(tilesToFlip) > 0:
        endOfTiles = True
        valid = True
      else:
        endOfTiles = True
        del tilesToFlip[:]
    else:
      endOfBoard = True
      del tilesToFlip[:]

  return valid, tilesToFlip

def checkValidMoves(x, y, role, other):
  '''
  - check if a move is valid
  - return check, error message and list of tiles to flip
  '''
  valid = False
  message = ''
  tiles = []

  if onBoard(x, y) == True:
    if emptyField(x, y) == True:
      valid, tiles = checkLines(x, y, role, other)
      if valid == True:
        return valid, message, tiles
      else:
        message = "Please choose a move that will turn a line."
    else:
      message = "Please choose an empty field."
  else:
    message = "Please enter a valid move within the borders of the game board."

  return valid, message, tiles

def flipTiles(role, tiles):
  '''set all tiles in list to set role'''
  for tile in tiles:
    board[tile[0]][tile[1]] = role

def playerMove():
  '''takes player input, checks for valid moves, turns tiles
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
      move, message, tiles = checkValidMoves(x, y, playerRole, aiRole)
      if move == True:
        validInput = True
        tiles.append([x, y])
        flipTiles(playerRole, tiles)
      else:
        print(message)
    else:
      print("Please enter a valid move: two digits for line and column.")

def aiMove():
  '''
  - calculates possible moves
  - chooses best move: corner stone, most tiles to be flipped
  - turns tiles
  '''
  input("Press Enter to see the computer's move.")
  flipTiles(aiRole, [[2, 2]])
  # setMarker(aiRole, 2, 2)

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
