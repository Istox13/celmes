import time
import pygame

class Menu:

    class Pause:
        def __init__(self, screen):
            self.font = pygame.font.Font(None, 50)
            self.screen = screen
            self.pause = False
            self.t_pos = 0
            self.sound = True
        
        def render(self):
            if self.pause:
                width, height = self.screen.get_size()

                t0 = (width * 0.25, height * 0.75)
                t1 = (width * 0.25, height * 0.25)
                t2 = (width * 0.75, height * 0.25)
                t3 = (width * 0.75, height * 0.75)
                pygame.draw.polygon(self.screen, (158, 173, 134), [t0, t1, t2, t3], 0)
                
                text1 = self.font.render('Exit to menu', 1, (0, 0, 0))
                text1_x = width * 0.5 - text1.get_width() // 2
                text1_y = height * 0.25 + (height * 0.5 // 3) // 2 - text1.get_height() // 2
                self.screen.blit(text1, (text1_x, text1_y))

                status = ('OFF' if self.sound else 'ON')
                text2 = self.font.render(f'Sound {status}', 1, (0, 0, 0))
                text2_x = width * 0.5 - text2.get_width() // 2
                text2_y = height * 0.5 - text2.get_height() // 2
                self.screen.blit(text2, (text2_x, text2_y))

                text3 = self.font.render(f'Restart', 1, (0, 0, 0))
                text3_x = width * 0.5 - text3.get_width() // 2
                text3_y = height * 0.75 - (height * 0.5 // 3) // 2 - text2.get_height() // 2
                self.screen.blit(text3, (text3_x, text3_y))
                
                n = str(self.t_pos + 1)
                exec(f'self.t_1 = (text{n}_x, text{n}_y + text{n}.get_height())')
                exec(f'self.t_2 = (text{n}_x + text{n}.get_width(), text{n}_y + text{n}.get_height())')
                pygame.draw.line(self.screen, (0, 0, 0), self.t_1, self.t_2, 4)


            

        def action(self, keys):
            if keys[pygame.K_DOWN]:
                self.t_pos = (self.t_pos + 1) % 3
            
            if keys[pygame.K_UP]:
                self.t_pos = (self.t_pos - 1) % 3
            
            if keys[pygame.K_RETURN]:
                if self.t_pos == 2:
                    self.pause = False
                    self.t_pos = 0
                    return 'restart'

                elif self.t_pos == 0:
                    self.pause = False
                    return 'Menu'

                elif self.t_pos == 1:
                    if self.sound:
                        pygame.mixer.music.set_volume(0)
                    else:
                        pygame.mixer.music.set_volume(0.5)
                    
                    self.sound = not self.sound
                


        def set_screen(self, screen):
            self.screen = screen


    def __init__(self, screen, games=open('list.games', 'r').read().split()):
        self.screen = screen
        self.games = games
        self.t_pos = 1
        self.speed = 1
        self.game = True
        self.logo = pygame.image.load('data/logo.png')
        screen.fill((255, 255, 255))
        screen.blit(self.logo, (-50, 70))
        pygame.display.flip()
        time.sleep(3)
        pygame.mixer.music.set_volume(0)
        self.init_sound()
        font = pygame.font.Font(None, 300)
        max_w = max([font.render(name, 1, (0, 0, 0)).get_width() for name in self.games])
        self.size = self.width, self.height = max_w + 40, 800
    

    def init_sound(self):
        self.sound_enter = pygame.mixer.Sound('data/sounds/g_tetris_drop.wav')
        self.sound_move = pygame.mixer.Sound('data/sounds/g_tetris_move.wav')

    def motion(self):
        pass

    def render(self):
         
        def get_gms(t_pos):
            games_3 = self.games * 3
            t_pos += len(self.games)
            return games_3[t_pos - 1:t_pos + 2]

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
            self.sound_move.play()
        
        if keys[pygame.K_UP]:
            self.t_pos = (self.t_pos - 1) % len(self.games)
            self.render()
            self.sound_move.play()
        
        if keys[pygame.K_RETURN]:
            self.sound_enter.play()
            time.sleep(0.5)
            return self.games[self.t_pos]

