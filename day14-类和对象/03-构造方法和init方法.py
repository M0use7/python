"""__author__ = 唐宏进 """
"""
1.构造方法：系统自动创建，方法名和类名一样。用来创建对象
2.__init__:init方法的功能是用来做初始化和添加对象的属性
当我们通过构造方法去创建对象的时候，系统会自动调用init方法（不用主动调用init方法）
"""
class Dog:
    def __init__(self):
        print('init方法')


class Person:
    # init方法可以添加参数
    def __init__(self, name,age = 18):
        print(name,age)
        print('人类的init方法')


if __name__ == '__main__':
    # 创建对象的过程：调用构造方法在内存中开辟空间创建一个对象，然后用新建的这个对象调用init方法，
    #                     来初始化对象的属性。最后才将对象返回
    dog1 = Dog()
    dog2 = Dog()

    # 如果类的init方法有参数，通过给构造方法传参类init方法传参
    p1 = Person('小明')
    p2 = Person('小红', 20)




