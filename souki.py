'''
<<<<<<< HEAD
9/25
後で変数名等リファクタリングが必要
[]条件分岐からplayerを動かす
[]連続して描画されちゃう問題の解決（screen.fillの場所）
[]pygame.key.get_pressed()でのプレイヤー操作
[]移動速度の調整と、初期位置の調整(playerY = 500くらい enemyY 150くらい？)
[]画面内から出ていってしまう問題の解決
[]敵の表示・移動（左右のみ➛近づいてくる）
=======
10 / 9

1:弾があたったときの処理
    ぶつかったのを判定する
    敵の位置を初期位置に戻す
    fireをfalseにする
2:連射機能
3:発射音とか爆発音






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
連打による処理低下の
'''
import math

import pygame
from pygame.locals import *

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("インベーダーゲーム")
screen.fill((0, 0, 0))

player = pygame.image.load("player.png")
enemy = pygame.image.load("enemy.png")
bullet = pygame.image.load("bullet.png")

player_X = 400 - player.get_width() / 2
player_Y = 500

enemy_X = 400 - enemy.get_width() / 2
enemy_Y = 200

# 弾の位置
bullet_X = player_X + player.get_width() / 2 - bullet.get_width() / 2
bullet_Y = player_Y - bullet.get_height()

running = True
fire = False

direction = 0.3

hit_number = 0
while running:
    screen.fill((0, 0, 0))
    if enemy_Y >= player_Y:
        enemy_Y = 200
    if enemy_X >= 800 or enemy_X <= 0:
        enemy_Y += enemy.get_height()
        direction *= -1
    enemy_X += direction

    key_pressed = pygame.key.get_pressed()
    if key_pressed[K_RIGHT]:
        if player_X < 800 - player.get_width():
            player_X += 1

    if key_pressed[K_LEFT]:
        if player_X > 0:
            player_X -= 1

    screen.blit(player, (player_X, player_Y))
    screen.blit(enemy, (enemy_X, enemy_Y))

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                if not fire:
                    bullet_X = player_X + player.get_width() / 2 - bullet.get_width()
                    fire = True

    if fire:
        screen.blit(bullet, (bullet_X, bullet_Y))
        bullet_Y -= 0.5
        if bullet_Y <= 0:
            bullet_X = player_X + player.get_width() / 2 - bullet.get_width() / 2
            bullet_Y = player_Y - bullet.get_height()
            fire = False

        enemy_centerX = enemy_X + enemy.get_width() / 2
        enemy_centerY = enemy_Y - enemy.get_height() / 2

        bullet_centerX = bullet_X + bullet.get_width() / 2
        bullet_centerY = bullet_Y - bullet.get_height() / 2

        if math.sqrt(math.pow(enemy_centerX - bullet_centerX, 2) + math.pow(enemy_centerY - bullet_centerY, 2)) <= 150:
            hit_number += 1
            print(hit_number)

    pygame.display.update()
