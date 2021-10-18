'''
10月２０日平舘用　弾発射機能

player_speed, bullet_speed, enemy_speedの変数を追加


'''

import pygame
from pygame.locals import *
import math

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("インベーダーゲーム")
screen.fill((0, 0, 0))
# 画像をロード
player = pygame.image.load("player.png")

enemy = pygame.image.load("enemy.png")

tekitou_surface = pygame.Surface((32, 32))
tekitou_surface.fill((255, 255, 255))

bullet = pygame.image.load("bullet.png")


# player, enemyの初期位置
playerX = 400
playerY = 500
enemyX = 100
enemyY = 200

# 発射されている弾のリスト
bullet_list = []

# スピード
player_speed = 0.1
enemy_speed = 0.1
bullet_speed = 0.1

running = True

while running:
    # 画面の初期化・player, enemyの表示
    screen.fill((0, 0, 0))

    screen.blit(player, (playerX, playerY))
    screen.blit(enemy, (enemyX, enemyY))
    screen.blit(tekitou_surface, (screen.get_width()/2, screen.get_height()/2))


    # bullet_listをもとに弾を表示
    for i in bullet_list:
        screen.blit(bullet, i)
        # 弾が画面外に出たとき
        if i[1] <= 0:
            bullet_list.remove(i)
            continue
        # 当たり判定を設定するために、中央の座標を取得
        enemy_centerX, enemy_centerY = enemyX + enemy.get_width() / 2, enemyY + enemy.get_height() / 2
        bullet_centerX, bullet_centerY = i[0] + bullet.get_width() / 2, i[1] + bullet.get_height() / 2
        # 三平方の定理　・・・モンテカルロ法の話
        distance = math.sqrt(math.pow(enemy_centerX - bullet_centerX, 2) + math.pow(enemy_centerY - bullet_centerY, 2))

        # 当たり判定を調整
        if distance <= 30 or i[1] <= 0:
            bullet_list.remove(i)
        else:
            i[1] -= bullet_speed

    # 現在押されているキーをリストに保存
    key_pressed = pygame.key.get_pressed()
    # 右キーが押されたとき


    if key_pressed[K_RIGHT]:
        playerX += player_speed
    if key_pressed[K_LEFT]:
        playerX -= player_speed

    # イベント取得
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            # スペースキーが押されたとき
            if event.key == K_SPACE:
                bulletX = playerX + (player.get_width() - bullet.get_width()) / 2
                bulletY = playerY - bullet.get_height()
                bullet_list.append([bulletX, bulletY])

    pygame.display.update()
