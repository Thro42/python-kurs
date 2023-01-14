import pygame
import sys

GRAY = (159, 163, 168)

# Initialisierung
pygame.init()
screen = pygame.display.set_mode((800,600), pygame.RESIZABLE)
clock = pygame.time.Clock()

#Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill(GRAY)
    pygame.display.update()
    clock.tick(60)
