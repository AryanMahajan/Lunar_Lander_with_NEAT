import pygame as pg
import neat
import pickle
import os

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
    
    def draw(self):
        self.scene.draw(land=self.scene.entity[0], platform=self.scene.entity[1], ship=self.scene.ship)

    def close(self):
        pg.quit()
        sys.exit()



def eval_genomes(genomes, config):
    gen = 0
    game = Game()
    win = game.screen
    gen = gen + 1
    nets = []
    ships = []
    ge = []

    for _, genome in genomes:
        genome.fitness = 0  # start with fitness level of 0
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        nets.append(net)
        ships.append(game.scene.ship)
        ge.append(genome)

    land = game.scene.entity[0]
    platform = game.scene.entity[1]

    clock = pg.time.Clock()

    run = True

    while run and len(ships) > 0:
        clock.tick(FPS)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
                pg.quit()
                quit()
                break

        for x, ship in enumerate(ships):  # give each ship a fitness of 0.1 for each frame it stays alive
            ge[x].fitness += 0.1
            ship.update()
           
            output = nets[x].activate((ship.rect.x, ship.rect.y, land.rect.x, land.rect.y,platform.rect.x, platform.rect.y))

            if output[0] > 0.5:
                ship.move_right()
                ge[x].fitness += 0.1
            if output[1] > 0.5:
                ship.move_left()
                ge[x].fitness += 0.1
            if output[2] > 0.5:
                ship.move_up()
                ge[x].fitness += 0.02


        for ship in ships:
                if game.crash_landing_condition():
                    ge[ships.index(ship)].fitness -= 1
                    nets.pop(ships.index(ship))
                    ge.pop(ships.index(ship))
                    ships.pop(ships.index(ship))
                if game.soft_landing_conditions():
                    for genome in ge:
                        genome.fitness += 5
                    
        game.draw()
        pg.display.flip()


        if gen > 25:
            pickle.dump(nets[0],open("best.pickle", "wb"))
            break      


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
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config-feedforward.txt')
    run(config_path)