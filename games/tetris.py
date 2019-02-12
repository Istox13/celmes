import pygame
from boards.tetris_board import Tetris_board
import random
from data import figure
import time
from gTetris import Tetris


def score(screen):
    text = font.render(f'Score: {tet.score}', 1, (0, 0, 0))
    text_x = 3 * width // 4 - text.get_width() // 2
    text_y = 0.7 * height  - text.get_height() // 2
    screen.blit(text, (text_x, text_y))

    text = font.render(f'Level: {tet.lvl}', 1, (0, 0, 0))
    text_x = 3 * width // 4 - text.get_width() // 2
    text_y = 6 * height // 7 - text.get_height() // 2
    screen.blit(text, (text_x, text_y))

    text = font.render('Next', 1, (0, 0, 0))
    text_x = 3 * width // 4 - text.get_width() // 2
    text_y = height // 5 - text.get_height() // 2
    screen.blit(text, (text_x, text_y))

    if tet.status:
        screen.fill((158, 173, 134))
        text = font2.render(f'{tet.status}', 1, (0, 0, 0))
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
game = True
old_time = time.time()
tet = Tetris(screen)
#pygame.mouse.set_visible(False)



while running:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if tet.game:
            if pygame.key.get_pressed()[pygame.K_DOWN]:
                tet.down(tet.t_figure, tet.board)
            
            if pygame.key.get_pressed()[pygame.K_RIGHT]:
                tet.right(tet.t_figure, tet.board)

            if pygame.key.get_pressed()[pygame.K_LEFT]:
                tet.left(tet.t_figure, tet.board)
            
            if pygame.key.get_pressed()[pygame.K_UP]:
                tet.rotate(tet.t_figure, tet.board)
            
            if pygame.key.get_pressed()[pygame.K_SPACE]:
                tet.drop(tet.t_figure, tet.board)

    if tet.game and time.time() - old_time > 1:
        old_time = time.time()
        tet.down(tet.t_figure, tet.board)
        
        
    tet.render()
    score(screen)

    pygame.display.flip()

pygame.quit()
