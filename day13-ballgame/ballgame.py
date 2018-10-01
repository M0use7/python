"""__author__ = 唐宏进 """
import pygame
import thj_color
from random import randint
"""
游戏功能：点击屏幕在点击的地方产生一个球，球可以自由移动，撞到便捷会弹回，撞到其他的球会吃掉

第一步：搭建游戏窗口
第二步：点击屏幕产生球
第三步：让球动起来（需要用列表来保存所有的球，需要使用字典来保存每个球的信息）
第四步：球碰撞后的效果
"""
# 全局变量
WINDOW_WIDTH = 400 # 屏幕宽度
WINDOW_HEIGHT = 600 # 屏幕高度

key_ball_color = 'ball_color'
key_ball_center = 'ball_center'
key_ball_radius = 'ball_radius'
key_ball_xspeed = 'ball_xspeed'
key_ball_yspeed = 'ball_yspeed'
key_ball_alive = 'ball_alive'
all_balls = [] # 保存所有的球


def ball_crash():
    """
    检测碰撞
    :return:
    """
    # 看屏幕上的每个球是否和其他的球的圆心距小于等于半径和
    # 拿第一个球
    for ball in all_balls:
        # 拿另外一个球
        for other in all_balls:
            if ball == other or ball[key_ball_alive] == False or other[key_ball_alive] == False:
                continue
            # 判断两次拿到的球是否碰撞
            x1, y1 = ball[key_ball_center]
            x2, y2 = other[key_ball_center]
            r1 = ball[key_ball_radius]
            r2 = other[key_ball_radius]
            if (x1-x2)**2 + (y1-y2)**2 <= (r1 + r2)**2:
                pass
                # 相撞后:
                #     ball[key_ball_radius] += int(other[key_ball_radius]*0.1)
                #     other[key_ball_alive] = False


def draw_all_ball():
    """
    画所有的球
    :return:
    """
    window.fill(thj_color.gray)
    for ball in all_balls[:]:
        # 如果活着就画出来，否则就移除
        if ball[key_ball_alive]:
            pygame.draw.circle(window,ball[key_ball_color],ball[key_ball_center],ball[key_ball_radius])
        else:
            all_balls.remove(ball)
    pygame.display.update()


def ball_move():
    """
    球动起来
    :return:
    """
    for ball in all_balls:
        # 获取新的原点
        ball_x,ball_y = ball[key_ball_center]
        new_x = ball_x + ball[key_ball_xspeed]
        new_y = ball_y + ball[key_ball_yspeed]

        ball[key_ball_center] = new_x, new_y

        # 做边界检测
        # x 方向的边界
        if new_x < ball[key_ball_radius]:
            new_x = ball[key_ball_radius]
            ball[key_ball_xspeed] *= -1
        elif new_x > WINDOW_WIDTH - ball[key_ball_radius]:
            new_x = WINDOW_WIDTH - ball[key_ball_radius]
            ball[key_ball_xspeed] *= -1
        # y方向的边界
        if new_y < ball[key_ball_radius]:
            new_y = ball[key_ball_radius]
            ball[key_ball_yspeed] *= -1
        elif new_y > WINDOW_HEIGHT - ball[key_ball_radius]:
            new_y = WINDOW_HEIGHT - ball[key_ball_radius]
            ball[key_ball_yspeed] *= -1

        # 3.修改圆心坐标
        ball[key_ball_center] = new_x,new_y


def create_ball(window,pos):
    """
    在指定的位置产生一个随机颜色的球
    :param window:
    :param pos:
    :return:
    """
    ball_color = thj_color.rand_color()
    ball_center = pos
    ball_radius = randint(10, 30)

    # 创建球对应的字典
    ball = {
        key_ball_color:ball_color,
        key_ball_center:ball_center,
        key_ball_radius:ball_radius,
        key_ball_xspeed:randint(-5,5),
        key_ball_yspeed:randint(-5,5),
        key_ball_alive:True
    }
    # 保存球的信息
    all_balls.append(ball)

    # 画球
    pygame.draw.circle(window, ball_color, ball_center, ball_radius)
    pygame.display.update()

#
# def main_game():
    """
    系统主系统
    :return:
    """
    # 初始化游戏
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
window.fill(thj_color.white)

    # 进入游戏界面默认显示的内容和要执行的操作写在这.....
pygame.display.flip()


# 游戏循环
while True:
    pygame.time.delay(50)
    # 游戏循环执行的代码写在这...
    ball_move() # 修改球的位置
    draw_all_ball() # 重新画所有的球
    ball_crash() # 球的碰撞

    # 事件检测
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        # 事件发生要执行的操作写这个下面...
        # 1.鼠标按下
        elif event.type == pygame.MOUSEBUTTONDOWN:
            create_ball(window, event.pos)
