import pygame as pyg

class Beam(object):
    def __init__(self):
        self.rect = pyg.Rect((0,0,0,0))
        self.color = (255,255,255)

    def draw(self,color,display):
        pyg.draw.rect(display, self.color, self.rect)