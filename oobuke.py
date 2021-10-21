'''
10/1
pygame.key.get_pressedでの移動まで

[]screen.fill((0, 0, 0))の追加
    移動ができるようになるが、弾が一瞬できえる
[]bulletX bulletYの定義
    まずはwhileの外で
[]while文のplayer, enemyの下にbulletのblit文を入れる
[]shoot変数を作成 スペースキーが押されたときの処理にTrueにする
[]if shoot == True:のステートメントを作る for文の前
    bulletをblit
[]bullet_speed = 1 として、↑のif文でbulletY -= bullet_speed
    連射できない 一発しか打てない
    bulletXが変わらない

[]連射できない
    弾が上の端っこまで行ったら、
    ・shootをFalseに戻す
    ・bulletYをもとに戻す
[]bulletXが変わらない
    spaceが押されたときのところに移動



[]enemyがはみ出ないように
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
bullet = pygame.image.load("bullet.png")

playerX = 400 - player.get_width() / 2
playerY = 500

enemyX = 400 - player.get_width() / 2
enemyY = 100

running = True

while running:

    screen.blit(player, (playerX, playerY))
    screen.blit(enemy, (enemyX, enemyY))
    # screen.blit(bullet,(playerX+ player.get_width() / 2 - bullet.get_width()/2,playerY- bullet.get_height()))

    key_press = pygame.key.get_pressed()

    if key_press[K_RIGHT]:
        if playerX < 800 - player.get_width():
            playerX += 0.1
    if key_press[K_LEFT]:
        if playerX > 0:
            playerX -= 0.1

    screen.blit(player, (playerX, playerY))
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                screen.blit(bullet,
                            (playerX + player.get_width() / 2 - bullet.get_width() / 2, playerY - bullet.get_height()))

    pygame.display.update()
