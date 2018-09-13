#This is a sonar game. The player places sonar devices at various places in the ocean to locate sunken treasure chests.

#game description
import random

########## Constants ##########
SONARS = 3
CHESTS = 3
BOARD_WIDTH = 60
BOARD_HEIGHT = 16

########### Classes ###########
class Chest(object):
  """ chest class, represents treasure chest with x and y coordinates"""
  global BOARD_WIDTH
  global BOARD_HEIGHT
  def __init__(self):
    self.x = random.randint(0, BOARD_WIDTH)
    self.y = random.randint(0, BOARD_HEIGHT)
  def __eq__(self, other):
    return self.x == other.x and self.y == other.y

class Sonar(object):
  """docstring for Sonar"""
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.distance = random.randint(0,9)

  def calculateDistance():
    '''calculate distance to nearest chest'''
    self.distance = 0
    
   
########## Functions ##########
def printIntro():
  '''
  - prints game intro and instructions
  '''
  print('''
    S O N A R !
    Would you like to view the instructions? (y/n)
    ''')
  instructionsChoice = input()
  
  if instructionsChoice == 'y':
    showInstructions()

def showInstructions():
  print('''
    Instructions:
    You are the captain of the Simon, a treasure-hunting ship. Your current mission
    is to find the three sunken treasure chests that are lurking in the part of the
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
    ''')
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
    newChest = Chest() #create chest object
    if newChest not in chestList:
      chestList.append(newChest)
        
def printBoard(width, height, chestList, sonarList):
  '''
  - prints game board with distances of chests from sonar devices
  - prints borders
  - creates board object
    - list of lists x/y
    - for every field
      - if field corresponds to sonar
        - print distance of sonar
      - else print random character: ~ or `
  - print game board 
  '''
  firstLine = ' ' * 10
  secondLine = ''
  felder = ['~', '`']
  board = []

  for x in range(1,int(width/10)):
    firstLine += str(x)
    firstLine += ' ' * 9
  print('  ' + firstLine)

  for x in range(10):
    secondLine += str(x)
  secondLine *= int(width/10)
  print('  ' + secondLine)

  for y_coordinate in range(height): #zeilen
    if y_coordinate < 10:
      print(' ', end='')
    print(y_coordinate, end='')
    for x_coordinate in range(width): #felder in zeilen/spalten
  #     for sonar in sonarList:
  #       if sonar.x == x_coordinate and sonar.y == y_coordinate:
  #         print(sonar.distance, end='')
  #       else:
      print(random.choice(felder), end='')
    print(y_coordinate)

  print('  ' + secondLine)
  print('  ' + firstLine)

def placeSonar(width, height, sonarList, chestList, sonars):
  '''
  - asks player to place sonar:
  You have X sonar devices left. X treasure chests remaining. Where do you want to drop the next sonar device? (0-59 0-14) (or type quit)
  - validates player input, only two numbers, first number max boardWidth, second number max boardHeight; no two sonars at same place; else quit -> quit game
  - creates sonar object
    - x, y, distance
    - calculates and updates distance to nearest chest
  - checks for found chests or distance from chests
    - if distance = 0
      - prints: You have found a sunken treasure chest!
      - removes corresponding chest from chestList
    - if distance 1-10
      - prints: Treasure detected at a distance of X from the sonar device.
  - adds sonar object to sonar list
  - updates sonar list
  '''

def gameChoice():
  '''
  - asks player, whether he wants to play again and validates the input
  - accepts only "y" or "n"
  '''
  gameChoice = ''

  while gameChoice != 'y' and gameChoice != 'n':
      print("Do you want to play again? (y/n)")
      gameChoice = input()

  if gameChoice == 'y':
      return True

  return False

########## Game Loop ##########
gameState = True
# remains true for as long, as the player wants to keep playing

while gameState == True:
  ###### Globals ########
  winState = False
  chestList = [] #list of chest objects
  sonarList = [Sonar(5,9), Sonar(23,6), Sonar(42,2)] #list of sonar objects

  printIntro() #print game intro and game instructions
  placeChests(BOARD_WIDTH, BOARD_HEIGHT, CHESTS, chestList) # create chests, add to chests list
  printBoard(BOARD_WIDTH, BOARD_HEIGHT, chestList, sonarList) #Spielbrett mit aktualisierten Sonar-zahlen drucken

  ########## Round Loop #########
  while len(sonarList) != SONARS and winState == False:
    placeSonar(BOARD_WIDTH, BOARD_HEIGHT, sonarList, chestList, SONARS) #Spieler fragen, wo sein sonar hin soll; eingabe validieren
    printBoard(BOARD_WIDTH, BOARD_HEIGHT, chestList, sonarList) #Spielbrett mit aktualisierten Sonar-zahlen drucken
    if len(chestList) == 0:
      winState = True # alle kisten gefunden?

  if winState == True: #alle Kisten gefunden? win
    print("Congratulations. You have found all %s treasure chests!" % (CHESTS))
  else: #alle Sonare verbraucht? lost
    print('''
      We've run out of sonar devices! Now we have to turn the ship around and head for home with treasure chests still out there! Game over.
      The remaining chests were here:
      ''')
    for x in chestList:
      print() #objekt x, objekt y

  # ?does the player want to play again?
  gameState = gameChoice()
