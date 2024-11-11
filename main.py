import pygame as pg
pg.init()
screen=pg.display.set_mode((400,300))
while True:
    for event in pg.event.get():
        if event.type==pg.QUIT:
            pg.quit
    pg.draw.rect(screen,(0,0,255),pg.Rect(180,130,100,50))
    pg.display.flip()
