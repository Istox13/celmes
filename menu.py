import pygame
import time

games = ['Tetris']

for name in games:
    exec(f'from games.g{name} import {name}')

def init_game(name):
    global t_game, screen
    t_game = exec(f'{name}(screen)')

class Menu:
    def __init__(self, screen, games):
        self.screen = screen
        self.games = games
        self.t_pos = 1
        self.size = self.width, self.height = 1800, 1000

    def render(self):
        def get_gms(t_pos):
            games_3 = self.games * 3
            t_pos += len(self.games)
            return games_3[t_pos:t_pos + 3]

        prop = (self.height - 441) // 8
        widths = list()
        
        for n, name in enumerate(get_gms(self.t_pos)):

            font = pygame.font.Font(None, 170 if n != 1 else 300)
            text = font.render(name, 1, (0, 0, 0))
            text_x = 0
            text_y = (2 + n) * prop + sum([0, 117 + prop, 207 + prop][:n + 1]) * (n > 0)
            widths.append(text.get_width())
            self.screen.blit(text, (text_x, text_y))
        
        pygame.draw.line(self.screen, (0, 0, 0), (700, 0), (700, self.height), 1)

    def action(self, keys):
        if keys[pygame.K_DOWN]:
            self.t_pos = (self.t_pos + 1) % len(self.games)
            self.render()
            time.sleep(0.3)
        
        if keys[pygame.K_UP]:
            self.t_pos = (self.t_pos - 1) % len(self.games)
            self.render()
            time.sleep(0.3)
        
        if keys[pygame.K_KP_ENTER]:
            return self.games[self.t_pos]




pygame.init()
size = width, height = 600, 610
color = (0, 0, 0)
screen = pygame.display.set_mode(size)
running = True
old_time = time.time()
t_game = Menu(screen, games)
screen = pygame.display.set_mode(t_game.size)

while running:
    screen.fill((158, 173, 134))
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
        
    n = t_game.action(pygame.key.get_pressed())
    
    if n:
        self.t_game = init_game(n)

    t_game.render()
    pygame.display.flip()

pygame.quit()
