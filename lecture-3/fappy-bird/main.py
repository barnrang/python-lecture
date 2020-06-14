import pygame
# Initialize pygame
pygame.init()

# import our files
import config
from bird import Bird
from pipes import Pipe, Pipes
from monitor import Monitor
import debugger

# Set game window the config width and height
game_display = pygame.display.set_mode((config.WIDTH, config.HEIGHT))
pygame.display.set_caption('Flappy bird')

clock = pygame.time.Clock()

# Contain state
game_quit = False
space_press = False
count = 0

while not game_quit:

    # Catch input from user
    for event in pygame.event.get():

        # If user press exit
        if event.type == pygame.QUIT:
            game_quit = True

        # If user press down a key
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                space_press = True

        # If user release a key
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                space_press = False

        print(event)

    # Display Black Screen
    game_display.fill(config.BLACK)

    # Display message if space is being pressed
    # See more in debugger.py
    if space_press:
        debugger.show_key_press(game_display, "space")

    # Update display after render
    pygame.display.update()
    count = (count + 1) % (2 * config.FPS)

    # For control constant Frames Per Second
    clock.tick(config.FPS)

