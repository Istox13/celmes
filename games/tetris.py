import pygame
from boards.olds_board import gBoard
import random
from data import figure
import time
from gTetris import Tetris
from gSnake import Snake


pygame.init()
size = width, height = 600, 610
color = (0, 0, 0)
screen = pygame.display.set_mode(size)
running = True
old_time = time.time()
t_game = Snake(screen)
screen = pygame.display.set_mode(t_game.get_size())

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
    pygame.display.flip()

pygame.quit()
