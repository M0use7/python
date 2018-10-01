"""__author__ = 唐宏进 """
import pygame
from my_color import *
from random import randint

# 玩家球的属性
x = 200
y = 300
x_speed = 1
y_speed = 1
flag = True

WINDOW_WIDTH = 400 # 屏幕宽度
WINDOW_HEIGHT = 600 # 屏幕高度

key_ball_color = 'ball_color'
key_ball_center = 'ball_center'




# 初始化游戏
pygame.init()
window = pygame.display.set_mode((400, 600))
window.fill(gray)
pygame.display.flip()

# 游戏循环
while True:

    key_pressed = pygame.key.get_pressed()
    if key_pressed[pygame.K_w] or key_pressed[pygame.K_UP]:
        y += y_speed*-1
    if key_pressed[pygame.K_s] or key_pressed[pygame.K_DOWN]:
        y += y_speed
    if key_pressed[pygame.K_d] or key_pressed[pygame.K_RIGHT]:
        x += x_speed
    if key_pressed[pygame.K_a] or key_pressed[pygame.K_LEFT]:
        x += x_speed*-1

    window.fill(gray)
    pygame.draw.circle(window, yellow, (x, y), 15)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN and flag:
            print(event.key)

            if event.key == pygame.K_UP:
                y += y_speed*-1
            if event.key == pygame.K_DOWN:
                y += y_speed
            if event.key == pygame.K_RIGHT:
                x += x_speed
            if event.key == pygame.K_LEFT:
                x += x_speed*-1
        if event.type == pygame.KEYUP:
            flag = False