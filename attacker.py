import pygame as pyg

class Attacker(object):
    def __init__(self):
        self.rect = pyg.Rect((250,500,50,10))

    def draw(self, display):
            pyg.draw.rect(display,(255,0,0),self.rect)
