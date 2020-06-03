import pygame

import config

class Monitor:
    
    def __init__(self):
        self.score = 0
        self.bird_enter_hole = False
        self.font = pygame.font.Font('assets/THSarabunNew_Bold.ttf', config.FONT_SIZE)

    def check_collision(self, bird, pipes):
        if self.__check_bird_hit_border(bird):
            return True

        for pipe in pipes.pipes:
            if self.__check_bird_in_pipe(bird, pipe):
                if self.__check_bird_hit_pipe(bird, pipe):
                    return True
        
        return False

    def check_score(self, bird, pipes):
        if self.bird_enter_hole:
            out_pipe = True
            for pipe in pipes.pipes:
                if self.__check_bird_in_pipe(bird, pipe):
                    out_pipe = False
                    break
            if out_pipe:
                self.bird_enter_hole = False
                self.score += 1

        else:
            for pipe in pipes.pipes:
                if self.__check_bird_in_pipe(bird, pipe):
                    self.bird_enter_hole = True
                    break


    def render(self, game_display):
        text = self.font.render(f"Score: {self.score}", True, config.RED, config.BLUE)
        text_rect = text.get_rect()
        text_rect.center = (7 * config.WIDTH // 8, config.HEIGHT // 8)

        game_display.blit(text, text_rect)

    def __check_bird_in_pipe(self, bird, pipe):
        return (pipe.x < bird.x < pipe.x + config.LOAD_PIPE_WIDTH) or \
                (pipe.x < (bird.x + config.LOAD_BIRD_WIDTH) < pipe.x + config.LOAD_PIPE_WIDTH)

    def __check_bird_hit_pipe(self, bird, pipe):
        return (bird.y < pipe.y_high_hit) or ((bird.y + config.LOAD_BIRD_HEIGHT) > pipe.y_low_hit)

    def __check_bird_hit_border(self, bird):
        return (bird.y < 0) or ((bird.y + config.LOAD_BIRD_HEIGHT) > config.HEIGHT)