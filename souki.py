
'''
9/25
後で変数名等リファクタリングが必要
・条件分岐からplayerを動かす
・pygame.key.get_pressed()でのプレイヤー操作
・移動速度の調整と、初期位置の調整
・画面内から出ていってしまう問題の解決
・敵の表示・移動（左右のみ➛近づいてくる）
'''

import pygame
from pygame.locals import *

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("インベーダーゲーム")
screen.fill((0, 0, 0))


player = pygame.image.load("player.png")
enemy = pygame.image.load("enemy.png")

playerX = 400 - player.get_width() / 2
playerY = 500

enemyX = 400 - enemy.get_width() / 2
enemyY = 200

running = True

direction = 1
while running:
    screen.fill((0, 0, 0))
    if enemyY >= playerY:
        enemyY = 200
    if enemyX >= 800 or enemyX <= 0:
        enemyY += enemy.get_height()
        direction *= -1
    enemyX +=  direction

    key_pressed = pygame.key.get_pressed()
    if key_pressed[K_RIGHT]:
        if playerX < 800 - player.get_width():
            playerX += 1

    if key_pressed[K_LEFT]:
        if playerX > 0:
            playerX -= 1


    screen.blit(player, (playerX, playerY))
    screen.blit(enemy, (enemyX, enemyY))
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        # if event.type == KEYDOWN:
        #     if event.key == K_RIGHT:
        #         screen.fill((255, 0, 0))
        #         playerX += 3
        #     if event.key == K_LEFT:
        #         screen.fill((0, 255, 0))
        #         playerX -= 3

    pygame.display.update()


