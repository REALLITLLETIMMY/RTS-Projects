import pygame

pygame.init()
FPS = 169
WIDTH = 800
HEIGHT = 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
while True:
    for i in pygame.event.get():
        print(i)
    pygame.display.update()
    clock.tick(FPS)
