import pygame
from boards.tetris_board import Tetris_board
import random
from data import figure
import time
from gTetris import Tetris


def print_information(screen, game):
    text = font.render(f'Score: {game.score}', 1, (0, 0, 0))
    text_x = 3 * width // 4 - text.get_width() // 2
    text_y = 0.7 * height  - text.get_height() // 2
    screen.blit(text, (text_x, text_y))

    text = font.render(f'Level: {game.lvl}', 1, (0, 0, 0))
    text_x = 3 * width // 4 - text.get_width() // 2
    text_y = 6 * height // 7 - text.get_height() // 2
    screen.blit(text, (text_x, text_y))

    if game.print_next:
        text = font.render('Next', 1, (0, 0, 0))
        text_x = 3 * width // 4 - text.get_width() // 2
        text_y = height // 5 - text.get_height() // 2
        screen.blit(text, (text_x, text_y))

    if game.status:
        screen.fill((158, 173, 134))
        text = font2.render(f'{game.status}', 1, (0, 0, 0))
        text_x =  width // 2 - text.get_width() // 2
        text_y =  height // 2 - text.get_height() // 2
        screen.blit(text, (text_x, text_y))




pygame.init()
size = width, height = 600, 610
color = (0, 0, 0)
screen = pygame.display.set_mode(size)
font = pygame.font.Font(None, 50)
font2 = pygame.font.Font(None, 140)
running = True
old_time = time.time()
t_game = Tetris(screen)


while running:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if t_game.game:
            t_game.action(pygame.key.get_pressed())

    if t_game.game and time.time() - old_time > t_game.speed:
        old_time = time.time()
        t_game.motion()

    t_game.render()
    print_information(screen, t_game)
    pygame.display.flip()

pygame.quit()
