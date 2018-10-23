"""__author__ = 余婷"""
import pygame

if __name__ == '__main__':
    # 1. 初始化游戏模块
    pygame.init()

    # 2. 创建游戏窗口
    """
    display.set_mode(窗口大小): 创建一个窗口并且返回
    窗口大小: 是一个元祖，并且元祖中需要两个值分别表示宽度和高度(单位是像素)
    """
    window = pygame.display.set_mode((400, 600))


    # 3. 让游戏一直运行，直到点关闭按钮才结束
    flag = True
    while flag:
        # 获取游戏过程中产生的所有的事件
        for event in pygame.event.get():
            # type来判断事件的类型
            if event.type == pygame.QUIT:
                exit()  # 退出程序
                # flag = False








