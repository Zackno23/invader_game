'''
9/25
後で変数名等リファクタリングが必要

'''

import pygame
from pygame.locals import *
import math

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("インベーダーゲーム")
screen.fill((0, 0, 0))

player = pygame.image.load("player.png")
enemy = pygame.image.load("enemy.png")
bullet = pygame.image.load("bullet.png")

playerX = 400
playerY = 500
enemyX = 100
enemyY = 200
bullet_list = []


# 略
running = True

while running:
    screen.fill((0, 0, 0))
    screen.blit(player, (playerX, playerY))
    screen.blit(enemy, (enemyX, enemyY))
    for i in bullet_list:
        screen.blit(bullet, i)
        if i[1] <= 0:
            bullet_list.remove(i)
            continue
        enemy_centerX, enemy_centerY = enemyX + enemy.get_width()/2, enemyY + enemy.get_height() / 2
        bullet_centerX, bullet_centerY = i[0] + bullet.get_width()/2, i[1] + bullet.get_height() / 2
        # 三平方の定理
        distance = math.sqrt(math.pow(enemy_centerX - bullet_centerX, 2) + math.pow(enemy_centerY - bullet_centerY, 2))
        print(distance)
        if distance <= 30:
            bullet_list.remove(i)
        i[1] -= 0.1



    # 現在押されているキーをリストで返す
    key_pressed = pygame.key.get_pressed()
    # 右キーが押されたとき
    if key_pressed[K_RIGHT]:
        playerX += 0.1
    if key_pressed[K_LEFT]:
        playerX -= 0.1
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                bulletX = playerX + (player.get_width() - bullet.get_width()) / 2
                bulletY = playerY - bullet.get_height()
                bullet_list.append([bulletX, bulletY])


    pygame.display.update()
