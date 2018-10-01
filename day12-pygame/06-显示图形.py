"""__author__ = 唐宏进 """

import pygame
from math import pi
# 初始化，创建窗口
pygame.init()
window = pygame.display.set_mode((600,600))
window.fill((255, 255, 255))

"""
1.画直线
def line(Surface, color, stat_pos, end_pos, with=1)
Surface:画在哪
color:线的颜色
stat_pos:起点
end_pos:终点
width:线宽
"""
# 画一条水平线
pygame.draw.line(window,(255, 0, 0), (50,100),(200,100))
# 画一条垂直线
pygame.draw.line(window,(0, 255, 0), (50,100),(50,200))

"""
2.画线段（折线）
def lines(Surface, color, closed, pointlist with=1)
Surface:画在哪
color:线的颜色
closed:是否闭合(是否连接起点和终点)
pointlist:点对应的列表
"""
pygame.draw.lines(window,(0,0,255),False,[(70,150),(120,170),(60,250)])

"""
3.画圆
def circle(Surface, color, pos, radius, width=0 )
Surface:画在哪
color:颜色
pos:圆心坐标
radius:半径
width: 线宽
"""
pygame.draw.circle(window,(255,255,0),(200,300),100)

"""
4.画矩形
def circle(Surface, color, Rect, width=0 )
Surface:画在哪
color:颜色
Rect:范围(元祖，元祖中有四个元素，分别是x,y,width,height)
"""
pygame.draw.rect(window,(0,255,0),(0,0,50,100))

"""
5.多边形
def polygon(Surface, color, pointlist, width=0)
"""
pygame.draw.polygon(window,(0,0,255),[(300,0),(500,0),(400,100),(200,100)])

"""
6.画椭圆
def ellipse(Surface, color, Rect, width=0)
"""
pygame.draw.ellipse(window, (0,0,255), (200,500,200,100))
"""
7.画弧线
def (Surface, color, Rect, start_angle, stop_angle, width=0)
"""
pygame.draw.arc(window,(255,0,0),(300,300,200,200),0,pi/2)
pygame.draw.arc(window,(0,255,0),(300,300,200,200),pi/2,pi)
pygame.draw.arc(window,(0,0,255),(300,300,200,200),pi,pi*3/2)
pygame.draw.arc(window,(255,255,0),(300,300,200,200),pi*3/2,pi*2)
# 展示内容
pygame.display.flip()

# 游戏循环
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()


