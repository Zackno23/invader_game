'''
9/25
後で変数名等リファクタリングが必要

'''

import pygame
from pygame.locals import *

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("インベーダーゲーム")
screen.fill((0, 0, 0))

player = pygame.image.load("player.png")
playerX = 100
playerY = 200


running = True

while running:
    screen.blit(player, (playerX, playerY))
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                playerX += 1
                screen.fill((255, 0, 0))
            if event.key == K_LEFT:
                screen.fill((0, 255, 0))
            if event.key == K_UP:
                screen.fill((0, 0, 255))
            if event.key == K_DOWN:
                screen.fill((0, 0, 0))
    pygame.display.update()
