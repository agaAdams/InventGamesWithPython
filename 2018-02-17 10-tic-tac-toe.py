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
  - returns updated gameboard
  '''
  index = 0
  currentFields = fields
  currentGameBoard = board

  for character in currentGameBoard:
    if character.isdigit():
      if currentFields.get(int(character)):
        currentGameBoard = currentGameBoard[:index] + currentFields[int(character)] + currentGameBoard[index + 1:]
    index += 1

  print(currentGameBoard)
  return currentGameBoard

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
  - updates and returns dictionary of play fields
  '''
  playerRole = role
  currentFields = fields
  fieldChoice = ''

  while not fieldChoice.isdigit() or int(fieldChoice) in currentFields:
    print("What's your next move? (Numbers 1-9 only. No occupied fields!)")
    fieldChoice = input()

  currentFields[int(fieldChoice)] = playerRole
  showGameboard(currentFields, board)

  return currentFields

def aiMove(airole, fields, board):
  '''
  - tries to close own or player occupied corner or side lines
  - sets corner field
  - sets middle
  - sets side field
  - prints gameboard and returns updated dictionary of fields
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
          aiSet(number, fields, airole, board)
          return fields

  for corner in corners: #checks for free corner fields and sets
    if corner not in fields:
      aiSet(corner, fields, airole, board)
      return fields

  if 5 not in fields: #checks for free middle and sets
    aiSet(number, fields, airole, board)
    return fields

  for side in sides: #checks for free sides and sets
    if side not in fields:
      aiSet(side, fields, airole, board)

def aiSet(field, fields, role, board):
  fields[field] = role
  print("The computer chooses ", field)
  showGameboard(fields, board)

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
gameState = True

while gameState == True:
  ###### Game Globals ######
  turnState = '' #whose turn is it?
  gameRound = True #is this game round still running
  playFields = {} #empty dictionary of set fields
  gameBoard = EMPTY_GAMEBOARD #set a new and clean game board

  playerRole, aiRole = welcomeMessage()
  gameBoard = showGameboard(playFields, gameBoard)
  # print(gameBoard)

  #randomize who starts, print the info
  turnState = firstDraw()

######## Round Loop #######
  while gameRound == True:
    #check whose turn it is
    if turnState == 'player': #if player
      ## ask for move
      ## validate input
      playFields = playerMove(playerRole, playFields, gameBoard)
      turnState = 'ai'
    else:
      #if ai
      ## make move
      playFields = aiMove(aiRole, playFields, gameBoard)
      turnState = 'player'

    gameRound = checkWin(playFields, playerRole, gameBoard)
    #check for win, if win set gameround to false

  # set turnState to ''
  turnState = ''

  # ?does the player want to play again?
  gameState = gameChoice()
