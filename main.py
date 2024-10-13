import pygame as pg
import neat
import pickle

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
    
    def run(self):

        while self.running:
            self.update()
            self.draw()
        self.close()

    def update(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False

        self.scene.update()

        pg.display.update()
        self.clock.tick(FPS)

    def draw(self):
        self.scene.draw()

    def close(self):
        pg.quit()
        sys.exit()

def eval_genomes(genomes, config):
    pass


def run(config_file):
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         config_file)

    p = neat.Population(config)

    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)
    winner = p.run(eval_genomes, 50)

    print('\nBest genome:\n{!s}'.format(winner))


if __name__ == "__main__":
    game = Game()
    game.run()