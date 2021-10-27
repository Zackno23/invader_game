"""
10月２０日
[] bulletをロード
[]弾を表示
    ※　whileの外に書く
    bulletX = playerX + (player.get_width() - bullet.get_width()) / 2
    bulletY = playerY - bullet.get_height()
    screen.blit(bullet、(bulletX, bulletY))
[]スペースキーを押したときのif文に入れる（一瞬だけ表示）
[]shoot をTrue にしたら発射する
    この時点では機体が移動しても弾が移動しない
[]bulletXの宣言をwhile内部に入れる
    発射前はついて来るけど、発射した後もついてきてしまう。
[]if event.key == K_spaceのところに↑の宣言を入れる
    一発しか打てない・最初から弾が表示されてしまう
[]二発目が打てるようにifを入れる
    if shoot:
        bulletY -= .1
        # 移動
        screen.blit(bullet,(bulletX, bulletY))
        if bulletY <= 0:
            shoot = False
            bulletY = playerY - bullet.get_height()
            bulletX = playerX + (player.get_width() - bullet.get_width()) / 2
[]bullet_speed定数にする
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
bullet = pygame.image.load("bullet.png")
enemy = pygame.image.load("enemy.png")

playerX = 800 / 2 - player.get_width() / 2
playerY = 500

bulletX = playerX + (player.get_width() - bullet.get_width()) / 2
bulletY = playerY - bullet.get_height()

enemyX = 400
enemyY = 100

running = True
bullet_speed = 0.5
shoot = False
bullet_list = []

while running:
    print(bullet_list)
    screen.fill((0, 0, 0))

    screen.blit(player, (playerX, playerY))
    screen.blit(enemy, (enemyX, enemyY))


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

    # if shoot == True:
    #     bulletY -= bullet_speed
    #     screen.blit(bullet, (bulletX, bulletY))
    #     if bulletY <= 0:
    #         shoot = False
    #         bulletY = playerY - bullet.get_height()
    #
    if bullet_list:
        for i in bullet_list:
            screen.blit(bullet, i)
            i[1] -= bullet_speed
            if i[1] <= 0:
                bullet_list.remove(i)


    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                shoot = True
                bulletX = playerX + (player.get_width() - bullet.get_width()) / 2
                bullet_list.append([bulletX, bulletY])

    pygame.display.update()
