import pygame as pyg
import random
import time

class Attacker(object):
    def __init__(self):
        self.rect = pyg.Rect((500,0,50,10))

    def draw(self, color, display):
            pyg.draw.rect(display, color, self.rect)

    def spawn_attacker(self):
            new_x = 0
            new_y = 0
            attacker_x = 0
            attacker_y = 0
            wall = random.randint(0,3)
            if wall == 0:
                new_x = random.randint(50,750)
                new_y = 0
                attacker_x = 50
                attacker_y = 10
            elif wall == 1:
                new_x = 790
                new_y = random.randint(50,550)
                attacker_x = 10
                attacker_y = 50
            elif wall == 2:
                new_x = random.randint(50,750)
                new_y = 590
                attacker_x = 50
                attacker_y = 10
            elif wall == 3:
                new_x = 0
                new_y = random.randint(50,550)
                attacker_x = 10
                attacker_y = 50
        
            return new_x, new_y, attacker_x, attacker_y

    def flash(self,display):
        pyg.display.update()
        self.draw((255,255,255), display)
        pyg.display.update()
        self.draw((255,0,0), display)
        pyg.display.update()
