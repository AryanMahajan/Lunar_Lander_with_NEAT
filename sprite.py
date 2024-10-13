import pygame as pg
from globals import *

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


class Platform(Entity):
    def __init__(self, groups, x, y, width, height,color=(255, 255, 255), image=None, collision=True):
        super().__init__(groups, image=image, position=(x, y))
        self.image = pg.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.collision = collision



class Lunar_Land(Entity):
    pass