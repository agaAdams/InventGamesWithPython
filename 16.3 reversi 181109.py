#This is a AI played reversi game simulation with two different AI algorithms.

import sys
import random

########## Constants ##########
WIDTH = 8
HEIGHT = 8

########### Classes ###########
class Tile(object):
  """game tile"""

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
    DIRECTIONS = [[-1, -1], [0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0]]
    for d in DIRECTIONS:
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

  def isCorner(self):
    '''checks if tile is corner tile'''
    CORNERS = [[0, 0], [0, HEIGHT - 1], [WIDTH - 1, 0], [WIDTH - 1, HEIGHT - 1]]
    for corner in CORNERS:
      if self.x == corner[0] and self.y == corner[1]:
        return True

  def isSide(self):
    '''checks if tile is side tile'''
    SIDES = []
    for x in range(WIDTH):
      SIDES.append([x, 0])
      SIDES.append([x, WIDTH - 1])
    for y in range(HEIGHT):
      SIDES.append([0, y])
      SIDES.append([HEIGHT - 1, y])

    for side in SIDES:
      if self.x == side[0] and self.y == side[1]:
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
def chooseAlgorithms():
  '''asks the user to choose from two possible algorithms to compare'''
  valid = False
  algorithm1 = algorithm2 = 0

  while valid == False:
    print('''
      Please choose two algorithms to pitch against each other:
      #1: CornerBestMove
      #2: WorstMove
      #3: RandomMove
      #4: CornerSideBestMove
      #5: RankBestMove
      ''')
    playerInput = input()
    if playerInput.isdigit() and len(playerInput) == 2:
      algorithm1 = playerInput[0]
      algorithm2 = playerInput[1]
      valid = True

  return algorithm1, algorithm2

def chooseReps():
  '''asks the user to enter the number of repetitions the program is to run'''
  valid = False
  reps = 0

  while valid == False:
    print("Please enter the number of repetitions you would like the simulation to run.")
    reps = input()
    if reps.isdigit():
      valid = True

  return int(reps)

def randomizeTurn():
  '''randomizes and returns first turn'''
  roles = ['X','O']
  first = random.choice(roles)

  return first

def calculatePossibleMoves(role):
  '''calculates and returns all possible moves on game board at given time for given role'''
  possibleMoves = []

  for x in range(WIDTH):
    for y in range(HEIGHT):
      newTile = Tile(x, y, role)
      if newBoard.emptyField(newTile):
        newTile.updateValidLines()
        if newTile.validLines:
          possibleMoves.append(newTile)

  return possibleMoves

def bestTiles(moves):
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

def worstTiles(moves):
  '''finds and returns lowest ranked tiles in list of tiles'''
  minTiles = []
  minRank = WIDTH * HEIGHT
  for tile in moves:
    tile.updateRank()
    if tile.rank < minRank:
      minTiles.clear()
      minTiles.append(tile)
      minRank = tile.rank
    elif tile.rank == minRank:
      minTiles.append(tile)

  return minTiles

def cornerBestMove(moves):
  '''chooses best possible move out of a list of possible moves'''
  cornerMoves = []
  nonCornerMoves = []
  
  for tile in moves:
    if tile.isCorner():
      cornerMoves.append(tile)
    else:
      nonCornerMoves.append(tile)

  if cornerMoves:
    bestMove = random.choice(bestTiles(cornerMoves))
  else:
    bestMove = random.choice(bestTiles(nonCornerMoves))

  return bestMove

def worstMove(moves):
  '''returns worst possible move'''
  try:
    worstMove = random.choice(worstTiles(moves))
  except:
    print("Da oben ist ein Fehler!!!")

  return worstMove

def cornerSideBestMove(moves):
  '''chooses best possible move out of corner moves, side moves, other moves'''
  cornerMoves = []
  sideMoves = []
  otherMoves = []

  for tile in moves:
    if tile.isCorner():
      cornerMoves.append(tile)
    elif tile.isSide():
      sideMoves.append(tile)
    else:
      otherMoves.append(tile)

  if cornerMoves:
    bestMove = random.choice(bestTiles(cornerMoves))
  elif sideMoves:
    bestMove = random.choice(bestTiles(sideMoves))
  else:
    bestMove = random.choice(bestTiles(otherMoves))

  return bestMove

def rankBestMove(moves):
  '''returns move with highest rank'''
  bestMove = random.choice(bestTiles(moves))
  return bestMove

def flipTiles(tile, role):
  '''sets all tiles in line to set role'''
  for line in tile.validLines:
    for tile in line.tiles:
      tile.updateRole(role)

def aiMove(algorithm, role):
  '''
  - finds possible moves
  - chooses best move according to chosen algorithm
  - turns tiles
  '''
  possibleMoves = calculatePossibleMoves(role)

  if algorithm == '1':
    bestMove = cornerBestMove(possibleMoves)
  elif algorithm == '2':
    bestMove = worstMove(possibleMoves)
  elif algorithm == '3':
    bestMove = random.choice(possibleMoves)
  elif algorithm == '4':
    bestMove = cornerSideBestMove(possibleMoves)
  elif algorithm == '5':
    bestMove = rankBestMove(possibleMoves)
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
  print("Welcome to Reversi!")
  xRole = 'X'
  oRole = 'O'
  xWins = oWins = ties = xPercent = oPercent = tiePercent = 0
  algorithm1, algorithm2 = chooseAlgorithms()
  repetitions = chooseReps()

  for r in range(repetitions):
    endState = False
    turnState = randomizeTurn()
    newBoard = Board()
    xPoints = oPoints = 0
    ########## Round Loop #########
    while endState == False:
      '''basic round loop'''
      if turnState == 'X':
        if movesLeft(xRole):
          aiMove(algorithm1, xRole)
          turnState = 'O'
        else:
          endState = True
      elif turnState == 'O':
        if movesLeft(oRole):
          aiMove(algorithm2, oRole)
          turnState = 'X'
        else:
          endState = True
    xPoints, oPoints = newBoard.calculatePoints()
    # print("#%s: X scored %s points. O scored %s points." % (r, xPoints, oPoints))
    if xPoints > oPoints:
      xWins += 1
    elif xPoints < oPoints:
      oWins += 1
    else:
      ties += 1
  xPercent = round(xWins / repetitions * 100, 1)
  oPercent = round(oWins / repetitions * 100, 1)
  tiePercent = round(ties / repetitions * 100, 1)
  print("#1 wins: %s (%s%%)" % (xWins, xPercent))
  print("#2 wins: %s (%s%%)" % (oWins, oPercent))
  print("Ties: %s (%s%%)" % (ties, tiePercent))

  # ?does the player want to play again?
  gameState = gameChoice()

