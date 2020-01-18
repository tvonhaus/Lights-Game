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
attack_timer = 500


player = Player()
attacker1 = Attacker()
clock = pyg.time.Clock()

spawn_attacker_event = pyg.USEREVENT + 1

pyg.time.set_timer(spawn_attacker_event, attack_timer)

print(attacker1.rect)


game_over = False
while not game_over:
    for event in pyg.event.get():
        if event.type==pyg.QUIT:
            game_over = True
        elif event.type == spawn_attacker_event:
            new_x = 0
            new_y = 0
            attacker_x = 0
            attacker_y = 0
            wall = random.randint(0,3)
            if wall == 0:
                new_x = random.randint(100,700)
                new_y = 0
                attacker_x = 50
                attacker_y = 10
            elif wall == 1:
                new_x = 790
                new_y = random.randint(100,500)
                attacker_x = 10
                attacker_y = 50
            elif wall == 2:
                new_x = random.randint(100,700)
                new_y = 590
                attacker_x = 50
                attacker_y = 10
            elif wall == 3:
                new_x = 0
                new_y = random.randint(100,500)
                attacker_x = 10
                attacker_y = 50
            attacker1.rect = (new_x,new_y,attacker_x,attacker_y)


    dis.fill(black)
    player.draw(dis)
    player.player_control()
    player.update(dis)
    attacker1.draw(dis)
    pyg.display.update()

    clock.tick(30)
pyg.quit()
quit()
