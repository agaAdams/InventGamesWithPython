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
     ===''', '''
  +---+
 [O   |
 /|\  |
 / \  |
     ===''', '''
  +---+
 [O]  |
 /|\  |
 / \  |
     ===''']

# word dictionary for the computer to choose from
# every value is a list containing several words
WORDS = {'Color':'red orange yellow green blue indigo violet white black brown'.split(),
'Shape':'square triangle rectangle circle ellipse rhombus trapazoid chevron pentagon hexagon septagon octogon'.split(),
'Fruit':'apple orange lemon lime pear watermelon grape grapefruit cherry banana cantalope mango strawberry tomato'.split(),
'Animal':'bat bear beaver cat cougar crab deer dog donkey duck eagle fish frog goat leech lion lizard monkey moose mouse otter owl panda python rabbit rat shark sheep skunk squid tiger turkey turtle weasel whale wolf wombat zebra'.split()}

############ Functions #############

def randomWord():
  '''
  chooses at random: first a list of words from a dictionary and then a word from this word list
  returns list name and random word
  '''
  listName = random.choice(list(WORDS.keys()))
  wordNumber = random.randint(0, len(WORDS[listName]) - 1)
  return listName, WORDS[listName][wordNumber]

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

def showGameBoard(roundCounter):
  print(HANGMAN_PICS[roundCounter])

  if gameRound == True:
    showWrongLetters()
    showCorrectLetters()
    print("\nMy secret word is a(n) " + wordList)
  else:
    print("YOU LOOSE!!! The secret word was " + secretWord.upper() + ".")

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

def setDifficulty():
  '''
  asks the player for intended difficulty and sets the roundCounter to an appropriate level
  '''
  difficultyChoice = ''
  global maxCounter

  while difficultyChoice !='e' and difficultyChoice !='h':
    print("Please choose difficulty: (e)asy or (h)ard.")
    difficultyChoice = input()

  if difficultyChoice == 'e':
    maxCounter = 7
  else:
    maxCounter = 5

########## Game Loop ###########
gameState = True

while gameState == True:
  ###### Game Globals ######
  roundCounter = 0
  maxCounter = 0
  guessedLetters = []
  guessedLetter = ''
  gameRound = True
  wordList, secretWord = randomWord()

  #determine difficult level
  setDifficulty()

  print("H A N G M A N")

  while gameRound == True:
    #round loop

      #print game board
      showGameBoard(roundCounter)

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
          roundCounter = roundCounter + 1

          # ?has the player had all of his guesses?
          if roundCounter > maxCounter:
            gameRound = False
            showGameBoard(roundCounter)
      else:
        print("You alreade have guessed this letter.")

  # ?does the player want to play again?
  gameChoice()

