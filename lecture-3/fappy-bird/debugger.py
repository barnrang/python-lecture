import pygame

import config

load_font = pygame.font.Font("assets/THSarabunNew_Bold.ttf", config.FONT_SIZE)


def show_key_press(game_display, key):
    text = load_font.render("Key {} is being pressed".format(key), True, config.RED, config.BLACK)
    text_rect = text.get_rect()
    text_rect.center = (config.WIDTH // 2, config.HEIGHT // 2)
    game_display.blit(text, text_rect)

def show_tex(game_display, text):
    text = load_font.render(text, True, config.RED, config.BLACK)
    text_rect = text.get_rect()
    text_rect.center = (config.WIDTH // 2, config.HEIGHT // 2)
    game_display.blit(text, text_rect)
