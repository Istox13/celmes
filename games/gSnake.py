import pygame
from boards.olds_board import gBoard
import random

class gSnake:
    def __init__(self, screen):
        self.status = ''
        self.game = True
        self.speed = 1
        self.score = 0
        self.lvl = 1
        self.screen = screen

        self.board = gBoard(self.screen, 0, 20, 20)
        self.snake = list()
    