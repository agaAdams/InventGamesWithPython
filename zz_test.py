import sys
import random

########## Constants ##########
WIDTH = 8
HEIGHT = 8
DIRECTIONS = [[-1, -1], [0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0]]

########### Classes ###########
class Tile(object):
  """game tile"""
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.lines = []
    self.validLines = []

  def updateLines(self):
    for d in DIRECTIONS:
      newLine = Line(self.x, self.y, d)
      self.validLines.append(newLine)

  def onBoard(self):
    '''checks if tile within game board borders'''
    if self.x >= 0 and self.x < (WIDTH) and self.y >= 0 and self.y < (HEIGHT):
      return True

class Line(object):
  """line of tiles"""
  def __init__(self, startX, startY, direction):
    super(Line, self).__init__()
    self.startX = startX
    self.startY = startY
    self.direction = direction
    self.tiles = []

newTile = Tile(9, 1)
newTile.updateLines()
print(newTile.onBoard())
for line in newTile.validLines:
  print(line.startX, line.startY, line.direction, line.tiles)
