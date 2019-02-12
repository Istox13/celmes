from boards.tetris_board import Tetris_board
import random
from data import figure
import pygame

class Tetris:
    def __init__(self, screen):
        self.status = ''
        self.game = True
        self.score = 0
        self.lvl = self.score // 10
        width_tetris, height_tetris = 20, 10
        self.t_figure, self.t_figure_code = self.get_figure()
        self.new_figure, self.new_figure_code = self.get_figure()
        self.screen = screen
        self.board = Tetris_board(screen, 0, width_tetris, height_tetris) 
        self.print_in(self.t_figure, self.board)


    def get_figure(self):
        return figure.coords_init(figure.fs[random.randint(0, 6)], 0)


    def get_status(self):
        return self.game


    def game_over(self, board):
        self.game = False
        self.status = 'Game Ower'


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

        for n, i in enumerate(ms[::]):
            if sum(i) == board.width:
                ms.pop(n)
                ms = [[0 for _ in range(board.width)]] + ms
                self.score += 1
                red = True

        if red:
            board.set_board(ms)

        self.t_figure, self.t_figure_code = self.new_figure, self.new_figure_code
        self.new_figure, self.new_figure_code = self.get_figure()
        self.print_in(self.t_figure, self.board)

    def render(self):
        self.board.render()

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
        