"""__author__ = 唐宏进 """
import pygame
from math import sqrt
from random import randint
pygame.init()
window = pygame.display.set_mode((400,600))
window.fill((255,255,255))
pygame.display.flip()

x = 200
y = 200
x1 = 100
y1 = 100
add1 = 1
add2 = 2
add3 = 3
add4 = 4
while True:
    pygame.time.delay(5)
    window.fill((255, 255, 255))
    pygame.draw.circle(window, (0, 255, 0), (x, y), 20)
    pygame.draw.circle(window, (0, 255, 0), (x1, y1), 30)
    pygame.display.flip()

    x += add1
    y += add2
    if x >= 350 or x <= 50:
        add1 *= -1
    if y >= 550 or y <= 50:
        add2 *= -1
    x1 += add3
    y1 += add4
    if x1 >= 350 or x1 <= 50:
        add3 *= -1
    if y1 >= 550 or y1 <= 50:
        add4 *= -1
    if (x1-x)**2+(y1-y)**2 <= 50**2:
        x,x1 = x1,x
        y,y1 = y1,y
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pass
        elif event.type == pygame.MOUSEBUTTONUP:
            pass