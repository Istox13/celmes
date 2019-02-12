import pygame
import os
import time


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)  
    
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    
    image = image.convert_alpha()
    return image


pygame.init()
size = width, height = 600, 300
screen = pygame.display.set_mode(size)
running = True

all_sprites = pygame.sprite.Group()
sprite = pygame.sprite.Sprite()
sprite.image = load_image("arrow.png")
sprite.rect = sprite.image.get_rect()
all_sprites.add(sprite)

x, y = sprite.rect.size
sprite.rect.x, sprite.rect.y = -x, 0
v = 200
n = time.time()
old_time = time.time()



while running:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False


    tm = time.time()
    if (tm - old_time) >= 2 * (v ** -1) and sprite.rect.x < 0:
        old_time = tm
        sprite.rect.x += 2

    screen.fill((0, 0, 255))
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()
