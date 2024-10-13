import pygame as pg
from globals import *

class Entity(pg.sprite.Sprite):
    def __init__(self, groups, image=pg.Surface((TILE_SIZE,TILE_SIZE)), position = (0,0)):
        super().__init__(groups)
        self.image = image
        self.rect = self.image.get_rect(topleft = position)