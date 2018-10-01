"""__author__ = 唐宏进 """
from random import randint

# 白色
white = (255, 255, 255)
# 黑色
black = (0, 0, 0)
# 红色
red = (255, 0, 0)
# 黄色
yellow = (250, 250, 0)
# 绿色
green = (0, 255, 0)
# 蓝色
blue = (0, 0, 255)
# 灰色
gray = (120, 120, 120)


def rand_color():
    """随机颜色"""
    return randint(0, 255), randint(0, 255), randint(0, 255)








if __name__ == '__main__':
    pass