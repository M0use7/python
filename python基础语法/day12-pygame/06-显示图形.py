"""__author__ = 余婷"""
import pygame

from math import pi

if __name__ == '__main__':
    # 初始化，创建窗口
    pygame.init()
    window = pygame.display.set_mode((400, 600))
    window.fill((255, 255, 255))

    """
    1.画线段
    def line(Surface, color, start_pos, end_pos, width=1)
    Surface: 画在哪儿
    color：线的颜色
    start_pos: 起点
    end_pos：终点
    width: 线宽
    """
    # 画一条水平线
    pygame.draw.line(window, (255, 0, 0), (50, 100), (200, 100))
    # 画一条垂直线
    pygame.draw.line(window, (0, 255, 0), (50, 100), (50, 200), 2)

    """
    2.画线段(折线)
    def lines(Surface, color, closed, pointlist, width=1)
    Surface: 画在哪儿
    color: 线的颜色
    closed: 是否闭合（是否连接起点和终点）
    pointlist：点对应的列表
    """
    pygame.draw.lines(window, (0, 0, 255), True, [(100, 200), (150, 120), (140, 300)])

    """
    3.画圆
    def circle(Surface, color, pos, radius, width=0)
    Surface: 画在哪儿
    color: 颜色
    pos：圆心坐标
    radius：半径
    width: 线宽，0 -> 填充
    """
    pygame.draw.circle(window, (255, 255, 0), (200, 300), 100, 0)

    """
    4.画矩形
    def rect(Surface, color, Rect, width=0)
    Surface:画在哪儿
    color: 颜色
    Rect：范围(元祖，元祖中有四个元素，分别是x,y,width,height)
    """
    pygame.draw.rect(window, (0, 255, 0), (10, 100, 50, 100))

    """
    5.画多边形
    polygon(Surface, color, pointlist, width=0)
    """
    pygame.draw.polygon(window, (0, 255, 255), [(300, 50), (250, 40),(100, 50), (200, 150)])

    """
    6.画椭圆
    def ellipse(Surface, color, Rect, width=0)
    """
    pygame.draw.ellipse(window, (123, 200, 210), (10, 200, 150, 60))

    """
    7.画弧线
    def arc(Surface, color, Rect, start_angle, stop_angle, width=1)
    start_angle: 0-2pi
    stop_angle:
    pi --- 180°   1° --- pi/180
    59° = pi/180 * 59
    """
    pygame.draw.arc(window, (255, 0, 0), (200, 400, 100, 100), pi/4+pi, pi*3/4+pi, 3)


    # 展示内容
    pygame.display.flip()



    # 游戏循环
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()