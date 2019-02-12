import pygame

class Tetris_board:
    def __init__(self, screen, color_key=0, height=20, width=10, left=10, cell_size=30, top=10, 
                zaliv=True):
        self.zaliv = zaliv
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = left
        self.top = top
        self.cell_size = cell_size
        self.screen = screen
        self.color = (0, 0, 0)

    def get_size(self):
        return self.width, self.height
 
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def set_board(self, board):
        self.board = board
    
    def get_board(self):
        return self.board
    
    def get_value(self, x, y):
        return self.board[y][x]
    
    def set_value(self, x, y, value):
        self.board[y][x] = value

    def render(self):
        if self.zaliv:
            self.screen.fill((158, 173, 134))
        n = 4
        for i in range(self.height):
            for j in range(self.width):
                color = self.color if self.board[i][j] != 0 else (135, 147, 114)
                
                for v in range(2): 
                    if not v:
                        
                        loc = (self.left + j * self.cell_size - n + 5,
                               self.top + i * self.cell_size - n + 5)
                        size = [self.cell_size - n - 10] * 2
                    else:
                        loc = (self.left + j * self.cell_size - n,
                               self.top + i * self.cell_size - n )
                        size = [self.cell_size - n] * 2
                    pygame.draw.rect(self.screen, color, (loc, size), v * 3)