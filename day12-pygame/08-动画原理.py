"""__author__ = 唐宏进 """
import pygame

pygame.init()
window = pygame.display.set_mode((400,600))
window.fill((255,255,255))
pygame.display.flip()
# 球的圆心坐标
x = 100
y = 100
r = 50
add1 = 2
add2 = 1
while True:
    pygame.time.delay(5)
    # 将之前纸上的内容给覆盖
    window.fill((255, 255, 255))
    # 不断的画圆
    pygame.draw.circle(window,(0,255,0),(x,y),r)
    pygame.display.update()
    # 改变y值让圆在垂直方向移动
    y += add1
    x += add2
    if y >= 550 or y <= 50:
        add1 *= -1
    if x >= 350 or x <= 50:
        add2 *= -1
    # r += add1
    # if r > 120 or r <= 20:
    #     add1 *= -1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
