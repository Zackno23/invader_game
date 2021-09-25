
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

playerX = 200
playerY = 100

enemyX = 100
enemyY = 200

running = True

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            print("a")
            if event.key == K_RIGHT:
                print("b")
                screen.fill((255, 0, 0))
            if event.key == K_LEFT:
                print("c")
                screen.fill((0, 255, 0))
            if event.key == K_UP:
                print("d")
                screen.fill((0, 0, 255))
            if event.key == K_DOWN:
                print("e")
                screen.fill((0, 0, 0))
    pygame.display.update()


