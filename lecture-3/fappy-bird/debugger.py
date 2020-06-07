import pygame

import config

load_font = pygame.font.Font("assets/THSarabunNew_Bold.ttf", config.FONT_SIZE)


def show_key_press(game_display, key):
    text = load_font.render(f"Key {key} is being pressed", True, config.RED, config.BLACK)
    text_rect = text.get_rect()
    text_rect.center = (config.WIDTH // 2, config.HEIGHT // 2)
    game_display.blit(text, text_rect)
