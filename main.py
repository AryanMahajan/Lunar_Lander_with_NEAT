import pygame as pg
import neat
import pickle
import os

import sys
from globals import *
from scenes import Scene
from game import Game



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

    score = 0

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
            ge[x].fitness -= 0.6
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
                ge[x].fitness += 0.008


        for ship in ships:
            if game.crash_landing_condition() or not game.scene.ship.check_in_display() or pg.key.get_pressed()[pg.K_q]:
                ge[ships.index(ship)].fitness -= 1
                nets.pop(ships.index(ship))
                ge.pop(ships.index(ship))
                ships.pop(ships.index(ship))
            if game.soft_landing_conditions() and game.scene.ship.check_in_display():
                for genome in ge:
                    genome.fitness += 5
                score +=1
                    
        game.draw(ships=ships)
        pg.display.flip()


        if score > 25:
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
    winner = p.run(eval_genomes)

    print('\nBest genome:\n{!s}'.format(winner))


if __name__ == "__main__":
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config-feedforward.txt')
    run(config_path)