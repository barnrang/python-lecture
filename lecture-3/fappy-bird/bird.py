import pygame

import config

# Second Per Frame
SPF = 1 / config.FPS


class Bird:

    def __init__(self):
        self.x = config.WIDTH / 4
        self.y = config.HEIGHT / 2
        self.dy = 0
        #self.image = pygame.image.load('assets/bird.png')
        self.image = pygame.transform.scale(pygame.image.load('assets/bird.png'), (config.LOAD_BIRD_WIDTH,
                                                                                   config.LOAD_BIRD_HEIGHT))

    def update(self):
        # TODO
        self.y += self.dy * SPF
        self.dy += config.GRAVITY * SPF

    def reset(self):
        # TODO
        pass

    def jump(self):
        # TODO
        self.dy = -config.JUMP_SPEED

    def render(self, game_display):
        '''
        Load image
        |
        blit (display to screen)
        '''

        game_display.blit(self.image, (self.x, self.y))
