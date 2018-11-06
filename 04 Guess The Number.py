# This is a Guess the Number Game
import random

secretNumber = random.randint(1,20)

print("Hello! What is your name?")
userName = input()

print("Well, " + userName + ". I am thinking of a number between 1 and 20.")

for rounds in range(1,7):
    print("Take a guess.")
    userNumber = int(input())

    if userNumber < secretNumber:
        print("Your guess is too low.")
    elif userNumber > secretNumber:
        print("Your guess is too high.")
    else:
        break

if secretNumber != userNumber:
    print("Sorry, " + userName + ". You loose. My secret Number was " + str(secretNumber) + ".")
else:
    print("Good job, " + userName + ". You guessed my number in " + str(rounds) + " guesses!")
