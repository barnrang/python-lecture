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
pygame.display.set_caption('Flappy napat')

clock = pygame.time.Clock()

# Contain state
game_quit = False
space_press = False
death = False
bird_in = False
count = 0

# Instances
bird = Bird()
pipes = Pipes()

'''
Catch Event <---
|              |
Update         |
|              |
Render --------

'''
# Game Loop
while not game_quit:

    # Catch input from user
    for event in pygame.event.get():

        # If user press exit
        if event.type == pygame.QUIT:
            game_quit = True

        # If user press down a key
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird.jump()
                space_press = True

            if event.key == pygame.K_k:
                death = True

        # If user release a key
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                space_press = False

        print(event)


    # Update

    if not death:
        bird.update()
        pipes.update()

        # If bird hit the world
        # Upper 0 lower config.HEIGHT
        bird_y = bird.y
        if bird_y < 0:
            death = True
        elif bird_y + config.LOAD_BIRD_HEIGHT > config.HEIGHT:
            death = True

        # Check if bird in or out
        pipes_list = pipes.pipes
        bird_in = False
        for pipe in pipes_list:
            pipe_x = pipe.x
            bird_l_x = bird.x
            bird_r_x = bird.x + config.LOAD_BIRD_WIDTH
            if pipe_x + config.LOAD_PIPE_WIDTH > bird_r_x > pipe_x or \
                    pipe_x + config.LOAD_PIPE_WIDTH > bird_l_x > pipe_x:
                bird_in = True

        if bird_in:
            pass
            ## check_hit_ceiling(bird)


    # Display Black Screen
    game_display.fill(config.BLACK)

    # Render bird
    bird.render(game_display)
    pipes.render(game_display)

    # Display message if space is being pressed
    # See more in debugger.py
    if bird_in:
        debugger.show_tex(game_display, "Bird in")
    else:
        debugger.show_tex(game_display, "Bird out")

    # if space_press:
    #     debugger.show_key_press(game_display, "space")

    # Update display after render
    pygame.display.update()
    count = (count + 1) % (2 * config.FPS)

    # Add more pipe
    # FPS 60 -> 2 second 120 (120 count)
    if count == 0:
        pipes.add_pipe()

    # For control constant Frames Per Second
    clock.tick(config.FPS)

