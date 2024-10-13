import pygame as pg
from globals import *
from sprite import Entity
from ship import Ship

class Scene:
    def __init__(self, game):
        self.game = game
        self.sprites = pg.sprite.Group()
        self.entity = []
        self.entity.append(Entity([self.sprites]))
        self.entity.append(Entity([self.sprites],position=(200,200)))

        self.ship = Ship([self.sprites],position = (SCREENWIDTH/2-TILE_SIZE/2,SCREENHEIGHT/2-300))

    def update(self):
        self.sprites.update()
        
    def draw(self):
        self.game.screen.fill(BACKGROUND_COLOR)
        self.sprites.draw(self.game.screen)