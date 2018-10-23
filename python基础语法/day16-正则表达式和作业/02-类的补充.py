"""__author__ = 余婷"""
import Person
from Time import Date

"""
1.多继承(了解)
python中的类支持多继承，但是不建议使用。
多继承继承的时候，子类可以拥有所有父类的所有的方法和类的字段，但是只能继承第一个父类的对象属性

2.多态
多态指的是一种事物有多种形态
有继承就有多态：不同类继承自同一个类，其实就是对这个共同的父类的不同的形态。继承后对方法的重写也是多态的表现。

3.封装、继承、多态
封装：一个类可以通过不同的方法对不同的通能进行封装。通过属性对不同的数据进行封装。
继承：通过继承可以让子类拥有父类的属性和方法

4.包
将多个模块封装到一起，就是包。包就是有一个默认文件__init__.py的文件夹

a.import 包.模块
import download.saveData
download.saveData.save_data_json('abc')

b.from 包 import 模块
from download import downloadData
downloadData.http_downoad('一人之下')

c.from 包.模块 import 方法/变量/类
from download.saveData import insert_db
insert_db('账号')

5. raise 错误类型
raise可以让程序主动崩溃，一般用于调试
raise：关键字
错误类型：必须是一个类,并且这个类是Exception的子类
"""


# ====================1.抛出异常=======================
class YTError(Exception):
    name = ''
    # 通过str魔法方法来设置错误提示信息
    # __str__的本质，就是定义类和对象的打印的内容
    def __str__(self):
        return '余氏错误！%s' % YTError.name

num = 11
if num % 2:
    YTError.name = '奇数错误！'
else:
    YTError.name = '偶数错误!'

raise YTError


# ===================2.多继承======================
class Animal(object):
    def __init__(self, age=0, name='小动物'):
        self.age = age
        self.name = name

    def eat(self):
        print('%s在吃东西' % self.name)


class Fly:
    def __init__(self, height=0):
        self.max_height = height

    def fly(self):
        # print('最大能飞:%d米' % self.max_height)
        print('飞起来')


# 让Bird同时继承Animal类和Fly类
class Bird(Fly, Animal):
    def eat(self):
        print('在吃虫子')
    pass


if __name__ == '__main__':
    bird1 = Bird()
    # print(bird1.name, bird1.age)
    print(bird1.max_height)
    bird1.eat()
    bird1.fly()

    Person.name = '李四'
    Person.eat()