import pygame

# import our files
import config
from bird import Bird
from pipes import Pipe, Pipes

pygame.init()

game_display = pygame.display.set_mode((config.WIDTH, config.HEIGHT))
pygame.display.set_caption('Flappy bird')

clock = pygame.time.Clock()

white = (255, 255, 255)
black = (0, 0, 0)

crashed = False
hit = False

bird = Bird()
pipes = Pipes()

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

    game_display.fill(black)


    if not hit:
        bird.update()
        pipes.update()
        hit = pipes.check_collision(bird)

    bird.render(game_display)
    pipes.render(game_display)

    pygame.display.update()
    clock.tick(config.FPS)

    count = (count + 1) % (2 * config.FPS)