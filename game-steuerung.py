import pygame
import sys

#Farben
GRAY = (159, 163, 168)
BLUE = (0, 0, 255)

# Initialisierung
pygame.init()
screen = pygame.display.set_mode((800,600), pygame.RESIZABLE)
clock = pygame.time.Clock()
dx = 0
# dy = 0
playerX = 400
playerY = 560

#Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:  # Taste wurde gedrückt
            if event.key == pygame.K_RIGHT:
                dx = 4
            elif event.key == pygame.K_LEFT:
                dx = -4
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                dx = 0
            elif event.key == pygame.K_RIGHT:
                dx = 0
    screen.fill(GRAY)
    # draw the Player
    player = pygame.Rect(playerX, playerY, 40, 40 )
    pygame.draw.rect(screen,BLUE, player,2)
    # move player
    playerX += dx
    pygame.display.update()
    clock.tick(60)
