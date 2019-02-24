from boards.olds_board import gBoard
import random
from data import figure
import pygame


class Tetris:

    size = (600, 610) 
    def __init__(self, screen):
        self.status = ''
        self.game = True
        self.speed = 1
        self.score = 0
        self.lvl = 1
        self.print_next = True
        self.init_sound()
        self.font = pygame.font.Font(None, 50)
        self.font2 = pygame.font.Font(None, 140)

        width_tetris, height_tetris = 20, 10
        self.t_figure, self.t_figure_code = self.get_figure()
        self.new_figure, self.new_figure_code = self.get_figure()
        self.screen = screen
        self.next = gBoard(self.screen, 0, 4, 4, 400, 30, 150, zaliv=False)
        self.board = gBoard(screen, 0, width_tetris, height_tetris) 
        self.print_in(self.t_figure, self.board)
    

    def close(self):
        pygame.mixer.music.stop()

    def init_sound(self):
        self.sound_drop = pygame.mixer.Sound('data/sounds/g_tetris_drop.wav')
        self.sound_move = pygame.mixer.Sound('data/sounds/g_tetris_move.wav')
        self.sound_delit = pygame.mixer.Sound('data/sounds/g_tetris_delit.wav')
        self.sound_start = pygame.mixer.Sound('data/sounds/g_tetris_start.wav')
        self.sound_win = pygame.mixer.Sound('data/sounds/g_tetris_win.wav')
        music_file = 'data/sounds/g_tetris_play.mp3'

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
        pygame.mixer.music.play(-1)

    def get_figure(self):
        return figure.coords_init(figure.fs[random.randint(0, 6)], 0)

    def get_status(self):
        return self.game

    def print_information(self):
        width, height = self.screen.get_size()

        text = self.font.render(f'Score: {self.score}', 1, (0, 0, 0))
        text_x = 3 * width // 4 - text.get_width() // 2
        text_y = 0.7 * height  - text.get_height() // 2
        self.screen.blit(text, (text_x, text_y))

        text = self.font.render(f'Level: {self.lvl}', 1, (0, 0, 0))
        text_x = 3 * width // 4 - text.get_width() // 2
        text_y = 6 * height // 7 - text.get_height() // 2
        self.screen.blit(text, (text_x, text_y))

        if self.print_next:
            text = self.font.render('Next', 1, (0, 0, 0))
            text_x = 3 * width // 4 - text.get_width() // 2
            text_y = height // 5 - text.get_height() // 2
            self.screen.blit(text, (text_x, text_y))

        if self.status:
            self.screen.fill((158, 173, 134))
            text = self.font2.render(f'{self.status}', 1, (0, 0, 0))
            text_x =  width // 2 - text.get_width() // 2
            text_y =  height // 2 - text.get_height() // 2
            self.screen.blit(text, (text_x, text_y))

    def action(self, keys):
        if keys[pygame.K_DOWN]:
            self.sound_move.play()
            self.down(self.t_figure, self.board)
        
        if keys[pygame.K_RIGHT]:
            self.sound_move.play()
            self.right(self.t_figure, self.board)

        if keys[pygame.K_LEFT]:
            self.sound_move.play()
            self.left(self.t_figure, self.board)
        
        if keys[pygame.K_UP]:
            self.rotate(self.t_figure, self.board)
        
        if keys[pygame.K_SPACE]:
            self.sound_drop.play()
            self.drop(self.t_figure, self.board)

    def game_over(self, board):
        self.game = False
        self.status = 'GAME OVER'

    def motion(self):
        self.sound_move.play()
        self.down(self.t_figure, self.board)

    def print_in(self, coords, board): 
        for x, y in coords:
            if board.get_value(x, y) == 1:
                self.game_over(board)
                break
        else:
            for x, y in coords:
                board.set_value(x, y, 1)

    def new_round(self, board):
        ms = board.get_board()
        red = False
        self.speed = 1 - (self.lvl - 1) * 0.1

        for n, i in enumerate(ms[::]):
            if sum(i) == board.width:
                ms.pop(n)
                ms = [[0 for _ in range(board.width)]] + ms
                self.score += 1
                self.lvl = self.score // 10 + 1
                red = True

        if self.score == 105:
            self.status = 'You win!'
            self.game = False
            pygame.mixer.music.stop()
            self.sound_win.play()

        if red:
            board.set_board(ms)
            self.sound_delit.play()
        
        
        self.t_figure, self.t_figure_code = self.new_figure, self.new_figure_code
        self.new_figure, self.new_figure_code = self.get_figure()
        self.print_in(self.t_figure, self.board)
        self.next.set_board(self.new_figure_code[0][0])

    def render(self):
        self.board.render()
        self.next.render(0)
        self.next.set_board(self.new_figure_code[0][0])
        self.print_information()

    def down(self, coords, board):
        for x, y in coords:
            board.set_value(x, y, 0)

        for i, coord in enumerate(coords):
            x, y = coord

            if y == board.height - 1 or board.get_value(x, y + 1) == 1:
                self.print_in(coords, board)
                self.new_round(board)
                return coords, False
        
        for i, coord in enumerate(coords):
            x, y = coord
            coords[i] = (x, y + 1)

        self.print_in(coords, board)
        
        return coords, True


    def right(self, coords, board):
        for x, y in coords:
            board.set_value(x, y, 0)

        for i in coords: 
            if i[0] >= board.get_size()[0] - 1 or board.get_value(i[0] + 1, i[1]) == 1:
                self.print_in(coords, board)
                return coords 
        
        
        for i, coord in enumerate(coords):
            x, y = coord
            coords[i] = (x + 1, y)

        self.print_in(coords, board)
        
        return coords


    def left(self, coords, board):
        for x, y in coords:
            board.set_value(x, y, 0)

        for i in coords: 
            if i[0] <= 0 or board.get_value(i[0] - 1, i[1]) == 1:
                self.print_in(coords, board)
                return coords 

        for x, y in coords:
            board.set_value(x, y, 0)
        
        for i, coord in enumerate(coords):
            x, y = coord
            coords[i] = (x - 1, y)

        self.print_in(coords, board)
        
        return coords


    def rotate(self, coords, board):
        ms_fig, n = self.t_figure_code

        x, y = 0, 0
        for i in self.t_figure:
            x += i[0]
            y += i[1]
        x //= len(self.t_figure)
        y //= len(self.t_figure)

        new_coords, new_code = figure.coords_init(ms_fig, (n + 1) % len(ms_fig), x, y)

        for x, y in coords:
            board.set_value(x, y, 0)

        for i in new_coords: 
            if (0 > i[0]) or (i[0] > (board.get_size()[0] - 1)) or (board.get_value(i[0], i[1]) == 1) or (0 >= i[1]) or (i[1] > (board.get_size()[1] - 1)):
                self.print_in(coords, board)
                return coords 
        
        self.print_in(new_coords, board)
        self.t_figure, self.t_figure_code = new_coords, new_code 
        return new_coords


    def drop(self, coords, board):
        flag = self.down(coords, board)[1]
        while flag:
            flag = self.down(coords, board)[1]
        
        