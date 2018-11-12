#This is a AI played reversi game. The computer takes turns to place markers on a board. Markers surrounded by 'hostile' markers change to hostile markers.

import sys
import random

########## Constants ##########
WIDTH = 8
HEIGHT = 8

########### Classes ###########
class Tile(object):
  """game tile"""
  DIRECTIONS = [[-1, -1], [0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0]]

  def __init__(self, x, y, role):
    self.x = x
    self.y = y
    self.role = role
    self.validLines = []
    self.rank = 0

  def updateRole(self, newRole):
    '''update role of tile'''
    self.role = newRole

  def updateValidLines(self):
    '''update list of valid lines'''
    for d in Tile.DIRECTIONS:
      newLine = Line(self.x, self.y, d, self.role)
      newLine.updateTiles()
      if newLine.tiles:
        if newLine.tiles[0].role != self.role:
          self.validLines.append(newLine)

  def updateRank(self):
    '''updates rank of tile'''
    self.rank = 0
    self.updateValidLines()
    for line in self.validLines:
      self.rank += len(line.tiles)

  def onBoard(self):
    '''checks if tile within game board borders'''
    if self.x >= 0 and self.x < (WIDTH) and self.y >= 0 and self.y < (HEIGHT):
      return True

  def __eq__(self, other):
    ''' equality comparison: compares x and y coordinates '''
    return self.x == other.x and self.y == other.y

  def __gt__(self, other):
    return self.rank > other.rank

  def __lt__(self, other):
    return self.rank < other.rank
    
class Line(object):
  """line of tiles"""
  def __init__(self, startX, startY, direction, role):
    self.startX = startX
    self.startY = startY
    self.direction = direction
    self.role = role
    self.tiles = []

  def updateTiles(self):
    '''update list of valid tiles in line'''
    self.tiles.clear()
    tilesInLine = []
    endOfBoard = False
    endOfTiles = False
    xDirection, yDirection = self.direction
    xPosition = self.startX + xDirection
    yPosition = self.startY + yDirection

    while not endOfBoard and not endOfTiles:
    # find all tiles in line
      if (xPosition <= WIDTH - 1 and xPosition >= 0) and (yPosition <= HEIGHT - 1 or yPosition >= 0):
        tile = next((t for t in newBoard.tiles if t.x == xPosition and t.y == yPosition and t.role != '.'), None)
        if tile:
          tilesInLine.append(tile)
          xPosition += xDirection
          yPosition += yDirection
        else:
          endOfTiles = True
      else:
        endOfBoard = True

    closingTile = next((t for t in tilesInLine if t.role == self.role), None)
    # find tile of own role closing the line'''

    if closingTile:
      # add all valid tiles up to closing tile to list of valid tiles
      for tile in tilesInLine:
        if tilesInLine.index(tile) <= tilesInLine.index(closingTile):
          self.tiles.append(tile)

  def __eq__(self, other):
    ''' equality comparison: compares starting coordinates and direction'''
    return self.startX == other.startX and self.startY == other.startY and self.direction == other.direction

  def __gt__(self, other):
    ''' > comparison: compares length of list of valid tiles '''
    return len(self.tiles) > len(other.tiles)

  def __lt__(self, other):
    ''' < comparison: compares length of list of valid tiles '''
    return len(self.tiles) < len(other.tiles)

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
    empty = False
    boardTile = next((t for t in self.tiles if t == tile), None)
    if tile not in self.tiles:
      empty = True
    else:
      if boardTile.role == '.':
        empty = True

    return empty

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
    xPoints = 0
    oPoints = 0

    for tile in self.tiles:
      if tile.role == xRole:
        xPoints += 1
      elif tile.role == oRole:
        oPoints += 1

    return xPoints, oPoints

########## Functions ##########
def randomizeTurn():
  '''randomizes and returns first turn'''
  roles = ['X','O']
  first = random.choice(roles)
  if first == 'X':
    print("X will go first.")
  else:
    print("O will go first.")
  return first

def flipTiles(tile, role):
  '''sets all tiles in line to set role'''
  for line in tile.validLines:
    for tile in line.tiles:
      tile.updateRole(role)

def calculatePossibleMoves(role):
  '''
  - calculates and returns all possible moves on game board at given time for given role
  '''
  possibleMoves = []

  for x in range(WIDTH):
    for y in range(HEIGHT):
      newTile = Tile(x, y, role)
      if newBoard.emptyField(newTile):
        newTile.updateValidLines()
        if newTile.validLines:
          possibleMoves.append(newTile)

  return possibleMoves

def topTiles(moves):
  '''finds and returns highest ranked tiles in list of tiles'''
  maxTiles = []
  maxRank = 0
  for tile in moves:
    tile.updateRank()
    if tile.rank > maxRank:
      maxTiles.clear()
      maxTiles.append(tile)
      maxRank = tile.rank
    elif tile.rank == maxRank:
      maxTiles.append(tile)

  return maxTiles

def chooseBestMove(moves):
  '''chooses best possible move out of a list of possible moves'''
  cornerMoves = []
  nonCornerMoves = []
  cornerTiles = []
  newTile1 = Tile(0, 0, 'X')
  cornerTiles.append(newTile1)
  newTile2 = Tile(0, HEIGHT - 1, 'X')
  cornerTiles.append(newTile2)
  newTile3 = Tile(WIDTH - 1, 0, 'X')
  cornerTiles.append(newTile3)
  newTile4 = Tile(WIDTH - 1, HEIGHT - 1 , 'X')
  cornerTiles.append(newTile4)

  for tile in moves:
    if tile in cornerTiles:
      cornerMoves.append(tile)
    else:
      nonCornerMoves.append(tile)

  if cornerMoves:
    bestMove = random.choice(topTiles(cornerMoves))
  else:
    bestMove = random.choice(topTiles(nonCornerMoves))

  return bestMove

def aiMove(role):
  '''
  - finds possible moves
  - chooses best move: corner stone, most tiles to be flipped
  - turns tiles
  '''
  possibleMoves = calculatePossibleMoves(role)
  bestMove = chooseBestMove(possibleMoves)
  newBoard.tiles.append(bestMove)
  flipTiles(bestMove, role)

def movesLeft(role):
  '''check for moves left for given role'''
  possibleMoves = calculatePossibleMoves(role)
  return possibleMoves

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
  endState = False

  print("Welcome to Reversi!")
  xRole = 'X'
  oRole = 'O'
  turnState = randomizeTurn()
  newBoard = Board()

  ########## Round Loop #########
  while endState == False:
    '''basic round loop'''
    xPoints, oPoints = newBoard.calculatePoints()

    if turnState == 'X':
      if movesLeft(xRole):
        aiMove(xRole)
        turnState = 'O'
      else:
        endState = True
    elif turnState == 'O':
      if movesLeft(oRole):
        aiMove(oRole)
        turnState = 'X'
      else:
        endState = True

  newBoard.printBoard()
  print("X scored %s points. O scored %s points." % (xPoints, oPoints))

  if xPoints > oPoints:
    print("X wins.")
  else:
    print("O wins.")
  # ?does the player want to play again?
  gameState = gameChoice()

