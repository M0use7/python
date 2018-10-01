"""__author__ = 唐宏进 """

"""
封装：
1.函数：对实现某一特定功能代码段的封装
2.模块：对变量、函数、类进行封装
模块：一个py文件就是一个模块

"""
def mul(*numbers):
    sum1 = 1
    for item in numbers:
        sum1 *= item
    return sum1
print(mul(1,2,5))

"""
1.怎么使用其他模块中的内容？
a.import 模块
通过模块.内容的形式去使用模块中的内容（能够使用全局变量、函数和类）
b.from 模块 import 模块中的内容
可以直接使用模块中的内容

c.from 模块 import *  ---> 将模块中的所有内容都导入
"""

# # 导入系统的math模块
# import math
# print(math.pi)
#
# # 导入自定义的my_list模块
# import  my_list
#
# # a.使用模块中的全局变量
# print(my_list.empty)
#
# # b.使用模块中的函数
# number = my_list.count1([1,2,3,4,6,1,8,9,1],1)
# print(number)

# b.
from my_list import count1,empty
number = count1([1,2,3,4,6,1,8,9,1],1)
print(number)
print(empty)

# c.
from math import *
print(pi)
print(sqrt(9))


"""
2.重命名
import 模块 as 新名字
from 模块 import 内容 as 新名字
"""
import random as RAN
print(RAN.randint(1,10))

from datetime import date as DataClass,datetime as TimeClass
print(DataClass.today())
print(TimeClass.now())

"""
每个模块都有一个__name__属性，这个属性的值默认就是当前模块的文件名。
当当前模块正在被执行(直接在当前模块中点了run)的时候，__name__属性的值是'__main__'

在一个模块中，将不希望被其他模块导入的代码写在if __name__ == '__name__'中，
希望被导入的放到这个if外面

建议：函数的声明、类的声明一般写在if的外面，其他的写在if里面（想要被外部使用的全局变量也可写在外面）
"""
import my_model
# from my_model import fun1
# print(fun1())

print('my_model',my_model.__name__)
print('01-模块',__name__)

