"""__author__ = 唐宏进 """

import pygame

# 初始化游戏和创建窗口
pygame.init()
window = pygame.display.set_mode((400,600))
window.fill((255,255,255))

# 显示文字
# 1.创建字体对象
"""
a.创建系统的字体对象
SysFont(name,size,bold=False,italic=False)
name:字体名（支持系统的字体名）
size:字体大小
bold:是否加粗
italic:是否倾斜

b.创建自定义字体对象
Font（字体文件路径，字体大小）
"""

# 2.根据字体去创建文字对象
# a.创建系统字体
# font = pygame.font.SysFont('Times', 30)

# b.创建自定义字体
font = pygame.font.Font('./files/aa.ttf', 30)
"""
render(text,antialias,color)
txt:需要显示的文字（字符串）
antialias:是否平滑（布尔）
color:颜色
background:背景颜色
"""
text = font.render('你好 pygame', True, (0, 0, 255), (255, 255, 0))

# 3.渲染文字
window.blit(text, (50, 50))

# 4.展示内容
pygame.display.flip()

# 游戏循环
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
