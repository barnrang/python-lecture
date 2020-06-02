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

        self.y_low_hit = self.y_low
        self.y_high_hit = self.y_low - config.HOLE_WIDTH

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

    def check_collision(self, bird):
        if (bird.y < 0) or ((bird.y + config.LOAD_BIRD_HEIGHT) > config.HEIGHT):
            return True

        for pipe in self.pipes:
            if (bird.x < pipe.x < bird.x + config.LOAD_BIRD_WIDTH) or \
                (bird.x < (pipe.x + config.LOAD_PIPE_WIDTH) < bird.x + config.LOAD_BIRD_WIDTH):
                if (bird.y < pipe.y_high_hit) or ((bird.y + config.LOAD_BIRD_HEIGHT) > pipe.y_low_hit):
                    return True
        
        return False

    def render(self, game_display):
        for pipe in self.pipes:
            pipe.render(game_display)