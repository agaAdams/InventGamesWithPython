#This program encrypts and decrypts messages with the Caesar Cipher method
import random

########## Constants ##########
MAX_KEY_LENGTH = 26

########## Functions ##########
def printIntro():
  playerInput = ''
  
  while playerInput is not 'e' and playerInput is not 'd':
    print("Do you wish to (e)ncrypt or (d)ecrypt a message?")
    playerInput = input()

  if playerInput == 'e':
    return True
  else:
    return False

def enterMessage():
  playerInput = ''
  print('Enter your message:')
  playerInput = input()
  return playerInput

def enterKey(length):
  playerInput = ''
  inputValid = False

  while not inputValid:
    print('Enter the key number (1-%s)' % (length))
    playerInput = input()
    if playerInput.isdigit:
      playerInput = int(playerInput)
      if playerInput <= length and playerInput > 0:
        inputValid = True

  return playerInput

def calculateTranslation(message, key, choice):
  newMessage = ''

  if choice == False:
    key *= - 1

  for c in message:
    index = ord(c)
    offsetIndex = index + key
    offsetCharacter = chr(offsetIndex)
    newMessage += offsetCharacter

  return newMessage

def gameChoice():
  '''
  - asks player, whether he wants to play again and validates the input
  - accepts only "y" or "n"
  '''
  gameChoice = ''

  while gameChoice != 'y' and gameChoice != 'n':
      print("Do you want to enter an other message? (y/n)")
      gameChoice = input()

  if gameChoice == 'y':
      return True

  return False

########## Game Loop ##########
gameState = True
# remains true for as long, as the player wants to keep playing

while gameState == True:
  ###### Globals ########

  ########## Round Loop #########
  # encrypt or decrypt?
  encrypt = printIntro()
  # enter message
  message = enterMessage()
  # enter key and validate
  key = enterKey(MAX_KEY_LENGTH)
  # calculate translation
  translation = calculateTranslation(message, key, encrypt)
  # print translation
  print('Your translated text is:')
  print(translation)

  # ?does the player want to play again?
  gameState = gameChoice()
