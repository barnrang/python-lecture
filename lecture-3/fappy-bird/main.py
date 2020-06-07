import pygame
pygame.init()

# import our files
import config
from bird import Bird
from pipes import Pipe, Pipes
from monitor import Monitor
import debugger

game_display = pygame.display.set_mode((config.WIDTH, config.HEIGHT))
pygame.display.set_caption('Flappy bird')

clock = pygame.time.Clock()
game_quit = False
space_press = False
count = 0

while not game_quit:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_quit = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                space_press = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                space_press = False

        print(event)
    # Display Contents
    game_display.fill(config.BLACK)
    if space_press:
        debugger.show_key_press(game_display, "space")

    pygame.display.update()
    clock.tick(config.FPS)

    count = (count + 1) % (2 * config.FPS)
