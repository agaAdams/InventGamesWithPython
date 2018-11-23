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

    def changeDirection(self, direction):
        '''changes the direction the sprite moves'''

    def changeSpeed(self, speed):
        '''changes the speed the sprite moves with'''

    def disappear(self, bottom):
        '''makes the baddie disappear and raise the games score'''

class Score(object):
    """holds score of current game and high score"""
    def __init__(self):
        super(Score, self).__init__()
        self.currentScore = 0
        self.highScore = 0

    def updateCurrentScore(self):
        self.currentScore += 1

    def updateHighScore(self, newScore):
        if newScore > self.highScore:
            self.highScore = newScore

    def resetCurrentScore(self):
        self.currentScore = 0
        
########## Functions ##########

############ Main ############
window = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
newPlayer = Player('player.png')
newBaddie = Baddie('baddie.png')
########## Game Loop ##########
while True:
    newPlayer.draw(window)
    newBaddie.draw(window)
    pygame.display.flip()
