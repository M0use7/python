"""__author__ = 唐宏进 """
from math import pi

"""
对象方法：
a.什么样的方法是对象方法：直接声明在类的函数默认就是对象方法，有一个默认参数self
b.对象方法要通过对象来调用：对象.对象方法()
c.对象方法中的默认参数self，不需要传参。因为在调用这个方法的时候，系统会自动将当前这个对象传给self
哪个对象调用的方法，self就指向谁
"""
class Circle:
    def __init__(self,radius1):
        self.radius = radius1

    # 声明了一个对象方法area
    # 在这儿，self就是调用area方法的对象。对象能做的事情，self都能做
    def area(self):
        # print(id(self))
        # print(self.radius)
        # self.radius = 100
        # print('求圆的面积')
        return pi*self.radius**2

# 练习1：写一个矩形类，有属性长和宽，有两个功能，分别是球周长和面积
class Rect:
    def __init__(self,length1,width1):
        self.length = length1
        self.width = width1

    def meter(self):
        return 2*(self.length+self.width)

    def area(self):
        return self.length*self.width
# 练习2：写一个班级类，班级里面有多个学生的xx成绩（一门）和班级名，可以获取班级成绩中的最高分
class Class:
    def __init__(self,class_name1):
        self.class_name = class_name1
        self.grades = []

    def max_grade(self):
        if not self.grades:
            return 0
        return max(self.grades)


if __name__ == '__main__':
    # 创建一个半径是5的圆的对象
    c1 = Circle(5)
    print(c1.area())

    r1 = Rect(10,20)
    print(r1.meter())
    print(r1.area())

    class1 = Class('python1806')
    class1.grades = [90,78,82,89,95]
    print(class1.class_name,class1.max_grade())
