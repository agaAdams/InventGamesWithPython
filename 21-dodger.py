# This is a simple dodger game. The player has to dodge the characters falling from the top of the screen. Every time a character reaches the bottom of the screen, the player's score goes up.

import pygame
import sys
import random
from pygame.locals import *

pygame.init()
pygame.key.set_repeat(1,50)
########## Constants ##########
WINDOWWIDTH = 400
WINDOWHEIGHT = 400
SPEED = 2
WHITE = (255, 255, 255)
STARTING_BADDIES = int(WINDOWWIDTH / 20 / 2)
PLAYER_IMAGE = 'player.png'
BADDIE_IMAGE = 'baddie.png'
BACKGROUND_MUSIC = 'background.mid'
########### Classes ###########
class Box(object):
    """docstring for Box"""
    def __init__(self, image):
        super(Box, self).__init__()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
    
    def draw(self, surface):
        '''draws sprite on given surface positioned on a rectangle'''
        surface.blit(self.image, self.rect)

    def move(self, direction):
        '''moves sprite into given direction'''
        self.rect.move_ip(direction)

class Player(Box):
    """represents the players sprite"""
    def __init__(self, image):
        super().__init__(image)
        self.rect.move_ip(random.randint(0, WINDOWWIDTH - 20), WINDOWHEIGHT-50) 

    def collide(self, other):
        '''tests if given object collides with player'''
        if self.rect.colliderect(other.rect):
            return True

class Baddie(Box):
    """represents the baddies"""
    def __init__(self, image):
        super().__init__(image)
        self.direction = [0, 1]
        self.speed = SPEED
        self.rect.move_ip(random.randint(0, WINDOWWIDTH - 20), 0) 

    def move(self):
        '''moves sprite into given direction'''
        self.rect.move_ip(self.direction)

    def changeDirection(self, direction):
        '''changes the direction the sprite moves'''
        self.direction[1] = -self.direction[1]

    def changeSpeed(self, speed):
        '''changes the speed the sprite moves with'''
        self.speed = speed

    def disappear(self, bottom):
        '''makes the baddie disappear and raise the games score'''
        if self.rect.bottom >= bottom:
            baddies.remove(self)
            score.updateCurrentScore()

class Score(object):
    """holds score of current game and high score"""
    def __init__(self):
        super(Score, self).__init__()
        self.currentScore = 0
        self.highScore = 0

    def updateCurrentScore(self):
        self.currentScore += 1

    def updateHighScore(self):
        if self.currentScore > self.highScore:
            self.highScore = self.currentScore

    def resetCurrentScore(self):
        self.currentScore = 0
        
########## Functions ##########
def createBaddie():
    newBaddie = Baddie(BADDIE_IMAGE)
    baddies.append(newBaddie)

def createStartingBaddies():
    for b in range(STARTING_BADDIES):
        createBaddie()

def gameOver():
    score.updateHighScore()
    score.resetCurrentScore()

def gameChoice():
    pass
############ Main ############
gameState = True
mainClock = pygame.time.Clock()
pygame.mixer.music.load(BACKGROUND_MUSIC)
# pygame.mixer.music.play(-1, 0.0)

window = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption("Dodger")

score = Score()

########## Game Loop ##########
while gameState:
    player = Player(PLAYER_IMAGE)
    baddies = []
    createStartingBaddies()
    endState = False

    while endState == False:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_UP:
                    player.move([0, -4])
                elif event.key == K_DOWN:
                    player.move([0, 4])
                elif event.key == K_LEFT:
                    player.move([-4, 0])
                elif event.key == K_RIGHT:
                    player.move([4, 0])
            elif event.type == KEYUP:
                if event.key == K_UP:
                    player.move([0, 0])
                elif event.key == K_DOWN:
                    player.move([0, 0])
                elif event.key == K_LEFT:
                    player.move([0, 0])
                elif event.key == K_RIGHT:
                    player.move([0, 0])
                elif event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        window.fill(WHITE)

        if len(baddies) < STARTING_BADDIES:
            createBaddie()

        for b in baddies:
            b.move()
            b.draw(window)
            b.disappear(WINDOWHEIGHT)
            if player.collide(b):
                endState = True

        player.draw(window)
        pygame.display.flip()
        mainClock.tick(40)

    gameOver()
