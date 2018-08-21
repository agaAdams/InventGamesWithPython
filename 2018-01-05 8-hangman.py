#This is a hangman game, where the user has to guess a word, the computer has selected randomly before.
import random

########### Constants ############

#all Hangman pics in a list
HANGMAN_PICS = ['''
  +---+
      |
      |
      |
     ===''', '''
  +---+
  O   |
      |
      |
     ===''', '''
  +---+
  O   |
  |   |
      |
     ===''', '''
  +---+
  O   |
 /|   |
      |
     ===''', '''
  +---+
  O   |
 /|\  |
      |
     ===''', '''
  +---+
  O   |
 /|\  |
 /    |
     ===''', '''
  +---+
  O   |
 /|\  |
 / \  |
     ===''']

# word list for the computer to choose from
WORDS = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()

############ Functions #############

def randomWord():
  '''
  chooses a word at random from the word list
  returns the random word
  '''
  wordNumber = random.randint(0, len(WORDS) - 1)
  return WORDS[wordNumber]

def compareLists(list1, list2, whichList):
  '''
  - checks whether elements in list1 are also in list2
  - returns either the list of matches or missed
  '''
  matches = []
  missed = []
  for x in list1:
    if x in list2:
      matches.append(x)
    else:
      missed.append(x)

  if whichList == True:
    return matches
  else:
    return missed

def showWrongLetters():
  '''shows wrong letters the user has already guessed'''
  missed = compareLists(guessedLetters, secretWord, False)
  print("Missed letters: ", end='')

  for letter in missed:
    print(letter, end=' ')

  print()

def showCorrectLetters():
  '''shows correct letters the user has already guessed'''
  matches = compareLists(secretWord, guessedLetters, True)

  for letter in secretWord:
      if letter in matches:
          print(letter, end=' ')
      else:
          print('_', end=' ')

def showGameBoard(counter):
  print(HANGMAN_PICS[counter])
  showWrongLetters()
  showCorrectLetters()

def validateGuessedLetter():
  '''
  - checks whether the user input is valid
  - accepts only a single letter
  - sets guessedLetter to lower case
  '''

  global guessedLetter
  guessedLetter = ''

  while not guessedLetter.isalpha() or len(guessedLetter) != 1:
    print("\nGuess ONE letter: ")
    guessedLetter = input()

  guessedLetter = guessedLetter.lower()

def gameChoice():
  '''
  - asks the player, whether he wants to play again and validates the input
  - accepts only "y" or "n"
  - sets the gameState accordingly
  '''

  global gameState
  gameChoice = ''

  while gameChoice != 'y' and gameChoice != 'n':
      print("Do you want to play again? (y/n)")
      gameChoice = input()

  if gameChoice == 'n':
      gameState = False

########## Game Loop ###########
gameState = True

while gameState == True:
  ###### Game Globals ######
  counter = 0
  guessedLetters = []
  guessedLetter = ''
  gameRound = True
  secretWord = randomWord()

  print("H A N G M A N")

  while gameRound == True:
    #round loop

      #print game board
      showGameBoard(counter)

      # validate player input
      validateGuessedLetter()

      # ?has this letter have been guessed already?
      if guessedLetter not in guessedLetters:
        guessedLetters.append(guessedLetter)

        # ?is this letter part of the secret word?
        if guessedLetter in secretWord:
          print("That one was right!")

          # ?has the player guessed the whole word?
          treffer = compareLists(secretWord, guessedLetters, True)
          if len(treffer) == len(secretWord):
            gameRound = False
            print("You win! The secret word was " + secretWord.upper() + ".")

        else:
          print("Sorry, this letter is not in my secret word.")
          counter = counter + 1

          # ?has the player had his six guesses?
          if counter > 5:
            gameRound = False
            print(HANGMAN_PICS[6])
            print("YOU LOOSE!!! The secret word was " + secretWord.upper() + ".")
      else:
        print("You alreade have guessed this letter.")

  # ?does the player want to play again?
  gameChoice()

