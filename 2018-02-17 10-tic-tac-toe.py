#[Anforderungen](x-devonthink-item://3C3FBF5A-48CA-4101-9DF9-9E3AE0861861)
#[Flowchart](x-devonthink-item://1D34B7AF-D45F-4D6A-A6AF-896BBC5FF640)
#
#This is a tic-tc-toe game, player vs computer.
import random

########## Constants ##########
EMPTY_GAMEBOARD = '''
7|8|9
-+-+-
4|5|6
-+-+-
1|2|3
'''

########## Functions ##########
def welcomeMessage():
  '''
  - prints welcome message on screen
  - asks player for X or O
  - validates player input
  - returns player and ai roles
  '''
  playerChoice = ''

  print("Welcome to Tic-Tac-Toe!")

  while playerChoice != 'x' and playerChoice != 'o':
    print("Do you want to be X or O?")
    playerChoice = input()

  if playerChoice == 'x':
    ai = 'o'
  else:
    ai = 'x'

  print("You are ", playerChoice.upper())

  return playerChoice, ai

def showGameboard(fields, board):
  '''
  - update gameboard
  - print updated gameboard
  - return updated gameboard
  '''
  index = 0

  for character in board:
    if character.isdigit():
      if fields.get(int(character)):
        board = board[:index] + fields[int(character)] + board[index + 1:]
    index += 1

  print(board)
  return board

def firstDraw():
  '''
  - determines who starts the game first
  - returns role with first turn
  '''

  first = random.randint(0, 1)

  if first == 0:
    print("You will go first.")
    firstTurn = 'player'
  else:
    print("The computer will go first.")
    firstTurn = 'ai'

  return firstTurn

def playerMove(role, fields, board):
  '''
  - validates player input (only numbers 1-9)
  - validates player input (only free fields)
  - updates and returns dictionary of play fields and gameboard
  '''
  fieldChoice = ''

  while not fieldChoice.isdigit() or int(fieldChoice) in fields:
    print("What's your next move? (Numbers 1-9 only. No occupied fields!)")
    fieldChoice = input()

  fields[int(fieldChoice)] = role
  board = showGameboard(fields, board)

  return fields, board

def aiMove(airole, fields, board):
  '''
  - tries to close own or player occupied corner or side lines
  - sets corner field
  - sets middle
  - sets side field
  - prints gameboard and returns updated dictionary of fields and game board
  '''
  corners = [1,3,7,9]
  sides = [2,4,6,8]
  winSets = { 1: [1,2,3], 2: [2,5,8], 3: [3,6,9], 4: [4,5,6], 5: [7,8,9], 6: [1,4,7], 7: [3,5,7], 8: [1,5,9] }

  for set in winSets: #checks for open lines and closes them
    x = 0
    o = 0
    for number in winSets[set]:
      if number in fields:
        if fields[number] == 'x':
          x += 1
        if fields[number] == 'o':
          o += 1
    if x > 1 or o > 1:
      for number in winSets[set]:
        if number not in fields:
          board = aiSet(number, fields, airole, board)
          return fields, board

  for corner in corners: #checks for free corner fields and sets
    if corner not in fields:
      board = aiSet(corner, fields, airole, board)
      return fields, board

  if 5 not in fields: #checks for free middle and sets
    board = aiSet(number, fields, airole, board)
    return fields, board

  for side in sides: #checks for free sides and sets
    if side not in fields:
      board = aiSet(side, fields, airole, board)
      return fields, board

def aiSet(field, fields, role, board):
  '''
  - sets chosen field as play field for the ai
  - prints choice
  - shows game board
  - returns updated game board
  '''
  fields[field] = role
  print("The computer chooses ", field)
  board = showGameboard(fields, board)
  return board

def checkWin(fields, role, board):
  '''
  - check if win conditions are met
  - ends game round in such case
  '''

  currentFields = fields
  gRound = True
  emptyField = 0

  for f in currentFields:
    if currentFields.get(f) == currentFields.get(f + 3) and currentFields.get(f) == currentFields.get(f + 6):
      gRound = False
    elif currentFields.get(f) == currentFields.get(f + 4) and currentFields.get(f) == currentFields.get(f + 8):
      gRound = False
    elif f == 3:
      if currentFields.get(f) == currentFields.get(f + 2) and currentFields.get(f) == currentFields.get(f + 4):
        gRound = False
    elif f == 1 or f == 4 or f == 7:
      if currentFields.get(f) == currentFields.get(f + 1) and currentFields.get(f) == currentFields.get(f + 2):
        gRound = False

  if gRound == False:
      if currentFields[f] == role:
        print("You have won!")
      else:
        print("The computer has won.")
  else:
    for character in board:
      if character.isdigit():
        emptyField += 1
    if emptyField == 0:
      print("There are no more moves left. You have a tie.")
      gRound = False

  return gRound

def gameChoice():
  '''
  - asks the player, whether he wants to play again and validates the input
  - accepts only "y" or "n"
  - sets the gameState accordingly
  '''

  gameChoice = ''
  state = True

  while gameChoice != 'y' and gameChoice != 'n':
      print("Do you want to play again? (y/n)")
      gameChoice = input()

  if gameChoice == 'n':
      state = False
  return state

########## Game Loop ##########
gameState = True #true as long as the player wants to have another go

while gameState == True:
  ###### Game Globals ######
  turnState = '' #whose turn is it?
  gameRound = True #is this game round still running
  playFields = {} #empty dictionary of set fields
  gameBoard = EMPTY_GAMEBOARD #set a new and clean game board

  playerRole, aiRole = welcomeMessage()
  showGameboard(playFields, gameBoard)

  #randomize who starts, print the info
  turnState = firstDraw()

######## Round Loop #######
  while gameRound == True:
    #check whose turn it is
    if turnState == 'player': #if player
      ## ask player for move
      playFields, gameBoard = playerMove(playerRole, playFields, gameBoard)
      turnState = 'ai'
    else:
      ## make ai move
      playFields, gameBoard = aiMove(aiRole, playFields, gameBoard)
      turnState = 'player'

    gameRound = checkWin(playFields, playerRole, gameBoard)
    #check for win, if win set gameround to false

  # ?does the player want to play again?
  gameState = gameChoice()
