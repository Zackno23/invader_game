'''
10/1
pygame.key.get_pressedでの移動まで
[]playerがはみ出ないようにする
[]enemyの移動
[]enemyがはみ出ないように
[]弾を発射させる

'''

import pygame
from pygame.locals import *

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("インベーダーゲーム")
screen.fill((0, 0, 0))

player = pygame.image.load("player.png")
enemy = pygame.image.load("enemy.png")

playerX = 100
playerY = 200

enemyX = 300
enemyY = 400



running = True

while running:
    screen.fill((0, 0, 0))
<<<<<<< HEAD
    screen.blit(player, (playerX, playerY))
    screen.blit(enemy, (enemyX, enemyY))
    
    key_press = pygame.key.get_pressed()

    if key_press[K_RIGHT]:
        playerX += 0.1
    if key_press[K_LEFT]:
        playerX -= 0.1


=======
    key_presseed = pygame.key.get_pressed()
    if key_presseed[K_RIGHT]:
        playerX += 1
    if key_presseed[K_LEFT]:
        playerX -= 1
    screen.blit(player, (playerX, playerY))
>>>>>>> 95429fbdc23f2fdd9626dadb775cad335949ba00
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        # if event.type == KEYDOWN:
<<<<<<< HEAD

            # if event.key == K_RIGHT:
            #     screen.fill((255, 0, 0))
            #     # playerX += 1
            # if event.key == K_LEFT:
            #     screen.fill((0, 255, 0))
            #     # playerX -=1
            # if event.key == K_UP:
            #     screen.fill((0, 0, 255))
            # if event.key == K_DOWN:
            #     print("e")
            #     screen.fill((0, 0, 0))
=======
        #     if event.key == K_RIGHT:
        #         screen.fill((255, 0, 0))
        #     if event.key == K_LEFT:
        #         screen.fill((0, 255, 0))
        #     if event.key == K_UP:
        #         screen.fill((0, 0, 255))
        #     if event.key == K_DOWN:
        #         screen.fill((0, 0, 0))
>>>>>>> 95429fbdc23f2fdd9626dadb775cad335949ba00
    pygame.display.update()
