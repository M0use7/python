"""__author__ = 余婷"""

"""
1.匿名函数
函数名 = lambda 参数列表:返回值

函数名(实参)

2.作用域
函数的调用过程是一个压栈的过程

全局变量：在函数/类外面声明的变量是全局变量
从声明开始到文件结束

局部变量: 在函数/类里面声明的变量是局部变量
从声明开始到函数/类结束

global的使用
nonlocal的使用

3.*递归函数(能不用就不用)
a.找临界值(结束循环/让函数结束)
b.假设函数功能已经实现，找关系(找上次循环和本次循环的关系/f(n)和f(n-1)的关系)
c.通过f(n-1)实现f(n)的功能

4.模块的使用
一个py文件就是一个模块

import
form-import
当程序执行到导入模块的代码的时候，会进入模块中，将模块里面的代码全部执行一遍
"""
# import random
# import math


import otherModel
# print(otherModel.a)
# print(otherModel.test())




n = 100
def func1():
    global n
    n = 200

    nn = 10
    def func2():
        nonlocal nn
        nn = 100
    func2()
    print(nn)

func1()
print(n)



sum1 = lambda x, y: x*y

def sum1_1(x, y):
    """
    函数功能的描述
    :param x:
    :param y:
    :return:
    """
    return x*y

sum1_1(10, 20)





if __name__ == '__main__':
    pass