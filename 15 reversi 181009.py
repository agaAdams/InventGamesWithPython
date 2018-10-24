#This is a reversi game. The player and the computer take turns to place marker so a board. Markers surrounded by 'hostile' markers change to hostile markers.

import sys
import random

########## Constants ##########
WIDTH = 8
HEIGHT = 8
DIRECTIONS = [[-1, -1], [0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0]]

########### Classes ###########
class Tile(object):
  """game tile"""
  def __init__(self, x, y, role):
    self.x = x
    self.y = y
    self.role = role
    self.validLines = []

  def updateRole(self, newRole):
    '''update role of tile'''
    self.role = newRole

  def updateValidLines(self):
    '''update list of valid lines'''
    for d in DIRECTIONS:
      newLine = Line(self.x, self.y, d)
      self.validLines.append(newLine)

  def onBoard(self):
    '''checks if tile within game board borders'''
    if self.x >= 0 and self.x < (WIDTH) and self.y >= 0 and self.y < (HEIGHT):
      return True

  def __eq__(self, other):
    ''' equality comparison: compares x and y coordinates '''
    return self.x == other.x and self.y == other.y

class Line(object):
  """line of tiles"""
  def __init__(self, startX, startY, direction):
    self.startX = startX
    self.startY = startY
    self.direction = direction
    self.tiles = []

  def updateTiles(self):
    '''update list of tiles in line'''
    self.tiles.clear()
    endOfBoard = False
    xDirection, yDirection = self.direction

    while not endOfBoard:
      xPosition = self.x + xDirection
      yPosition = self.y + yDirection
      if (xPosition <= WIDTH - 1 and xPosition >= 0) and (yPosition <= HEIGHT - 1 or yPosition >= 0):
        if next((t for t in newBoard.tiles if t.x == xPosition and t.y == yPosition), None):
          self.tiles.append([xPosition, yPosition])
          xDirection += xDirection
          yDirection += yDirection
      else:
        endOfBoard = True

class Board(object):
  """game board"""
  def __init__(self):
    self.tiles = [] #all tiles on board
    self.makeNewBoard()
  
  def makeNewBoard(self):
    '''creates four start tiles'''
    newTile1 = Tile(3, 3, 'X')
    self.tiles.append(newTile1)
    newTile2 = Tile(4, 3, 'O')
    self.tiles.append(newTile2)
    newTile3 = Tile(3, 4, 'O')
    self.tiles.append(newTile3)
    newTile4 = Tile(4, 4, 'X')
    self.tiles.append(newTile4)

  def emptyField(self, tile):
    '''checks if field empty'''
    if tile not in self.tiles:
      return True

  def firstLine(self):
    '''creates and returns first line of game board'''
    first = '   '
    for i in range(WIDTH):
      number = '  ' + str(i + 1) + ' '
      first += number

    return first

  def borderLine(self):
    '''creates and returns border line of game board fields'''
    border = '   +'
    for i in range(1, WIDTH + 1):
      border += '---+'

    return border

  def horizontalLine(self):
    '''creates and returns horizontal seperator line of game board fields'''
    horizontal = '|'
    for i in range(1, WIDTH + 1):
      horizontal += '   |'

    return horizontal

  def printBoard(self):
    '''prints game board'''
    print(self.firstLine())
    for line in range(HEIGHT):
      print(self.borderLine())
      print('   ' + self.horizontalLine())
      print(' ' + str(line + 1) + ' |', end='')
      for x in range(0, WIDTH):
        tile = next((tile for tile in self.tiles if tile.x == x and tile.y == line), None)
        if tile:
          field = tile.role
        else:
          field = ' '
        print(' ' + field + ' |', end='')
      print()
      print('   ' + self.horizontalLine())
    print(self.borderLine())

  def calculatePoints(self):
    '''calculates and prints player's and computer's points'''
    playerPoints = 0
    aiPoints = 0

    for tile in self.tiles:
      if tile.role == playerRole:
        playerPoints += 1
      elif tile.role == aiRole:
        aiPoints += 1

    print("You have %s points. The computer has %s points." % (playerPoints, aiPoints))

########## Functions ##########
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

def checkLines(x, y, role, other):
  '''
  - checks field for valid lines in all directions
  - returns check and list of tiles to flip in all directions
  '''
  line = False
  flippedTiles = []

  for i in DIRECTIONS:
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

def checkValidMoves(tile):
  '''
  - check if a move is valid
  - return check, error message and list of tiles to flip
  '''
  valid = False
  message = ''
  # tiles = []

  if tile.onBoard() == True:
    if newBoard.emptyField(tile) == True:
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
      newTile = Tile(x, y, playerRole)
      move, message, tiles = checkValidMoves(newTile)
      if move == True:
        validInput = True
  #      tiles.append([x, y])
   #     flipTiles(playerRole, tiles)
      else:
        print(message)
    else:
      print("Please enter a valid move: two digits for line and column.")

def calculatePossibleMoves():
  '''
  - calculates all possible moves on game board at given time
  - returns list of possible moves
  '''
  possibleMoves = []
  possibleCornerMoves = []
  possibleNonCornerMoves = []
  cornerDirections = [[-1, -1], [1, -1], [1, 1], [-1, 1]]

  for idx, x in enumerate(board):
    for idy, y in enumerate(x):
      if emptyField(idx, idy):
        for i in DIRECTIONS:
          valid, tiles = validLine(i, idx, idy, aiRole, playerRole)
          if valid:
            xDirection, yDirection = i
            newLine = Line(idx, idy, xDirection, yDirection, tiles)
            if i in cornerDirections:
              possibleCornerMoves.append(newLine)
            else:
              possibleNonCornerMoves.append(newLine)
  possibleMoves.append(possibleCornerMoves)
  possibleMoves.append(possibleNonCornerMoves)

  return possibleMoves

def chooseBestMove(moves):
  cornerMoves, nonCornerMoves = moves  

  if len(cornerMoves) > 0:
    bestMove = max(cornerMoves, key=lambda item:item.tiles)
  else:
    bestMove = max(nonCornerMoves, key=lambda item:item.tiles)
  return bestMove

def aiMove():
  '''
  - calculates possible moves
  - chooses best move: corner stone, most tiles to be flipped
  - turns tiles
  '''
  input("Press Enter to see the computer's move.")
  possibleMoves = calculatePossibleMoves()
  bestMove = chooseBestMove(possibleMoves)
  _, tilesToFlip = checkLines(bestMove.x, bestMove.y, aiRole, playerRole)
  tilesToFlip.append([bestMove.x, bestMove.y])
  flipTiles(aiRole, tilesToFlip)

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

  playerRole, aiRole = printIntro()
  turnState = randomizeTurn()
  newBoard = Board()

  ########## Round Loop #########
  while gameRound != (WIDTH * HEIGHT - 4) and endState == False:
    newBoard.printBoard()
    newBoard.calculatePoints()
    if turnState == 'player':
      playerMove()
      turnState = 'ai'
    elif turnState == 'ai':
      aiMove()
      turnState = 'player'
    gameRound += 1

  # ?does the player want to play again?
  gameState = gameChoice()
