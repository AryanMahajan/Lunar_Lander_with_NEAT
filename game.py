import pygame as pg

import sys
from globals import *
from scenes import Scene


class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
        self.clock = pg.time.Clock()

        self.running = True
        self.scene = Scene(self)
    


    def update(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False

        self.scene.update()
#        self.crash_landing_condition()
#        self.soft_landing_conditions
#        self.collisions()

        pg.display.update()
        self.clock.tick(FPS)

    def collisions(self):
        entity = self.scene.entity
        ship = self.scene.ship
        for entities in entity:
            if entities.check_collisions(ship=ship):
                self.close()

    def soft_landing_conditions(self):
        entity_platform = self.scene.entity[1]
        ship = self.scene.ship
        if entity_platform.soft_landed(ship=ship):
            return True
        return False

    def crash_landing_condition(self):
        entity_land = self.scene.entity[0]
        ship = self.scene.ship
        if entity_land.crash_landed(ship = ship):
            return True
        return False
#    def run(self):
#
#        while self.running:
#            self.update()
#            self.draw()
#        self.close()
    
    def draw(self,ships):
        self.scene.draw(land=self.scene.entity[0], platform=self.scene.entity[1], ships=ships)

    def close(self):
        pg.quit()
        sys.exit()
