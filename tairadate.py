"""

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
    if key_pressed[K_UP]:

    if key_pressed[K_DOWN]:




        if playerX < 800 - player.get_width():
            playerX += 0.1

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False


    pygame.display.update()
