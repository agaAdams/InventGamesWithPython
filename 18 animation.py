# This is a simple pygame animation example

import pygame
import sys
import random
from pygame.locals import *

pygame.init()

########## Constants ##########
WINDOWWIDTH = 400
WINDOWHEIGHT = 400
BOXES = 8
SPEED = 2

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

COLORS = [BLACK, RED, GREEN, BLUE]
DIRECTIONS = [[-1, -1], [1, -1], [1, 1], [-1, 1]]

########### Classes ###########
class Box(object):
    """rectangular box"""
    def __init__(self, width, height, color, position, direction):
        self.color = color
        self.direction = direction
        self.rect = pygame.Rect(position[0], position[1], width, height)

    def drawBox(self, surface):
        '''draws box as a rectangular shape on given surface'''
        pygame.draw.rect(surface, self.color, self.rect)

    def collideBox(self, width, height):
        '''reverses movement direction if box hits any of the given borders'''
        if self.rect.left < 0:
            self.direction[0] = -self.direction[0]
        if self.rect.right > width:
            self.direction[0] = -self.direction[0]
        if self.rect.top < 0:
            self.direction[1] = -self.direction[1]
        if self.rect.bottom > height:
            self.direction[1] = -self.direction[1]

    def moveBox(self):
        '''moves box into it's direction by set speed'''
        newDirection = [SPEED * d for d in self.direction]
        self.rect.move_ip(newDirection)
        
########## Functions ##########
def createBoxes(number):
    '''initializes required number of boxes and adds them to list of boxes, returns None'''
    for box in range(BOXES):
        width = random.randint(20, WINDOWWIDTH/4)
        height = random.randint(20, WINDOWHEIGHT/4)
        color = random.choice(COLORS)
        position = random.randint(0, WINDOWWIDTH - width), random.randint(0, WINDOWHEIGHT - height)
        direction = random.choice(DIRECTIONS).copy()
        newBox = Box(width, height, color, position, direction)
        boxes.append(newBox)

############ Main ############
boxes = []
window = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption("Animated Boxes")
createBoxes(BOXES)

########## Game Loop ##########
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    window.fill(WHITE)

    for box in boxes:
        box.collideBox(pygame.display.Info().current_w, pygame.display.Info().current_h)
        box.moveBox()
        box.drawBox(window)

    pygame.display.update()
