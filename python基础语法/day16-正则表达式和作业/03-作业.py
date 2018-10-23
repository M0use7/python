"""__author__ = 余婷"""


# ==================1.电脑类=================
class Computer:
    """电脑类"""
    def __init__(self, brand='联想', color='黑色', memory=0):
        self.brand = brand
        self.color = color
        self.memory = memory

    @staticmethod
    def play_game(game):
        print('玩儿%s' % game)

    @staticmethod
    def code():
        print('写python代码')

    @staticmethod
    def watch_video(video):
        print('在看%s' % video)


com1 = Computer(memory=512)
# 查
print(com1.color)
print(getattr(com1, 'color', '白色'))
# 改
com1.brand = '戴尔'
setattr(com1, 'brand', '华硕')
# 增
# com1.size = 13.5
setattr(com1, 'size', 15)
print(com1.size)
# 删
del com1.size
delattr(com1, 'memory')


# =====================2.人和狗====================
class Dog:
    """狗"""
    def __init__(self, name1='', color1='', age1=0):
        self.name = name1
        self.color = color1
        self.age = age1

    def shout(self):
        print('%s在汪汪叫!' % self.name)


class Person:
    """人"""
    def __init__(self, name='', age=0):
        self.name = name
        self.age = age
        self.dog = None   # dog属性的值必须是Dog类的对象

    def took_dog(self):
        # 能遛狗的前提是自己有狗
        if not self.dog:
            print('没有🐶~溜自己吧！')
            return
        print('%s牵着%s在玩儿~' % (self.name, self.dog.name))


p1 = Person('小明')
p1.age = 18
p1.dog = Dog('大黄', '黄色', 2)
p1.took_dog()


# ===================3.学生和班级================
class Student:
    """学生"""
    def __init__(self, name, age=0, id=''):
        self.name = name
        self.age = age
        self.id = id

    def response(self):
        """答到"""
        print('%s,到！' % self.name)

    def show_info(self):
        print('姓名:%s 年龄:%d 学号:%s' % (self.name, self.age, self.id))


class Class:
    """班级"""
    def __init__(self, name):
        self.students = []  # 这个列表的元素是学生对象
        self.name = name
        self.__count = 0

    def add_student(self):
        """添加学生"""
        name = input('姓名:')
        age = input('年龄:')
        # 学号
        self.__count += 1
        id = 'stu' + str(self.__count).rjust(3, '0')

        # 创建学生对象
        stu = Student(name, int(age), id)

        # 将学生保存到班级中
        self.students.append(stu)

    def del_student(self):
        """删除学生"""
        del_name = input('请输入要删除的学生名字:')

        is_del = False
        # 遍历列表拿到的是学生对象
        for stu in self.students[:]:
            if stu.name == del_name:
                self.students.remove(stu)
                print('删除成功!')
                is_del = True

        if not is_del:
            print('没有该学生！')

    def call_names(self):
        """点名"""
        for stu in self.students:
            print(stu.name)
            stu.response()


class1 = Class('python1806')
# 添加学生
for _ in range(5):
    class1.add_student()
# 删除学生
class1.del_student()
# 点名
class1.call_names()


# =====================4.数学类========================
class Math:
    pi = 3.14159265358
    e = 2.7

    @staticmethod
    def sum_double(num1, num2):
        return num1 + num2

    @classmethod
    def circle_area(cls, r):
        return cls.pi * r**2































