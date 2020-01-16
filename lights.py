import pygame as pyg
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



player = Player()
attacker1 = Attacker()
clock = pyg.time.Clock()

game_over = False
while not game_over:
    for event in pyg.event.get():
        if event.type==pyg.QUIT:
            game_over = True
    


    dis.fill(black)
    player.draw(dis)
    player.player_control()
    player.update(dis)
    attacker1.draw(dis)
    pyg.display.update()

    clock.tick(30)
pyg.quit()
quit()
