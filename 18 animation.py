# This is a simple pygame animation example

import pygame
import sys
import random
from pygame.locals import *

pygame.init()

########## Constants ##########
WINDOWWIDTH = 400
WINDOWHEIGHT = 400
BOXES = 5
SPEED = 1

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

COLORS = [BLACK, RED, GREEN, BLUE]
DIRECTIONS = [[-1, -1], [1, -1], [1, 1], [-1, 1]]

########### Classes ###########
class Box(object):
    """simple rectangular box"""
    def __init__(self, width, height, color, position, direction):
        self.color = color
        self.direction = direction
        self.boxRect = pygame.Rect(position[0], position[1], width, height)

    def moveBox(self):
        '''moves box and reverses movement direction if box hits the window border'''
        if self.boxRect.left <= 0 or self.boxRect.right >= WINDOWWIDTH:
            self.direction[0] = -self.direction[0]
        if self.boxRect.top <= 0 or self.boxRect.bottom >= WINDOWHEIGHT:
            self.direction[1] = -self.direction[1]
        self.boxRect = self.boxRect.move(self.direction[0] * SPEED, self.direction[1] * SPEED)
        
########## Functions ##########
def createBoxes(number):
    '''initializes required number of boxes and adds them to list of boxes, returns None'''
    for box in range(BOXES):
        width = random.randint(20, WINDOWWIDTH/4)
        height = random.randint(20, WINDOWHEIGHT/4)
        color = random.choice(COLORS)
        position = random.randint(0, WINDOWWIDTH - width), random.randint(0, WINDOWHEIGHT - height)
        direction = random.choice(DIRECTIONS)
        newBox = Box(width, height, color, position, direction)
        boxes.append(newBox)

############ Main ############
b1 = pygame.Rect(random.randint(0, WINDOWWIDTH), random.randint(0, WINDOWHEIGHT), random.randint(20, WINDOWWIDTH/4), random.randint(20, WINDOWHEIGHT/4))
b2 = pygame.Rect(random.randint(0, WINDOWWIDTH), random.randint(0, WINDOWHEIGHT), random.randint(20, WINDOWWIDTH/4), random.randint(20, WINDOWHEIGHT/4))
b3 = pygame.Rect(random.randint(0, WINDOWWIDTH), random.randint(0, WINDOWHEIGHT), random.randint(20, WINDOWWIDTH/4), random.randint(20, WINDOWHEIGHT/4))

boxes = [[b1, random.choice(COLORS), random.choice(DIRECTIONS)], [b2, random.choice(COLORS), random.choice(DIRECTIONS)], [b3, random.choice(COLORS), random.choice(DIRECTIONS)]]
window = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption("Animated Boxes")
# createBoxe s(BOXES)

########## Game Loop ##########
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    window.fill(WHITE)

    for box in boxes:
        pygame.draw.rect(window, box[1], box[0])
        box[0].move_ip(box[2])
        if box[0].left <= 0 or box[0].right >= WINDOWWIDTH:
            box[2][0] = -box[2][0]
        if box[0].top <= 0 or box[0].bottom >= WINDOWHEIGHT:
            box[2][1] = -box[2][1]

    pygame.display.update()
