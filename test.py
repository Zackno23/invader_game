'''
授業前テスト用ファイル
'''


9/25
後で変数名等リファクタリングが必要
[]条件分岐からplayerを動かす
[]連続して描画されちゃう問題の解決（screen.fillの場所）
[]pygame.key.get_pressed()でのプレイヤー操作
[]移動速度の調整と、初期位置の調整
[]画面内から出ていってしまう問題の解決
[]敵の表示・移動（左右のみ➛近づいてくる）

import pygame
from pygame.locals import *

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("インベーダーゲーム")


player = pygame.image.load("player.png")
enemy = pygame.image.load("enemy.png")

playerX = 200
playerY = 100

enemyX = 100
enemyY = 200

running = True

while running:
    screen.fill((0, 0, 0))
    screen.blit(player, (playerX, playerY))
    screen.blit(enemy, (enemyX, enemyY))
    key_pressed = pygame.key.get_pressed()

    # playerの動き
    if key_pressed[K_LEFT] and playerX > 0:
        playerX -= 1
    if key_pressed[K_RIGHT] and playerX < 800 - player.get_width():
        playerX += 1

    # enemyの動き

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        # if event.type == KEYDOWN:
            # if event.key == K_RIGHT:
            #     playerX += 10
            # if event.key == K_LEFT:
            #     playerX -= 10

    pygame.display.update()


