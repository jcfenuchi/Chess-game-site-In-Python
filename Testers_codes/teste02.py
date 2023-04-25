"""Move an image with the mouse."""

import pygame
from pygame.locals import *

RED = (255, 0, 0)
GRAY = (150, 150, 150)


pygame.init()
w, h = 800, 800
screen = pygame.display.set_mode((w, h))
running = True


img = pygame.transform.scale(pygame.image.load('images/pieces/black/Rook.png'),(50,50))
img.convert()
rect = img.get_rect()
#rect.center = w//2, h//2
moving = False

board = pygame.transform.scale(pygame.image.load("images/board/chess board.jpg"),(800,800))

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        elif event.type == MOUSEBUTTONDOWN:
            if rect.collidepoint(event.pos):
                moving = True

        elif event.type == MOUSEBUTTONUP:
            moving = False

        elif event.type == MOUSEMOTION and moving:
            rect.move_ip(event.rel)
    
    screen.blit(board,(0,0))
    screen.blit(img, rect)
    pygame.draw.rect(screen, RED, rect, 1)
    pygame.display.update()

pygame.quit()