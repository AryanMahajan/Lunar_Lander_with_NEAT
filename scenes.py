import pygame as pg
from globals import *
from sprite import Land, Platform
from ship import Ship

class Scene:
    def __init__(self, game):
        self.game = game
        self.sprites = pg.sprite.Group()
        self.entity = []
        self.entity.append(Land([self.sprites]))
        self.entity.append(Platform([self.sprites]))

        self.ship = Ship([self.sprites])

    def update(self):
        self.sprites.update()
        
    def draw(self,land,platform,ship):
        self.game.screen.fill(BACKGROUND_COLOR)
        self.sprites.draw(self.game.screen)
    
        # Optionally, you can separately draw the land, platform, and ship if needed
        self.game.screen.blit(land.image, land.rect)
        self.game.screen.blit(platform.image, platform.rect)
        self.game.screen.blit(ship.image, ship.rect)