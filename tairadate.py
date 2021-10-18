"""
10月２０日
[] enemyを表示
[] bulletをロード
[]弾を表示
    ※　while直下に書く
    bulletX = playerX + (player.get_width() - bullet.get_width()) / 2
    bulletY = playerY - bullet.get_height()
    screen.blit(bullet、(bulletX, bulletY))
[]スペースキーを押したときのif文に入れる（一瞬だけ表示）
[]弾が移動する処理を入れる（bullet_speed定数にする）
[]連射昨日の説明（リスト）
[]変数bullet_list作成
    for i in bullet_list:
        screen.blit(bullet, i)
        enemy_centerX, enemy_centerY = enemyX + enemy.get_width() / 2, enemyY + enemy.get_height() / 2
        bullet_centerX, bullet_centerY = i[0] + bullet.get_width() / 2, i[1] + bullet.get_height() / 2
        distance = math.sqrt(math.pow(enemy_centerX - bullet_centerX, 2) + math.pow(enemy_centerY - bullet_centerY, 2))
        if distance <= 30 or i[1] <= 0:
            bullet_list.remove(i)
        else:
            i[1] -= bullet_speed



"""
import pygame
from pygame.locals import *

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("インベーダーゲーム")
screen.fill((0, 0, 0))

player = pygame.image.load("player.png")
playerX = 800 / 2 - player.get_width() / 2
playerY = 500

running = True

while running:
    screen.fill((0, 0, 0))
    screen.blit(player, (playerX, playerY))

    # 押されたキーを調べる
    key_pressed = pygame.key.get_pressed()
    # 左が押されたとき
    if key_pressed[K_LEFT]:
        if playerX > 0:
            playerX -= 0.1
    # 右が押されたとき
    if key_pressed[K_RIGHT]:
        if playerX < 800 - player.get_width():
            playerX += 0.1

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False


    pygame.display.update()
