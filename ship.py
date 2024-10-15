import pygame as pg
from globals import *

class Ship(pg.sprite.Sprite):
    def __init__(self, groups, image = pg.Surface((TILE_SIZE,TILE_SIZE)), position = (SCREENWIDTH/2-TILE_SIZE/2,SCREENHEIGHT/2-300)):
        super().__init__(groups)
        self.image = image
        self.image.fill(SHIP_COLOR)
        self.rect = self.image.get_rect(topleft = position)

    def update(self):
        self.rect.y += 0.5
#        self.move()

    def move_right(self):
        self.rect.x += 1
    def move_left(self):
        self.rect.x -= 1
    def move_up(self):
        self.rect.y -= 2

#    def move(self):
#        keys = pg.key.get_pressed()
#        if keys[pg.K_d]:
#            self.move_right()
#        if keys[pg.K_a]:
#            self.move_left()
#        if keys[pg.K_w]:
#            self.move_up()

    def on_screen(self) ->bool:
        return self.rect.x > 0 and self.rect.x < SCREENWIDTH and self.rect.y >SCREENHEIGHT

    def get_mask(self):
        return pg.mask.from_surface(self.image)
    
    def check_in_display(self):
        return self.rect.x > 0 and self.rect.x < SCREENWIDTH-TILE_SIZE and self.rect.y > 0 and self.rect.y < SCREENHEIGHT