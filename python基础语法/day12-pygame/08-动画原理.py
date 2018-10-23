"""__author__ = 余婷"""
import pygame

if __name__ == '__main__':
    # 初始化
    pygame.init()
    window = pygame.display.set_mode((400, 600))
    window.fill((255, 255, 255))
    pygame.display.flip()

    # 球的圆心坐标
    x = 100
    y = 100
    r = 50
    add = 4
    y_speed = 2
    # 游戏循环
    while True:

        # 延迟
        # pygame.time.delay(10)

        # 将之前纸上的内容给覆盖
        window.fill((255, 255, 255))
        # 不断的画圆
        pygame.draw.circle(window, (255, 0, 0), (x, y), r)
        pygame.display.update()

        # 改变y值让圆在垂直方向移动
        y += y_speed
        # r += add
        # if r >= 120 or r <= 20:
        #     add *= -1
        # 边界检测
        if y > 600 - r:
            y = 600 - r
            y_speed = -2
        elif y < 50:
            y = 50
            y_speed = 2

        # 事件检测
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()


