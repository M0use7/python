"""__author__ = 唐宏进 """
"""
python中并没有真正的私有化
python的类中默认的属性和方法都是公开的

1.私有化
a.类中的属性和方法都可以通过在属性名和方法名前加两个下划线，来让属性和方法变成私有的
b.私有的属性和方法只能在当前的类中使用

2.私有化的原理
在前面有两个下划线的属性名和方法名前添加了'_类名'来阻止外部通过直接访问属性名来使用属性
"""
class Dog:
    # 字段
    number = 100
    __count = 200

    def __init__(self):
        # 对象的属性
        self.color = '黄色'
        self.age = 3
        self.name = '大黄'
        self.__sex = '公狗'
    # 对象方法
    def eat(self):
        print('%s在吃屎~'%self.name)

    # 在类中可以使用私有的方法
    def __eat(self):
        print('%s啃骨头~'%self.name)

    # 类方法
    @classmethod
    def bark(cls):
        print('汪汪汪~~~')
    def __bark(cls):
        print('汪汪汪~~~')

    # 静态方法
    @staticmethod
    def function():
        print('看家！！')


# python的类中默认的属性和方法都是公开的
dog1 = Dog()
print(Dog.number)
print(dog1.name, dog1.color, dog1.age)
dog1.eat()
Dog.bark()
Dog.function()
print(dog1.__dict__)

# 在类的外面不能直接使用私有的属性
# print(Dog.__count)
# print(dog1.__sex)
# dog1.__eat()
# Dog.__bark()
if __name__ == '__main__':
    pass