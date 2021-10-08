'''
10 / 9
[]弾の発射
    ロード
    ブリット
[]連続で弾を撃てるようにするには
[]まずはenemyを止めながらやってみよう
[]弾表示の仕組み
    弾の座標をリストに格納
    リスト全体に移動の処理をする
    リスト全体をの座標情報を元に描画（blit）
    弾がenemyにぶつかっていないかチェック
        ぶつかったらリストから削除
        三平方の定理・・・モンテカルロ法の話
    リストの中で一番最初の要素が画面外に行っていないかチェック
        画面外だったらリストから削除
    continueについての説明
[]enemyを動かして動作チェック
[]得点機能追加

＜時間があれば＞
連打による処理低下の防ぎ方
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
    enemyX += direction

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

    pygame.display.update()
