# This is the game of Dragon Realm
import pdb; pdb.set_trace()
import random
import time

def printIntro():
    print('''You are in a land full of dragons.
        In front of you, you see two caves.
        In one cave, the dragon is friendly and will share his treasure with you.
        The other dragon is greedy and hungry, and will eat you on sight.''')

def caveChoice():
    caveChoice = ''
    while caveChoice != '1' and caveChoice != '2':
        print("Which cave will you go into? (1 or 2)")
        caveChoice = input()

    return int(caveChoice)

def randomCave(chosenCave):
    print("You approach the cave...")
    time.sleep(2)
    print("It is dark and spooky...")
    time.sleep(2)
    print("A large dragon jumps out in front of you! He opens his jaws and...")
    time.sleep(5)

    randomCave = random.randint(1,2)
    if randomCave != chosenCave:
        print("Gobbles you down in one bite!")
    else:
        print("Gives you his treasure!")

def gameChoice():
    gameChoice = ''
    while gameChoice != 'y' and gameChoice != 'n':
        print("Do you want to play again? (y/n)")
        gameChoice = input()

        if gameChoice == 'n':
            global gameState
            gameState = False

gameState = True

while gameState == True:
    printIntro()
    randomCave(caveChoice())
    gameChoice()
