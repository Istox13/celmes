import pygame
from bords.tetris_board import Tetris_board as Board

pygame.init()
size = width, height = 600, 800
a, b = 20, 10
color = (0, 0, 0)
screen = pygame.display.set_mode(size)
board = Board(a, b, screen, color) 
running = True


while running:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.K_DOWN:
            

    board.render()
    pygame.display.flip()

pygame.quit()
