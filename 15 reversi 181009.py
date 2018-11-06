#This is a reversi game. The player and the computer take turns to place markers on a board. Markers surrounded by 'hostile' markers change to hostile markers.

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

  def updateRole(self, newRole):
    '''update role of tile'''
    self.role = newRole

  def updateValidLines(self):
    '''update list of valid lines'''
    for d in Tile.DIRECTIONS:
      newLine = Line(self.x, self.y, d, self.role)
      newLine.updateTiles()
      if len(newLine.tiles) > 1:
        if newLine.tiles[0].role != self.role:
          for tile in newLine.tiles:
            if tile.role == self.role:
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
  def __init__(self, startX, startY, direction, role):
    self.startX = startX
    self.startY = startY
    self.direction = direction
    self.role = role
    self.tiles = []

  def updateTiles(self):
    '''update list of valid tiles in line'''
    self.tiles.clear()
    endOfBoard = False
    endOfTiles = False
    xDirection, yDirection = self.direction
    xPosition = self.startX + xDirection
    yPosition = self.startY + yDirection

    while not endOfBoard and not endOfTiles:
      if (xPosition <= WIDTH - 1 and xPosition >= 0) and (yPosition <= HEIGHT - 1 or yPosition >= 0):
        tile = next((t for t in newBoard.tiles if t.x == xPosition and t.y == yPosition and t.role != '.'), None)
        if tile:
          self.tiles.append(tile)
          xPosition += xDirection
          yPosition += yDirection
        else:
          endOfTiles = True
      else:
        endOfBoard = True

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
    playerPoints = 0
    aiPoints = 0

    for tile in self.tiles:
      if tile.role == playerRole:
        playerPoints += 1
      elif tile.role == aiRole:
        aiPoints += 1

    return playerPoints, aiPoints

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

def validMove(tile):
  '''
  - checks if a move is valid
  - returns error message
  '''
  valid = False
  message = ''

  if tile.onBoard() == True:
    if newBoard.emptyField(tile) == True:
      tile.updateValidLines()
      if len(tile.validLines) > 0:
        valid = True
      else:
        message = "Please choose a move that will turn a line."
    else:
      message = "Please choose an empty field."
  else:
    message = "Please enter a valid move within the borders of the game board."

  return valid, message

def flipTiles(lines, role):
  '''sets all tiles in list to set role'''
  tileList = []
  for line in lines:
    lastTile = next(t for t in reversed(line.tiles) if t.role == role)
    # tileList = (x for x in line.tiles if line.tiles.index(x) <= line.tiles.index(lastTile))
    tileList.clear()
    for tile in line.tiles:
      if line.tiles.index(tile) <= line.tiles.index(lastTile):
        tileList.append(tile)
    for tile in tileList:
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
        if len(newTile.validLines) > 0:
          possibleMoves.append(newTile)

  return possibleMoves

def showHints():
  '''shows possible moves for player as dots on game board'''
  moves = calculatePossibleMoves(playerRole)
  for move in moves:
    newTile = Tile(move.x, move.y, '.')
    newBoard.tiles.append(newTile)
  newBoard.printBoard()

def removeHints():
  '''removes dotted hint tiles form game board'''
  newBoard.tiles = [z for z in newBoard.tiles if z.role != '.']

def playerMove():
  '''takes player input, checks for valid moves, flips tiles
  '''
  playerInput = ''
  validInput = False

  while validInput == False:
    print("Enter your move, or type quit to end the game, or hints to show hints.")
    playerInput = input()
    if playerInput == 'quit':
      sys.exit()
    elif playerInput == 'hints':
      showHints()
    elif playerInput.isdigit() and len(playerInput) == 2:
      x = int(playerInput[0]) - 1
      y = int(playerInput[1]) - 1
      newTile = Tile(x, y, playerRole)
      valid, message = validMove(newTile)
      if valid:
        newBoard.tiles.append(newTile)
        flipTiles(newTile.validLines, playerRole)
        removeHints()
        validInput = True
      else:
        print(message)
    else:
      print("Please enter a valid move: two digits for line and column.")

def chooseBestMove(moves):
  '''chooses best possible move out of a list of possible moves'''
  cornerMoves = []
  nonCornerMoves = []
  cornerDirections = [[-1, -1], [1, -1], [1, 1], [-1, 1]]

  for move in moves:
    for line in move.validLines:
      if line.direction in cornerDirections:
        cornerMoves.append(move)
      else:
        nonCornerMoves.append(move)

  if len(cornerMoves) > 0:
    bestMove = max(cornerMoves, key=lambda item:item.validLines)
  else:
    bestMove = max(nonCornerMoves, key=lambda item:item.validLines)
  return bestMove

def aiMove():
  '''
  - finds possible moves
  - chooses best move: corner stone, most tiles to be flipped
  - turns tiles
  '''
  input("Press Enter to see the computer's move.")
  possibleMoves = calculatePossibleMoves(aiRole)
  bestMove = chooseBestMove(possibleMoves)
  newBoard.tiles.append(bestMove)
  flipTiles(bestMove.validLines, aiRole)

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

  playerRole, aiRole = printIntro()
  turnState = randomizeTurn()
  newBoard = Board()

  ########## Round Loop #########
  while endState == False:
    '''basic round loop'''
    newBoard.printBoard()
    playerPoints, aiPoints = newBoard.calculatePoints()
    print("You have %s points. The computer has %s points." % (playerPoints, aiPoints))

    if turnState == 'player':
      possibleMoves = calculatePossibleMoves(playerRole)
      if len(possibleMoves) > 0:
        playerMove()
        turnState = 'ai'
      else:
        endSta1t 
        print("You are out of moves.")
    elif turnState == 'ai':
      possibleMoves = calculatePossibleMoves(aiRole)
      if len(possibleMoves) > 0:
        aiMove()
        turnState = 'player'
      else:
        endState = True
        print("The computer is out of moves.")

  if playerPoints > aiPoints:
    print("Congratulations! You win.")
  else:
    print("Sorry! You lost.")
  # ?does the player want to play again?
  gameState = gameChoice()
