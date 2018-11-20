# This is a simple pygame example with collision detection, key event handling, sprites and sounds

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
PLAYER_IMAGE = 'player.png'
FOOD_IMAGE = 'cherry.png'
SOUND = 'pickup.wav'
BACKGROUND_MUSIC = 'background.mid'
INFLATE = 2

########### Classes ###########
class playerBox(object):
    """sprite representing the player"""
    def __init__(self, image):
        super(playerBox, self).__init__()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.move_ip(random.randint(0, WINDOWWIDTH - 50), random.randint(0, WINDOWHEIGHT - 50))
        
    def draw(self, surface):
        '''draws sprite on given surface positioned on a rectangle'''
        surface.blit(self.image, self.rect)

    def move(self, direction):
        '''moves sprite into given direction'''
        self.rect.move_ip(direction)

    def teleport(self):
        '''teleports sprite to random location'''
        self.rect = pygame.Rect(random.randint(0, WINDOWWIDTH - 50), random.randint(0, WINDOWHEIGHT - 50), self.rect.width, self.rect.height)

    def eat(self, other):
        '''tests if given rectangle collides with playerBox, resizes playerBox on collision'''
        if self.rect.colliderect(other.rect):
            other.eaten()
            self.rect.inflate_ip(INFLATE, INFLATE)
            self.image = pygame.transform.scale(self.image, (self.rect.width, self.rect.height))
            pickUpSound.play()

class foodBox(object):
    """sprite representing food"""
    def __init__(self, image, left, top):
        super(foodBox, self).__init__()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.move_ip(left, top)

    def draw(self, surface):
        '''draws sprite on given surface'''
        surface.blit(self.image, self.rect)

    def eaten(self):
        '''removes sprite from food list'''
        food.remove(self)

########## Functions ##########
def createStartingFood():
    '''creates food boxes on game start'''
    for s in range(STARTINGFOOD):
        createFood()

def createFood(position=None):
    '''creates a food box at given or random position'''
    if position:
        newFood = foodBox(FOOD_IMAGE, position[0], position[1])
    else:
        newFood = foodBox(FOOD_IMAGE, random.randint(0, WINDOWWIDTH - 20), random.randint(0, WINDOWHEIGHT - 20))
    food.append(newFood)

############ Main ############
mainClock = pygame.time.Clock()
pickUpSound = pygame.mixer.Sound(SOUND)
pygame.mixer.music.load(BACKGROUND_MUSIC)
pygame.mixer.music.play(-1, 0.0)

player = playerBox(PLAYER_IMAGE)
food = []
window = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption("Cherry Picker")
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
        player.eat(f)

    for f in food:
        f.draw(window)
    player.draw(window)

    pygame.display.flip()
    mainClock.tick(40)
