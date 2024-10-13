import pygame as pg
from globals import *
from sprite import Entity

class Scene:
    def __init__(self, game):
        self.game = game
        self.sprites = pg.sprite.Group()
        self.entity = Entity([self.sprites])

    def update(self):
        self.entity.rect.x +=1
        
    def draw(self):
        self.game.screen.fill('lightblue')
        self.sprites.draw(self.game.screen)