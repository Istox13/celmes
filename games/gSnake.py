import pygame
from boards.olds_board import gBoard
import random

class Snake:

    def __init__(self, screen):
        self.status = ''
        self.game = True
        self.speed = 1
        self.score = -1
        self.lvl = 1
        self.screen = screen
        self.napr = (1, 0)
        self.init_sound()

        self.board = gBoard(self.screen, 0, 30, 30)
        self.snake = [(i, self.board.height - 1) for i in range(5)]
        self.new_point()
        


    def new_point(self):
        self.sound_drop.play()
        x, y = self.snake[-1]

        while (x, y) in self.snake:
            x = random.randint(0, self.board.width - 1)
            y = random.randint(0, self.board.height - 1)

        self.score += 1
        self.point = (x, y)


    def add_len(self):
        x, y = self.snake[0]
        x1, y1 = self.snake[1]
        x += x - x1
        y += y - y1
        
        return (x, y)


    def c_status(self):
        if not self.game:
            font = pygame.font.Font(None, 50)
            font2 = pygame.font.Font(None, 140)
            width, height = self.screen.get_size()

            self.screen.fill((158, 173, 134))

            text = font.render(f'Score: {self.score}', 1, (0, 0, 0))
            text_x =  width // 2 - text.get_width() // 2
            text_y =  (height // 2 - text.get_height() // 2) 
            self.screen.blit(text, (text_x, text_y))

            text = font2.render(f'{self.status}', 1, (0, 0, 0))
            text_x =  (width // 2 - text.get_width() // 2)
            text_y =  (height // 2 - text.get_height() // 2) // 2
            self.screen.blit(text, (text_x, text_y))

        
    def motion(self):
        if self.game:
            self.sound_move.play()
            for coords in self.snake:
                self.board.set_value(*coords, 0)

            self.snake.pop(0)
            self.snake.append(tuple([self.snake[-1][i] + self.napr[i] for i in range(2)]))

            if self.snake[-1] == self.point:
                self.new_point()
                self.snake = [self.add_len()] + self.snake

            for coords in self.snake:
                x, y = coords
                if not (0 <= x < self.board.width and 0 <= y < self.board.height) or \
                len(set(self.snake)) != len(self.snake):
                    self.game = False
                    self.status = 'GAME OVER'
                    self.sound_delit.play()
                    break
                self.board.set_value(*coords, 1)

        if self.score == 89:
            self.status = 'YOU WIN!'
            self.game = False


    def init_sound(self):
        self.sound_drop = pygame.mixer.Sound('data/sounds/g_tetris_drop.wav')
        self.sound_move = pygame.mixer.Sound('data/sounds/g_tetris_move.wav')
        self.sound_delit = pygame.mixer.Sound('data/sounds/g_tetris_delit.wav')
        '''music_file = 'data/sounds/g_tetris_play.mp3'

        freq = 44100     # audio CD quality
        bitsize = -16    # unsigned 16 bit
        channels = 2     # 1 is mono, 2 is stereo
        buffer = 2048    # number of samples (experiment to get right sound)
        pygame.mixer.init(freq, bitsize, channels, buffer)
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.set_num_channels(3)

        try:
            pygame.mixer.music.load(music_file)
        except pygame.error:
            print("File %s not found! (%s)" % (music_file, pygame.get_error()))
        self.sound_start.play()
        pygame.mixer.music.play(-1)'''


    def render(self):
        f'''Вызывается через {self.speed} секунд при self.game == True'''
        self.board.set_value(*self.point, 1)
        self.board.render()
        self.c_status()
    

    def get_size(self):
        return (910, 910) 

    
    def action(self, keys):
        if keys[pygame.K_DOWN] and self.napr != (0, -1):
            self.napr = (0, 1)
            self.motion()
        
        if keys[pygame.K_RIGHT] and self.napr != (-1, 0):
            self.napr = (1, 0)
            self.motion()

        if keys[pygame.K_LEFT] and self.napr != (1, 0):
            self.napr = (-1, 0)
            self.motion()
        
        if keys[pygame.K_UP] and self.napr != (0, 1):
            self.napr = (0, -1)
            self.motion()
        
        if keys[pygame.K_SPACE]:
            self.speed = 0.25
        else:
            self.speed = 1
        
