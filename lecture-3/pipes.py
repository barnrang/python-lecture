import random
import pygame

import config

SPF = 1 / config.FPS

upward_pipe = pygame.transform.scale(pygame.image.load('assets/pipe.png'), (config.LOAD_PIPE_WIDTH, config.LOAD_PIPE_HEIGHT))
downward_pipe = pygame.transform.flip(upward_pipe, False, True)

class Pipe:
    def __init__(self):
        self.y_low = random.randint(config.HOLE_WIDTH + config.MIN_SHOW, config.HEIGHT - config.MIN_SHOW)
        self.y_high = self.y_low - config.HOLE_WIDTH - config.LOAD_PIPE_HEIGHT
        self.x = config.WIDTH  

    def update(self):
        self.x -= config.PIPE_SPEED * SPF

    def render(self, game_display):
        game_display.blit(upward_pipe, (self.x, self.y_low))
        game_display.blit(downward_pipe, (self.x, self.y_high))



class Pipes:
    def __init__(self):
        self.pipes = []

    def add_pipe(self):
        self.pipes.append(Pipe())

    def clean_pipe(self):
        self.pipes = [pipe for pipe in self.pipes if pipe.x > -config.LOAD_PIPE_WIDTH]

    def update(self):
        for pipe in self.pipes:
            pipe.update()

    def render(self, game_display):
        for pipe in self.pipes:
            pipe.render(game_display)