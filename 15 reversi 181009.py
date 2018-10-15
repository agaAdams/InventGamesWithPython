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
  for x in range(HEIGHT):
    board.append([])
    for y in range(WIDTH):
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

  for x in range(HEIGHT):
    for y in board[x]:
      if y == 'X':
        xPoints += 1
      elif y == 'O':
        oPoints += 1

  if playerRole == 'X':
    print("You have %s points. The computer has %s points." % (xPoints, oPoints))
  else:
    print("You have %s points. The computer has %s points." % (oPoints, xPoints))

def checkEmptyFields(x, y):
  empty = True
  for line in range(HEIGHT):
    if line == x and y in board[line]:
      empty = False
  return empty

def checkAdjecentMarkers(x, y):
  adjecent = False
  for line in range(WIDTH):
    if line == x: #gleiche zeile
      for cell in range(HEIGHT):
        if cell == y - 1 and board[line][cell] != ' ':
          adjecent = True
        elif cell == y + 1 and board[line][cell] != ' ':
          adjecent = True
    elif line == x - 1:
      for cell in range(HEIGHT):
        if cell == y  and board[line][cell] != ' ':
          adjecent = True
        elif cell == y - 1 and board[line][cell] != ' ':
          adjecent = True
        elif cell == y + 1 and board[line][cell] != ' ':
          adjecent = True
    elif line == x + 1:
      for cell in range(HEIGHT):
        if cell == y  and board[line][cell] != ' ':
          adjecent = True
        elif cell == y - 1 and board[line][cell] != ' ':
          adjecent = True
        elif cell == y + 1 and board[line][cell] != ' ':
          adjecent = True
  return adjecent

def checkTurnMarkers(x, y, role):
  turn = False

  #vertical line
  verticalItems = []
  for item in range(HEIGHT):
    verticalItems.append(board[item][y])
  firstVItem = next((item for item in verticalItems if item != ' '), - 1)
  if firstVItem > 0:
    firstVY = verticalItems.index(firstVItem)
    lastVY = max(loc for loc, val in enumerate(verticalItems) if val != ' ')
    if x < firstVY:
      if board[lastVY][y] == role:
        turn = True
    elif x > lastVY:
      if board[firstVY][y] == role:
        turn = True
  
  #firstDY
  #lastDY

  # horizontal line
  firstHItem = next((item for item in board[x] if item != ' '), - 1)
  if firstHItem > 0:
    firstHY = board[x].index(firstItem)
    lastHY = max(loc for loc, val in enumerate(board[x]) if val != ' ')
    if y < firstHY:
      if board[x][lastHY] == role:
        turn = True
    elif y > lastHY:
      if board[x][firstHY] == role:
        turn = True

  # diagonal line
  diagonalItems = []
  
  return turn

def checkPossibleMoves(x, y, role):
  possible = False
  message = ''

  if checkEmptyFields(x, y) == True:
    if checkAdjecentMarkers(x, y) == True:
      if checkTurnMarkers(x, y, role) == True:
        possible = True
      else:
        message = "Please choose a move that will turn a line."
    else:
      message = "Please place your move next to an already existing marker."
  else:
    message = "Please choose an empty field."
  return possible, message

def setMarker(role, y, x):
  board[x][y] = role

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
        move, message = checkPossibleMoves(x, y, playerRole)
        if move == True:
          validInput = True
          setMarker(playerRole, y, x)
          # turnMarkers()
        else:
          print(message)
      else:
        print("Please enter a valid move within the borders of the game board.")
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
