'''
9/25
後で変数名等リファクタリングが必要

'''
import sys

import pygame
from pygame.locals import *

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("インベーダーゲーム")
screen.fill((0, 0, 0))

player = pygame.image.load("player.png")

enemy = pygame.image.load("enemy.png")
tekitou_surface = pygame.Surface((32, 32))
tekitou_surface.fill((255, 255, 255))

playerX = 200
playerY = 100
enemyX = 100
enemyY = 200

# 略
running = True

while running:
    screen.fill((0, 0, 0))

    screen.blit(player, (playerX, playerY))
    screen.blit(enemy, (enemyX, enemyY))
    screen.blit(tekitou_surface, (screen.get_width()/2, screen.get_height()/2))

    # 現在押されているキーをリストで返す
    key_pressed = pygame.key.get_pressed()
    # 右キーが押されたとき
    if key_pressed[K_RIGHT] == 1:
        playerX += 1
    # 左キーが押されたとき
    if key_pressed[K_LEFT] == 1:
        playerX -= 1
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    pygame.display.update()
