"""__author__ = 唐宏进 """

"""
1.匿名函数
函数名 = lambda 参数列表:返回值

函数名(实参)

2.作用域
函数的调用过程是一个压栈的过程
从声明开始到文件结束

全局变量：在函数/类外面声明的变量是全局变量

局部变量：在函数/类里面的变量是局部变量
从声明开始到函数/类结束

3.递归函数(能不用就不用)
a.找临界值(结束循环/让函数结束)
b.假设函数功能已经实现，找关系(找上次循环和本次循环的关系/f(n)和f(n-1)的关系)
c.通过f(n-1)实现f(n)的功能

4.模块的使用
一个py文件就是一个模块

import 模块名
from 模块名 import 内容
当程序导入模块的代码的时候，会进入模块中，将模块里面的代码全部执行一遍
"""

sum1 =lambda x,y:x*y

def sum1_1(x,y):
    """
    函数功能的描述
    :param x:
    :param y:
    :return:
    """
    return x*y

sum1_1(10,20)




