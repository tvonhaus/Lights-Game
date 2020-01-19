import pygame as pyg
import time
import random
from player import Player 
from attacker import Attacker

pyg.init()
dis_width = 800
dis_height = 600
dis = pyg.display.set_mode((dis_width,dis_height))
dis_rect = dis.get_rect()
pyg.display.set_caption('Lights')

white = (255,255,255)
black = (0,0,0)
attack_timer = 1000


player = Player()
attacker1 = Attacker()
clock = pyg.time.Clock()

print(attacker1.rect)
spawn_attacker_event = pyg.USEREVENT + 1

pyg.time.set_timer(spawn_attacker_event, attack_timer)

game_over = False
while not game_over:
    for event in pyg.event.get():
        if event.type==pyg.QUIT:
            game_over = True
        elif event.type == spawn_attacker_event:
            new_x , new_y, attacker_x, attacker_y = attacker1.spawn_attacker() 
            attacker1.rect = (new_x,new_y,attacker_x,attacker_y)
            #attacker1.flash(dis)

    dis.fill(black)
    player.draw(dis)
    player.player_control()
    player.update(dis)
    attacker1.draw((255,0,0), dis)
    attacker1.flash(dis)
    pyg.display.update()

    clock.tick(30)
pyg.quit()
quit()
