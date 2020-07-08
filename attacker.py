import pygame as pyg
import random
import time

class Attacker(object):
    def __init__(self):
        self.x = 500
        self.y = 0
        self.rect = pyg.Rect((self.x,self.y,50,10))
        self.color = (255,0,0)
        self.wall = 0
        self.flag = 0
        self.beamTimer = 0

    def draw(self, color, display):
            pyg.draw.rect(display, self.color, self.rect)

    def spawn_attacker(self):
            new_x = 0
            new_y = 0
            self.x = 0
            self.y = 0
            self.beamTimer = 400
            self.flag = 1
            wall = random.randint(0,3)
            if wall == 0:
                self.wall = 0
                new_x = random.randint(50,750)
                new_y = 0
                self.x = 50
                self.y = 10
            elif wall == 1:
                self.wall = 1
                new_x = 790
                new_y = random.randint(50,550)
                self.x = 10
                self.y = 50
            elif wall == 2:
                self.wall = 2
                new_x = random.randint(50,750)
                new_y = 590
                self.x= 50
                self.y = 10
            elif wall == 3:
                self.wall = 3
                new_x = 0
                new_y = random.randint(50,550)
                self.x = 10
                self.y = 50
        
            return new_x, new_y

    def update_color(self,color):
        self.color = color

    def flash(self,display):
        self.draw((255,0,0), display)
        pyg.display.update()
        pyg.time.delay
        self.draw((255,255,255), display)
        pyg.display.update()
        self.draw((255,0,0), display)
        pyg.display.update()
