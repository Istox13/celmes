import pygame, sys
pygame.init()
class Sprite:
    def __init__(self, xpos, ypos, filename): 
        self.x = xpos
        self.y = ypos
        self.bitmap = pygame.image.load(filename)
        self.bitmap.set_colorkey((0,0,0)) 
    def render(self, screen):
        screen.blit(self.bitmap,(self.x,self.y))
 
class Menu:
    
    def __init__(self):
        self.punkts = [(265, 300, u'Help', (11, 0, 77)),
          (265, 340, 'Exit', (11, 0, 77)),
          (230, 150, u'CELMES', (255, 0, 0))]
        pygame.font.init()
        self.window = pygame.display.set_mode((610, 460))
        pygame.display.set_caption('CELMES')
        self.screen = pygame.Surface((610, 640))
    def render(self, screen, font):
        for i in self.punkts:
            self.screen.blit(font.render(i[2], 1, i[3]), (i[0], i[1]))
    def menu(self):
        pygame.display.set_caption('CELMES')
        done = True
        font_menu = pygame.font.Font(None, 50)
        punkt = 0
        tetr = Sprite(10, 10, 'data/tetris.png')
        snake = Sprite(10, 250, 'data/snake.png')
        maze = Sprite(400, 10, 'data/maze.png')
        cars = Sprite(400, 250, 'data/highway.png')
        while done:
            self.screen.fill((0, 100, 200))
            tetr.render(self.screen)
            snake.render(self.screen)
            maze.render(self.screen)
            cars.render(self.screen)
            self.render(self.screen, font_menu)
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                    if 210 > e.pos[0] > 10 and 210 > e.pos[1] > 10:
                        print(1)
                    if 210 > e.pos[0] > 10 and 450 > e.pos[1] > 250:
                        print(2)
                    if 315 > e.pos[0] > 265 and 350 > e.pos[1] > 300:
                        self.helpwindow()
                    if 315 > e.pos[0] > 265 and 400 > e.pos[1] > 350:
                        pygame.quit()
                        sys.exit()
                    if 600 > e.pos[0] > 400 and 210 > e.pos[1] > 10:
                        print(3)
                    if 600 > e.pos[0] > 400 and 450 > e.pos[1] > 250:
                        print(4)
            self.window.blit(self.screen, (0, 0))
            pygame.display.flip()

    def helpwindow(self):
        helpw = pygame.Surface((610, 460))
        pygame.display.set_caption('CELMES: HELP')
        helpw.fill((255, 255, 255))
        font = pygame.font.Font(None, 70)
        helpw.blit(font.render('Правила', 1, (0, 0, 0)), (200, 10))
        self.window.blit(helpw, (0, 0))
        pygame.display.update()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.menu()
                    break
        

if __name__ == '__main__':
    game = Menu()
    game.menu()
    pygame.quit()
