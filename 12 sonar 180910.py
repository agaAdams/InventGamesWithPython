#This is a sonar game. The player places sonar devices at various places in the ocean to locate sunken treasure chests.
import random
import re

########## Constants ##########
SONARS = 16 #number of sonars the player has to find chests
CHESTS = 3 #number of placed chests
BOARD_WIDTH = 60
BOARD_HEIGHT = 16

########### Classes ###########
class Chest(object):
  """
  - chest class, represents treasure chest with x and y coordinates
  - takes board width and height as arguments
  """
  def __init__(self, width, height):
    self.x = random.randint(0, width - 1)
    self.y = random.randint(0, height - 1)
  def __eq__(self, other):
    ''' equality comparison: compares x and y coordinates '''
    return self.x == other.x and self.y == other.y

class Board(object):
  """
  - board class, represents game board
  - calculates game board as list of lists
  - places sonar distances or random ocean characters
  """
  def __init__(self):
    self.board = []

  def calculateBoard(self, width, height, chestList, sonarList):
    sonarVisible = False
    felder = ['~', '`']

    for y_coordinate in range(height): #lines
      line = []
      if y_coordinate < 10:
        line.append('')
      line.append(str(y_coordinate))
      for x_coordinate in range(width): #cells
        for sonar in sonarList:
          if sonar.x == x_coordinate and sonar.y == y_coordinate:
            line.append(str(sonar.distance))
            sonarVisible = True
        if sonarVisible == False:
          line.append(random.choice(felder))
        sonarVisible = False
      line.append(str(y_coordinate))
      self.board.append(line)

class Sonar(object):
  """
  - sonar class, represents sonar object with x and y coordinates and distance to chests
  - takes x and y coordinates as arguments
  """
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.distance = 0

  def __eq__(self, other):
    ''' equality comparison: compares x and y coordinates '''
    return self.x == other.x and self.y == other.y

  def calculateDistance(self, chestList):
    '''calculate distance to nearest chest'''
    distance = 0

    for chest in chestList:
      distanceX = abs(chest.x - self.x)
      distanceY = abs(chest.y - self.y)
      if distanceX > distanceY:
        chestDistance = distanceX
      else:
        chestDistance = distanceY
      if chestDistance <= 9 and distance == 0:
        distance = chestDistance
      elif chestDistance <= 9 and chestDistance < distance:
        distance = chestDistance

    self.distance = distance

########## Functions ##########
def printIntro(chests):
  '''
  - prints game intro and instructions
  '''
  print('''
    S O N A R !
    Would you like to view the instructions? (y/n)
    ''')
  instructionsChoice = input()
  
  if instructionsChoice == 'y':
    showInstructions(chests)

def showInstructions(chests):
  print('''
    Instructions:
    You are the captain of the Simon, a treasure-hunting ship. Your current mission
    is to find the %s sunken treasure chests that are lurking in the part of the
    ocean you are in and collect them.

    To play, enter the coordinates of the point in the ocean you wish to drop a
    sonar device. The sonar can find out how far away the closest chest is to it.
    For example, the d below marks where the device was dropped, and the 2's
    represent distances of 2 away from the device. The 4's represent
    distances of 4 away from the device.

        444444444
        4       4
        4 22222 4
        4 2   2 4
        4 2 d 2 4
        4 2   2 4
        4 22222 4
        4       4
        444444444

    Press enter to continue...
    ''' % (chests))
  input()

  print('''
    For example, here is a treasure chest (the c) located a distance of 2 away
    from the sonar device (the d):

        22222
        c   2
        2 d 2
        2   2
        22222

    The point where the device was dropped will be marked with a 2.

    The treasure chests don't move around. Sonar devices can detect treasure
    chests up to a distance of 9. If all chests are out of range, the point
    will be marked with O

    If a device is directly dropped on a treasure chest, you have discovered
    the location of the chest, and it will be collected. The sonar device will
    remain there.

    When you collect a chest, all sonar devices will update to locate the next
    closest sunken treasure chest.

    Press enter to continue...
    ''')
  input()
  print()

def placeChests(width, height, chests, chestList):
  '''
  - creates chest object
  - checks no two chests on same place
  - adds chest object to chestList, until as many chests as set in CHESTS
  '''
  while len(chestList) != chests: #is chest list full?
    newChest = Chest(width - 1, height - 1) #create chest object
    if newChest not in chestList:
      chestList.append(newChest)
        
def printBoard(width, height, chestList, sonarList):
  '''
  - prints game board with borders and distances of chests from sonar devices
  '''
  firstLine, secondLine = createBorder(width)
  newBoard = Board()
  newBoard.calculateBoard(width, height, chestList, sonarList)

  #print top boarder
  print(*firstLine)
  print(*secondLine)

  #print game board
  for item in newBoard.board:
    print(*item)

  #print bottom border
  print(*secondLine)
  print(*firstLine)
  
def createBorder(width):
  '''
  - creates game board borders
  '''
  firstLine = []
  secondLine = []
  tenLine = ''

  for x in range(10):
    tenLine += (str(x) + ' ')
  tenLine = tenLine[:-1]

  firstLine.append('   ')
  firstLine.append('  ' * 9)

  secondLine.append('  ')

  for x in range(1,int(width/10)):
    firstLine.append(str(x))
    firstLine.append(' ' * 17)
  for x in range(int(width/10)):
    secondLine.append(tenLine)

  return firstLine, secondLine

def placeSonar(width, height, sonarList, chestList, sonars):
  '''
  - asks player to place sonar
  - validates player input
  - creates sonar object
  - adds sonar object to sonar list
  '''
  playerInput = ''
  pattern = '\d{2},\d{2}'
  validInput = False
  sonarsLeft = sonars - len(sonarList)

  while not validInput:
    print("You have %s sonar devices left. %s treasure chests remaining. Where do you want to drop the next sonar device? (00-%s,00-%s)" % (sonarsLeft, len(chestList), width - 1, height - 1))
    playerInput = input()
    if re.match(pattern, playerInput): #checks for valid input pattern
      x_coordinate = int(playerInput.split(',')[0])
      y_coordinate = int(playerInput.split(',')[1])
      if x_coordinate <= width - 1 and y_coordinate <= height - 1: #check for numbers within borders of game board
        newSonar = Sonar(x_coordinate, y_coordinate)
        if newSonar not in sonarList: #check no sonar already there at same place
          validInput = True
          sonarList.append(newSonar)
        else:
          print('You already have a sonar with these coordinates.')
      else:
        print('Please choose coordinates within the borders of the game board. (%s, %s)' % (width - 1, height - 1))
    else:
      print('Please type your chosen sonar location in the correct format: (00,00), ie. two sets of two digits, sperated by a comma.')

def updateSonarDistances(sonarList, chestList):
  ''' - updates distances to treasure chests left for all sonars '''
  for sonar in sonarList:
    sonar.calculateDistance(chestList)

def checkChestFind(sonarList, chestList):
  '''
  - checks for found chests or distance of last placed sonar to nearest chest
  '''
  lastSonar = sonarList[-1]
  chestFound = False

  for chest in chestList:
    if chest == lastSonar:
      chestList.remove(chest)
      chestFound = True
  return chestFound

def printPlayerInfo(sonarList, chestFound):
  '''
  - informs the player whether a chest was found or detected
  '''
  lastSonar = sonarList[-1]
  
  if chestFound == True:
    print('You have found a sunken treasure chest!')

  if chestFound == False and lastSonar.distance != 0:
    print('Treasure detected at a distance of %s from the sonar device.' % lastSonar.distance)

def gameChoice():
  '''
  - asks player, whether he wants to play again and validates the input
  - accepts only "y" or "n"
  '''
  print("Do you want to play again? (y/n)")

  if input() == 'y':
      return True

  return False

########## Game Loop ##########
gameState = True
# remains true for as long, as the player wants to keep playing

while gameState == True:
  ###### Globals ########
  winState = False #remains false as long as the player has not found all chests
  chestList = [] #list of chest objects
  sonarList = [] #list of sonar objects

  printIntro(CHESTS)
  placeChests(BOARD_WIDTH, BOARD_HEIGHT, CHESTS, chestList)
  printBoard(BOARD_WIDTH, BOARD_HEIGHT, chestList, sonarList)

  ########## Round Loop #########
  while len(sonarList) != SONARS and winState == False:
    chestFound = False #true if player has found a chest this round

    placeSonar(BOARD_WIDTH, BOARD_HEIGHT, sonarList, chestList, SONARS)
    chestFound = checkChestFind(sonarList, chestList)
    updateSonarDistances(sonarList, chestList)
    printBoard(BOARD_WIDTH, BOARD_HEIGHT, chestList, sonarList)
    printPlayerInfo(sonarList, chestFound)

    if len(chestList) == 0:
      winState = True

  if winState == True:
    print("Congratulations. You have found all %s treasure chests!" % (CHESTS))
  else:
    print('''
      We've run out of sonar devices! Now we have to turn the ship around and head for home with treasure chests still out there! Game over.
      The remaining chests were here:
      ''')
    for chest in chestList:
      print(chest.x, chest.y)

  gameState = gameChoice()
