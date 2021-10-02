'''
10/1
pygame.key.get_pressedでの移動まで
[]playerがはみ出ないようにする
[]enemyの移動
[]enemyがはみ出ないように
[]弾を発射させる

'''

import pygame
from pygame.locals import *

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("インベーダーゲーム")
screen.fill((0, 0, 0))

player = pygame.image.load("player.png")
enemy = pygame.image.load("enemy.png")

playerX = 200
playerY = 100

enemyX = 100
enemyY = 200

running = True

while running:
    screen.fill((0, 0, 0))
    key_presseed = pygame.key.get_pressed()
    if key_presseed[K_RIGHT]:
        playerX += 1
    if key_presseed[K_LEFT]:
        playerX -= 1
    screen.blit(player, (playerX, playerY))
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        # if event.type == KEYDOWN:
        #     if event.key == K_RIGHT:
        #         screen.fill((255, 0, 0))
        #     if event.key == K_LEFT:
        #         screen.fill((0, 255, 0))
        #     if event.key == K_UP:
        #         screen.fill((0, 0, 255))
        #     if event.key == K_DOWN:
        #         screen.fill((0, 0, 0))
    pygame.display.update()
