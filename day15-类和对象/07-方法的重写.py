"""__author__ = 唐宏进 """

"""
子类继承父类，拥有了父类的属性和方法以后，还可以添加自己的属性和方法

1.添加方法和类的字段
直接在子类中声明相应的方法

2.添加对象属性
对象的属性是通过继承父类的init方法而继承下来
如果想要保留父类的对象的同时，添加自己的对象属性，需要在子类的init方法中通过super()去调用父类的init方法

3.方法的重写
在子类中重新实现父类的方法，就是重写
方式一：直接覆盖父类的实现
方式二：保留父类的功能再添加其他功能

4.类中方法的调用过程
先在当前这个类中去找，没有就去父类中找，找不到再去父类的父类中找，依次类推，如果在基类中都没有找到才崩溃，
在第一次找到的位置去调用

注意：使用super的时候必须是通过super()来代替父类或者是父类对象
"""
class Animal:
    """动物类"""
    def __init__(self):
        self.age = 0
        self.sex = '雌'

    def shout(self):
        print('嗷嗷叫~~')

class Cat(Animal):
    """猫类"""
    def __init__(self):
        # 调用父类的init方法
        super().__init__()
        self.name = '小花'

    food = '鱼'

    def shout(self):
        print('喵喵~')

class Dog(Animal):
    """狗类"""
    def shout(self):
        # 通过super()调用父类的方法，保留父类的功能
        super().shout()
        print('汪汪!!')

cat1= Cat()
cat1.shout()
dog1 = Dog()
dog1.shout()

if __name__ == '__main__':
    pass