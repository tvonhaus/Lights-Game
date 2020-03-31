import pygame as pyg
import time
import random
from player import Player 
from attacker import Attacker

# --- constants --- 
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
attack_timer = 1100

# -- display --
pyg.init()
dis_width = 800
dis_height = 600
dis = pyg.display.set_mode((dis_width,dis_height))
dis_rect = dis.get_rect()
pyg.display.set_caption('Lights')

# -- objects -- 
player = Player()
attacker1 = Attacker()
clock = pyg.time.Clock()
current_time = pyg.time.get_ticks()

# -- events -- 
spawn_attacker_event = pyg.USEREVENT + 1
flash_attacker_event = pyg.USEREVENT + 2
finish_flash_event = pyg.USEREVENT + 3

# -- timers --
pyg.time.set_timer(spawn_attacker_event, attack_timer)

game_over = False
while not game_over:
    for event in pyg.event.get():
        print(event)
        if event.type == pyg.QUIT:
            game_over = True
        elif event.type == spawn_attacker_event:
            new_x , new_y, attacker_x, attacker_y = attacker1.spawn_attacker() 
            attacker1.rect = (new_x,new_y,attacker_x,attacker_y)
            flash_timer = 500
            pyg.time.set_timer(flash_attacker_event, flash_timer)
        elif event.type == flash_attacker_event:
            attacker1.update_color(white)
            attacker1.draw(attacker1.color,dis)
            pyg.time.set_timer(finish_flash_event,500)
        elif event.type == finish_flash_event:
            attacker1.update_color(red)
            attacker1.draw(attacker1.color,dis) 

    # -- updates --
    dis.fill(black)
    player.draw(dis)
    player.player_control()
    player.update(dis)
    attacker1.draw(attacker1.color,dis)
    pyg.display.update()
    current_time = pyg.time.get_ticks()
    # print(current_time)
    clock.tick(60)

pygame.quit()
quit()
