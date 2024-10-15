import pygame as pg
from globals import *
import random

class Entity(pg.sprite.Sprite):
    def __init__(self, groups, image=pg.Surface((TILE_SIZE,TILE_SIZE)), position = (0,0)):
        super().__init__(groups)
        self.image = image
        self.image.fill('grey')
        self.rect = self.image.get_rect(topleft = position)

    def update(self):
        pass
    
    def check_collisions(self,ship):
        ship_mask = ship.get_mask()
        self_mask = pg.mask.from_surface(self.image)

        offset = (self.rect.x - ship.rect.x, self.rect.y - ship.rect.y)

        if ship_mask.overlap(self_mask, offset):
            return True
        
        return False


class Land(Entity):
    def __init__(self, groups, image=pg.Surface(((TILE_SIZE)*(SCREENWIDTH/TILE_SIZE),TILE_SIZE)), position = (0,SCREENHEIGHT-TILE_SIZE)):
        super().__init__(groups, image, position)
        self.image = image
        self.image.fill('grey')
        self.rect = self.image.get_rect(topleft = position)

    def crash_landed(self,ship):
        ship_mask = ship.get_mask()
        self_mask = pg.mask.from_surface(self.image)

        offset = (self.rect.x - ship.rect.x, self.rect.y - ship.rect.y)

        if ship_mask.overlap(self_mask, offset):
            return True
        
        return False


class Platform(Entity):
    def __init__(self, groups, image=pg.Surface((TILE_SIZE*2,TILE_SIZE/4)), position = (random.randint(0,(SCREENWIDTH-TILE_SIZE-TILE_SIZE*2)),(SCREENHEIGHT-TILE_SIZE*2)+(TILE_SIZE/4)*3)):
        super().__init__(groups, image, position)
        self.image = image
        self.image.fill('green')
        self.rect = self.image.get_rect(topleft = position)

    def soft_landed(self,ship):
        ship_mask = ship.get_mask()
        self_mask = pg.mask.from_surface(self.image)

        offset = (self.rect.x - ship.rect.x, self.rect.y - ship.rect.y)

        if ship_mask.overlap(self_mask, offset):
            return True
        
        return False