from boards.olds_board import gBoard
import random
import pygame
import time


class Race:
    size = (600, 610)

    def __init__(self, screen):
        self.status = ''
        self.game = True
        self.speed = 1
        self.old_speed = 1
        self.score = 0
        self.lvl = 1
        self.print_next = False
        #self.init_sound()
        self.coords = [[4, 16], [3, 17], [4, 17], [5, 17], [4, 18], [3, 19], [5, 19]]
        self.screen = screen
        self.board = gBoard(screen)
        self.font = pygame.font.Font(None, 50)
        self.font2 = pygame.font.Font(None, 140)

        for i in range(0, 20, 2):
            self.board.set_value(0, i, 1)
            self.board.set_value(9, i, 1)

        for i in self.coords:
            self.board.set_value(i[0], i[1], 1)

        self.k = 0
        self.cars = []
    
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
        
    def motion(self):
        self.k += 1

        if self.k == 8:
            self.create_car()
            self.k = 0
            
        self.rdown()

        for i in range(20):
            self.board.set_value(0, i,
                                 abs(self.board.get_value(0, i) - 1))
            self.board.set_value(9, i,
                                 abs(self.board.get_value(9, i) - 1))


    def create_car(self):
        mx = random.randint(1, 6)
        coords = [[mx+1, 0], [mx, 1], [mx+1, 1], [mx+2, 1],
                  [mx+1, 2], [mx, 3], [mx+2, 3]]
        for i in coords:
            self.board.set_value(i[0], i[1], 1)
        self.cars.append(coords)


    def check(self):
        for i in self.cars:
            for j in self.coords:
                if j in i:
                    self.game_over(self.board)
        if self.score == 10 * self.lvl:
            self.lvl += 1
            self.speed *= 1 - (self.lvl - 1) * 0.1
        if self.score == 90:
            self.status = 'You win!'
            self.game = False


    def render(self):
        self.check()
        self.board.render()
        self.print_information()
        
        
    def action(self, keys):
        if keys[pygame.K_RIGHT]:
            self.right()
        if keys[pygame.K_LEFT]:
            self.left()
        if keys[pygame.K_SPACE] and 0.3 < self.speed:
            self.old_speed = self.speed
            self.speed = 0.3
        else:
            self.speed = self.old_speed


    def left(self):
        if self.coords[0][0] > 2:
            for i in self.coords:
                self.board.set_value(i[0], i[1], 0)
            for i in self.coords:
                i[0] -= 1
            for i in self.coords:
                self.board.set_value(i[0], i[1], 1)
        

    def right(self):
        if self.coords[0][0] < 7:
            for i in self.coords:
                self.board.set_value(i[0], i[1], 0)
            for i in self.coords:
                i[0] += 1
            for i in self.coords:
                self.board.set_value(i[0], i[1], 1)


    def rdown(self):
        for e in range(len(self.cars)):
            for i in range(len(self.cars[e])):
                if self.cars[e][i][1] <= 19:
                    car = self.cars[e][i]
                    self.board.set_value(car[0], car[1], 0)
                    car[1] = car[1] + 1
        if self.cars:
            if self.cars[0]:
                if self.cars[0][0][1] >= 17:
                    car = len(self.cars[0])
                    if car == 7:
                        del self.cars[0][5:]
                    if car == 5 or car == 1:
                        del self.cars[0][-1]
                    if car == 4:
                        del self.cars[0][1:]
            else:
                del self.cars[0]
                self.score += 1
        for car in self.cars:
            for i, j in car:    
                self.board.set_value(i, j, 1)


    def game_over(self, board):
        self.game = False
        self.status = 'GAME OVER'
                
