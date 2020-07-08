import pygame as pyg
import time
import random
from player import Player 
from attacker import Attacker
from beam import Beam

# --- constants --- 
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
attacker_timer = 1500
attacker_flag = 0
shoot_timer = 0


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
shot = Beam()
clock = pyg.time.Clock()
current_time = pyg.time.get_ticks()

# -- events -- 
spawn_attacker_event = pyg.USEREVENT + 1
attacker_shoot_event = pyg.USEREVENT + 2
# flash_attacker_event = pyg.USEREVENT + 2
# finish_flash_event = pyg.USEREVENT + 3

# -- timers --
pyg.time.set_timer(spawn_attacker_event, attacker_timer)

game_over = False
while not game_over:
    if (attacker1.beamTimer == 0) and (attacker1.flag == 1):
        print("shoot")
        attacker1.flag = 0
    for event in pyg.event.get():
        print(event)
        if event.type == pyg.QUIT:
            game_over = True
        elif event.type == spawn_attacker_event:
            new_x , new_y = attacker1.spawn_attacker() 
            attacker1.rect = (new_x,new_y,attacker1.x,attacker1.y)
            # flash_timer = 500
            # pyg.time.set_timer(flash_attacker_event, flash_timer)
        # elif event.type == flash_attacker_event:
        #     attacker1.update_color(white)
        #     attacker1.draw(attacker1.color,dis)
        #     pyg.time.set_timer(finish_flash_event,500)
        # elif event.type == finish_flash_event:
        #     attacker1.update_color(red)
        #     attacker1.draw(attacker1.color,dis) 

    # -- updates --
    dis.fill(black)

    # Player Update
    player.draw(dis)
    player.player_control()
    player.update(dis)

    #Attacker Update
    attacker1.draw(attacker1.color,dis)
    if(attacker1.beamTimer > 0):
        attacker1.beamTimer -= 10
    
    

    pyg.display.update()
    clock.tick(60)

pyg.quit()
quit()
