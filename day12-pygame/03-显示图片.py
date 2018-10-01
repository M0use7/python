"""__author__ = 唐宏进 """

import pygame

# .初始化游戏模块
pygame.init()

# 2.创建窗口
window = pygame.display.set_mode((600, 600))

# 给窗口填充颜色
"""
fill(颜色)
颜色：计算机三原色（红、绿、蓝），每个颜色对应的值的范围是0-255。可以通过三原色的值可以调配出不同的颜色
颜色值：是一个元祖，元祖中三个元素，分别代表红绿蓝（rgb）
(255,0,0) ---> 红色
(0,255,0) ---> 绿色
(0,0,255) ---> 绿色
(255,255,255) ---> 白色
(0,0,0) ---> 黑色
"""
# window.fill(255, 255, 255)

# a.获取图片，创建图片对象
"""
image.load(图片路径)：获取本地的一张照片，返回图片对象
"""
image = pygame.image.load('./files/cat.jpg')

"""
get_size()：获取大小，返回值是一个元祖，有两个元素，分别是宽和高
"""
image_width,image_height = image.get_size()
# b.渲染图片（将图片贴在纸上）
"""
blit(渲染对象，位置)
位置：坐标(x,y)值的类型是元祖，元祖有两个元素分别对应x坐标和y坐标
"""
# window.blit(image,(0, 0))
window.blit(image,(600-image_width,600-image_height))
# c.展示内容（将纸贴在画框上）
pygame.display.flip()

# 3.游戏循环
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()