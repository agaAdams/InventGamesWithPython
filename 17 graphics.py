import pygame, sys
from pygame.locals import *

pygame.init() #initialize all of pygames modules

windowSurface = pygame.display.set_mode((500, 400)) #create graphical window as Surface object
pygame.display.set_caption("Hello World!")  # set caption of window

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

basicFont = pygame.font.SysFont(None, 48)
text = basicFont.render("Hello world!", True, WHITE, BLUE)
textRect = text.get_rect()
textRect.centerx = windowSurface.get_rect().centerx
textRect.centery = windowSurface.get_rect().centery

windowSurface.fill(WHITE)
windowSurface.blit(text, textRect) #copy rendered text onto rectangle
pygame.display.update() #make everything that was drawn onto the window surface visible on computer screen

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

