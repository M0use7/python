"""__author__ = 唐宏进 """
"""
类中的内容：属性和方法
1.属性：
a.对象的属性：不同的对象，对应的值可能不一样，这样的属性是对象属性
类中的对象属性是声明在init方法中的，并且声明格式是：self.属性名 = 初值
对象属性的使用：对象.属性名

b.类的字段：属于类的，所有的对象对应的值是一样的
2.方法：（保存功能的）
a.对象方法
b.类方法
c.静态方法
"""

class Student:
    """学生类"""
    def __init__(self):
        # 声明对象属性name,age,id
        self.name = '张三'
        self.age = 0
        self.id = '001'

class Dog:
    """狗类"""
    # 创建Dog对象的时候，必须传类型和颜色
    def __init__(self, type1, color):
        self.type = type1
        self.color = color

class Computer:
    """电脑类"""
    def __init__(self, color, memory):
        self.color = color
        self.memory = memory

# 练习：写一个矩形类，拥有属性长和宽
class Rect:
    def __init__(self, long=20, width=10):
        self.long = long
        self.width = width

if __name__ == "__main__":
    # stu1就是Student类的对象
    stu1 = Student()
    # 通过对象去使用对象的属性
    print(stu1.name,stu1.age,stu1.id)
    # 通过对象去修改对象的属性
    stu1.name = '老王'
    print(stu1.name)

    dog1 = Dog('土狗', '黄色')
    print(dog1.type,dog1.color)

    dog2 = Dog('斗狗','黑色')
    print(dog2.type,dog2.color)

    comp1 = Computer('白色', 495)
    print(comp1.color,comp1.memory)
    comp2 = Computer('黑色', 512)
    print(comp2.color, comp2.memory)
