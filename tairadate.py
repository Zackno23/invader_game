'''
9/25
<<<<<<< HEAD
[]後で変数名等リファクタリングが必要
[]screen.blit()の使い方を確認 引数の設定
[]playerの移動
[]eventを使った移動
[]押しっぱなしの処理
    []playerの移動
    []enemyの移動
[]たまの移動
=======
後で変数名等リファクタリングが必要
9/29
１時間目：blitの説明まで→ifによる上下左右への動き
2時間目：上下左右の移動→押しっぱなし処理
コミットすることを教える
>>>>>>> d08327b37622457c1372f47ff287890eff37de4c
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
    screen.fill((0, 0, 0))
    screen.blit(player, (playerX, playerY))
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
<<<<<<< HEAD
                screen.fill((255, 0, 0))
            if event.key == K_LEFT:
                screen.fill((0, 255, 0))
            if event.key == K_UP:
                screen.fill((0, 0, 255))
            if event.key == K_DOWN:
                screen.fill((0, 0, 0))
=======
                playerX += 1
                # screen.fill((255, 0, 0))
            if event.key == K_LEFT:
                playerX -= 1
                # screen.fill((0, 255, 0))
            if event.key == K_UP:
                playerY -= 1
                # screen.fill((0, 0, 255))
            if event.key == K_DOWN:
                playerY += 1
                # screen.fill((0, 0, 0))
>>>>>>> d08327b37622457c1372f47ff287890eff37de4c
    pygame.display.update()
