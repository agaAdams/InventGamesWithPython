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

########### Classes ###########
class Player(object):
    """represents the players sprite"""
    def __init__(self, image):
        super(Player, self).__init__()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()

    def draw(self, surface):
        '''draws sprite on given surface positioned on a rectangle'''
        surface.blit(self.image, self.rect)

    def move(self, direction):
        '''moves sprite into given direction'''
        self.rect.move_ip(direction)

    def collide(self, other):
        '''tests if given object collides with player'''
        if self.rect.colliderect(other.rect):
            return True

class Baddie(object):
    """represents the baddies"""
    def __init__(self, image, direction, speed):
        super(Baddie, self).__init__()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.direction = direction
        self.speed = speed

    def draw(self, surface):
        '''draws sprite on given surface positioned on a rectangle'''
        surface.blit(self.image, self.rect)

    def move(self):
        '''moves sprite into given direction'''
        self.rect.move_ip(self.direction)

    def changeDirection(self, direction):
        '''changes the direction the sprite moves'''

    def slow(self, speed):
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

########## Game Loop ##########
