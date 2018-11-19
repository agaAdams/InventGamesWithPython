# This is a simple pygame example with collision detection and key event handling

import pygame
import sys
import random
from pygame.locals import *

pygame.init()
pygame.key.set_repeat(1,50)
########## Constants ##########
WINDOWWIDTH = 400
WINDOWHEIGHT = 400
STARTINGFOOD = 50
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

########### Classes ###########
class playerBox(object):
    """black rectangular box representing the player"""
    def __init__(self):
        super(playerBox, self).__init__()
        self.color = BLACK
        self.rect = pygame.Rect(random.randint(0, WINDOWWIDTH - 50), random.randint(0, WINDOWHEIGHT - 50), 50, 50)
        
    def draw(self, surface):
        '''draws box as a rectangular shape on given surface'''
        pygame.draw.rect(surface, self.color, self.rect)

    def move(self, direction):
        '''moves box into given direction'''
        self.rect.move_ip(direction)

    def teleport(self):
        '''teleports box to random location'''
        self.rect = pygame.Rect(random.randint(0, WINDOWWIDTH - 50), random.randint(0, WINDOWHEIGHT - 50), self.rect.width, self.rect.height)

    def collide(self, other):
        '''tests if given rectangle collides with playerBox'''
        if self.rect.colliderect(other.rect):
            return True

class foodBox(object):
    """green rectangular box representing food"""
    def __init__(self, left, top):
        super(foodBox, self).__init__()
        self.color = GREEN
        self.rect = pygame.Rect(left, top, 20, 20)

    def draw(self, surface):
        '''draws box as a rectangular shape on given surface'''
        pygame.draw.rect(surface, self.color, self.rect)

    def eaten(self):
        '''removes box from food list'''
        food.remove(self)

########## Functions ##########
def createStartingFood():
    '''creates food boxes on game start'''
    for s in range(STARTINGFOOD):
        createFood()

def createFood(position=None):
    '''creates a food box at given or random position'''
    if position:
        newFood = foodBox(position[0], position[1])
    else:
        newFood = foodBox(random.randint(0, WINDOWWIDTH - 20), random.randint(0, WINDOWHEIGHT - 20))
    food.append(newFood)

############ Main ############
mainClock = pygame.time.Clock()
player = playerBox()
food = []
window = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption("Food Hunt")
createStartingFood()

########## Game Loop ##########
while True:
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
            elif event.key == K_x:
                player.teleport()
            elif event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
        elif event.type == MOUSEBUTTONUP:
            createFood(position=event.pos)

    window.fill(WHITE)

    if len(food) < STARTINGFOOD:
        createFood()

    for f in food:
        if player.collide(f):
            f.eaten()

    for f in food:
        f.draw(window)
    player.draw(window)

    pygame.display.update()
    mainClock.tick(40)
