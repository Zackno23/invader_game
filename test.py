
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

bulletX = playerX + (player.get_width() - bullet.get_width()) / 2
bulletY = playerY - bullet.get_height()

running = True
shoot = False

bullet_speed = 1

while running:
    screen.fill((0, 0, 0))
    screen.blit(player, (playerX, playerY))
    screen.blit(enemy, (enemyX, enemyY))

    key_press = pygame.key.get_pressed()

    if key_press[K_RIGHT]:
        if playerX < 800 - player.get_width():
            playerX += 1
    if key_press[K_LEFT]:
        if playerX > 0:
            playerX -= 1
    if shoot == True:
        if bulletY <= 0:
            shoot = False
            bulletY = bulletY = playerY - bullet.get_height()
        else:
            bulletY -= bullet_speed
            screen.blit(bullet, (bulletX, bulletY))
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                bulletX = playerX + (player.get_width() - bullet.get_width()) / 2
                shoot = True

    pygame.display.update()
