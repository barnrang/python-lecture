import pygame

import config

SPF = 1 / config.FPS

class Bird:
    x = config.WIDTH / 4
    y = config.HEIGHT / 2
    dy = 0
    
    def __init__(self):
        self.image = pygame.transform.scale(pygame.image.load('assets/bird.png'), (config.LOAD_BIRD_WIDTH, config.LOAD_BIRD_HEIGHT))

    def update(self):
        self.dy += config.GRAVITY * SPF
        self.y += self.dy * SPF

    def jump(self):
        self.dy = -config.JUMP_SPEED

    def render(self, game_display):
        game_display.blit(self.image, (self.x, self.y))
