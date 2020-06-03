import pygame

# import our files
import config
from bird import Bird
from pipes import Pipe, Pipes
from monitor import Monitor

pygame.init()

game_display = pygame.display.set_mode((config.WIDTH, config.HEIGHT))
pygame.display.set_caption('Flappy bird')

clock = pygame.time.Clock()

crashed = False
hit = False

bird = Bird()
pipes = Pipes()
monitor = Monitor()

count = 0

while not crashed:

    if count == 0:
        pipes.add_pipe()
        pipes.clean_pipe()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("yooo")
                bird.jump()

        print(event)

    game_display.fill(config.BLACK)


    if not hit:
        bird.update()
        pipes.update()
        hit = monitor.check_collision(bird, pipes)
        monitor.check_score(bird, pipes)

    bird.render(game_display)
    pipes.render(game_display)
    monitor.render(game_display)

    pygame.display.update()
    clock.tick(config.FPS)

    count = (count + 1) % (2 * config.FPS)