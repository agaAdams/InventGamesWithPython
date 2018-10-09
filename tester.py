import random

class Chest(object):
    """ chest class, represents treasure chest with x and y coordinates"""
    def __init__(self, x = random.randint(0, 60), y = random.randint(0, 15)):
        self.x = x
        self.y = y

    def __eq__(self, other): 
        return self.__dict__ == other.__dict__

c1 = Chest(1,2)
c2 = Chest(1,2)
c3 = Chest()

print(c1.x, c2.x, c3.x, c1.y, c2.y, c3.y)
print(c1 == c2)
print(c2 == c3)



