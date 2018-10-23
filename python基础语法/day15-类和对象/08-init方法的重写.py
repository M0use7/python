"""__author__ = 余婷"""


# 练习：写一个Person类,拥有属性name,age,sex。要求创建Person对象的时候必须给name和age赋值，sex可赋可不赋
#      再写一个Staff类继承自Person类，要求保留Person中所有的属性，并且添加新的属性salary。
#      要求创建Staff类的对象的时候，只能给name赋值(必须赋)

class Person:
    def __init__(self, name1, age1, sex1='boy'):
        self.name = name1
        self.age = age1
        self.sex = sex1


class Staff(Person):
    def __init__(self, name):
        super().__init__(name, 18)
        self.salary = 0


if __name__ == '__main__':
    p1 = Person('张三', 20, 'boy')
    p2 = Person('夏明', 30)

    s1 = Staff('小红')