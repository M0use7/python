"""__author__ = 唐宏进 """

"""
1.多继承(了解)
python中的类支持多继承，但是不建议使用
多继承继承的时候，子类可以拥有所有父类的所有方法和类的字段，但是只能继承第一个父类的对象属性

2.多态
多态指的是一种事物有多种形态
有继承就有多态：不同类继承自同一个类，其实就是对这个共同的父类的不同的形态。继承后对方法的重写也是多态的表现。

3.封装、继承、多态
封装：一个类可以通过不同的方法对不同的功能进行封装。通过属性对不同的数据进行封装。
继承：通过继承可以让子类拥有父类的属性和方法

4.包
将多个模块封装到一起，就是包。包有一个默认文件__init__文件夹

a.import 包.模块

b.from 包 import 模块

c.from 包.模块 import 方法/变量/类

5.raise 错误类型
raise可以让程序主动崩溃，一般用于调试
raise：关键字
错误类型：必须是一个类，并且这个类是Exception的子类
"""


class Animal(object):
    def __init__(self,age=0, name='小动物'):
        self.name = name
        self.age = age

    def eat(self):
        print('在吃东西')

class Fly:
    number = 10
    def __init__(self, height=50):
        self.max_height = height

    def fly(self):
        print('能飞%d米'%self.max_height)

# 让Bird同时继承Animal类和Fly类
class Bird(Fly, Animal):
    pass

b1 = Bird()
# print(b1.name, b1.age)
b1.eat()
print(Bird.number)
b1.fly()