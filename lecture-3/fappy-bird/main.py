from enum import Enum

import pygame

# import our files
import config
from bird import Bird
from pipes import Pipe, Pipes
from monitor import Monitor


class GameState(Enum):
    NOT_START = 1
    PLAYING = 2
    CRASH = 3
    RESET = 4
    QUIT = 5


pygame.init()

game_display = pygame.display.set_mode((config.WIDTH, config.HEIGHT))
pygame.display.set_caption('Flappy bird')

clock = pygame.time.Clock()

crashed = False
game_state = GameState.NOT_START

bird = Bird()
pipes = Pipes()
monitor = Monitor()

count = 0

while game_state != GameState.QUIT:

    if game_state == GameState.RESET:
        bird.reset()
        pipes.reset()
        monitor.reset()
        count = 0
        game_state = GameState.NOT_START

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_state = GameState.QUIT
            continue

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("yooo")
                bird.jump()

                if game_state == GameState.NOT_START:
                    game_state = GameState.PLAYING
                    count = 0

            # Press R to reset
            if game_state == GameState.CRASH and event.key == pygame.K_r:
                game_state = GameState.RESET

        print(event)

    game_display.fill(config.BLACK)

    if game_state == GameState.PLAYING:

        # Add pipes and clean old ones
        if count == 0:
            pipes.add_pipe()
            pipes.clean_pipe()

        bird.update()
        pipes.update()
        if monitor.check_collision(bird, pipes):
            game_state = GameState.CRASH
        
        monitor.check_score(bird, pipes)

    bird.render(game_display)
    pipes.render(game_display)
    monitor.render(game_display)
    monitor.print_fps(game_display, clock)
    if game_state == GameState.CRASH:
        monitor.render_dead(game_display)

    pygame.display.update()

    count = (count + 1) % (2 * config.FPS)
    print(config.FPS)
    clock.tick(config.FPS)
