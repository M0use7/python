"""__author__ = 唐宏进 """
from random import randint
import pygame

# 初始化，创建窗口
pygame.init()
window = pygame.display.set_mode((600,600))
window.fill((255, 255, 255))
pygame.display.flip()


# 游戏循环
while True:
    # 所有的事件处理的入口就是这个for循环
    # for循环中的代码只有游戏事件发生后才会执行
    """
    事件的type：
    
    a.鼠标事件：
    QUIT:关闭按钮被点击事件
    MOUSEBUTTONDOWN:鼠标按下事件
    MOUSEBUTTONUP:鼠标按下松开时对应的事件
    MOUSEMOTION:鼠标移动事件
    
    b.键盘事件：
    KEYDOWN:键盘按下
    KEYUP:键盘弹起
    
    c.事件的pos --- 鼠标事件发生的位置(坐标)
    d.事件的key：--- 键盘事件被按的键对应的编码值
    """
    for event in pygame.event.get():
        # 不同的事件发生后，对应的type值不一样
        if event.type == pygame.QUIT:
            print('点击关闭按钮')
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # 鼠标按下要做的事情就写在这儿
            print(event.pos)
            print('鼠标按下')
            # 鼠标按下一次画一个球
            pygame.draw.circle(window,(randint(0,255),randint(0,255),randint(0,255),)
                               ,event.pos,randint(20,50))
            pygame.display.flip()
        elif event.type == pygame.MOUSEBUTTONUP:
            print('鼠标弹起',event.pos)
        elif event.type == pygame.MOUSEMOTION:
            print('鼠标移动')
            # pygame.draw.circle(window, (randint(0, 255), randint(0, 255), randint(0, 255),)
            #                    , event.pos, randint(20, 50))
            # pygame.display.flip()
            pass
        elif event.type == pygame.KEYDOWN:
            print('键盘按下',event.key,chr(event.key))
        elif event.type == pygame.KEYUP:
            print('键盘弹起')

