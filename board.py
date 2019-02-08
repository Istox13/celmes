import pygame

class Board:
    def __init__(self, height, width, screen):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = 10
        self.top = 10
        self.cell_size = 30
        self.screen = screen
 
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self):
        for i in range(self.height):
            for j in range(self.width):
                loc = (self.left + j*self.cell_size,
                        self.top + i*self.cell_size)
                size = [self.cell_size]*2
                pygame.draw.rect(self.screen, (255, 0, 0), (loc, size), 1)

        


#pygame.init()
#size = width, height = 800, 600
#screen = pygame.display.set_mode(size)
#board = Board(10, 20, screen)
#running = True
#while running:
#    for event in pygame.event.get():
#        if event.type == pygame.QUIT:
#            running = False
#    screen.fill((0, 0, 0))
#    board.render()
#    pygame.display.flip()
#pygame.quit()

        

