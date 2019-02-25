import pygame
import time
from gMenu import Menu
import Easter_egg

games = open('list.games', 'r').read().split()

for name in games:
    exec(f'from g{name} import {name}')

pygame.init()
size = width, height = 600, 610
color = (0, 0, 0)
screen = pygame.display.set_mode(size)
running = True
pause = Menu.Pause(screen)
old_time = time.time()
t_game = Menu(screen)
screen = pygame.display.set_mode(t_game.size)

while running:
    screen.fill((158, 173, 134))
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if t_game.game and not pause.pause:
            name = t_game.action(pygame.key.get_pressed())

        if pygame.key.get_pressed()[pygame.K_ESCAPE] and t_game.__class__.__name__ != 'Menu':
            pause.pause = not pause.pause

        if pause.pause:
            name = pause.action(pygame.key.get_pressed())

    if t_game.game and time.time() - old_time > t_game.speed and not pause.pause:
        old_time = time.time()
        t_game.motion()
        
    if name:
        if name == 'restart':
            name = t_game.__class__.__name__

        exec(f't_game = {name}(screen)')
        screen = pygame.display.set_mode(t_game.size)
        name = ''

    t_game.render()
    
    pause.render()
    pygame.display.flip()


pygame.quit()
