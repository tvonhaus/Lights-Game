import pygame as pyg

class Player(object):
    def __init__(self):
        self.rect = pyg.Rect((200,150,10,10))
                
    def player_control(self):
        key = pyg.key.get_pressed()
        dist = 15
        if key[pyg.K_LEFT]:
            self.rect.move_ip(-dist,0)
        if key[pyg.K_RIGHT]:
            self.rect.move_ip(dist,0)
        if key[pyg.K_UP]:
            self.rect.move_ip(0,-dist)
        if key[pyg.K_DOWN]:
            self.rect.move_ip(0,dist)

    def draw(self, display):
        pyg.draw.rect(display,(255,255,255),self.rect)
