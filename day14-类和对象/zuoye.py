# """__author__ = 唐宏进 """
# 1.声明一个电脑类:
# 属性:品牌、颜色、内存大小
# 方法:打游戏、写代码、看视频
# a.创建电脑类的对象，然后通过对象点的方式获取、修改、添加和删除它的属性
# b.通过attr相关方法去获取、修改、添加和删除它的属性
# class Computer:
#     def __init__(self, brand1='Dell', color1='黑色', memory_size1='4G'):
#         self.brand = brand1
#         self.color = color1
#         self.memory_size = memory_size1
#     @staticmethod
#     def play_game(game):
#         print('玩%s游戏', game)
#
#     @staticmethod
#     def write_code():
#         print('写python代码')
#
#     @staticmethod
#     def watch_video(video):
#         print('看%s视频' % video)
# # 创建一个computer对象
# computer = Computer()
# # 获取computer对象的相关属性
# print(computer.brand,computer.color,computer.memory_size)
# # 修改computer对象的颜色属性和内存属性
# computer.color = '白色'
# computer.memory_size = '8G'
# # 给computer对象添加尺寸属性
# computer.size = 15.6
# # 删除computer对象的颜色属性
# del computer.color
#
# # 获取computer对象的品牌属性
# print(getattr(computer,'brand','白色'))
# # 修改computer对象的品牌属性为'Macbook'
# setattr(computer,'brand','Macbook')
# # 给computer对象添加颜色属性
# setattr(computer,'color','粉色')
# # 删除computer对象的内存属性
# delattr(computer,'memory_size')
#
# 2.声明一个人的类和狗的类:
# 狗的属性:名字、颜色、年龄 狗的方法:叫唤
# 人的属性:名字、年龄、狗   人的方法:遛狗
# a.创建人的对象小明，让他拥有一条狗大黄，然后让小明去遛
# class Person:
#     def __init__(self,name, age):
#         self.name = name
#         self.age = age
#         self.dog = None # Dog类的对象
#     def walk(self):
#         if not self.dog:
#             print('您的狗狗正在路上~~~')
#             return
#         print('%s在遛%s玩'%(self.name,self.dog.name))
#
# class Dog:
#     def __init__(self,name,color,age):
#         self.name = name
#         self.color = color
#         self.age = age
#     def bark(self):
#         print('%s在汪汪叫'%self.name)
# person = Person('小明','18')
# person.dog = Dog('大黄', '黄色', 5)
# person.walk()
# person.dog.bark()
#
# 3.声明一个矩形类:
# 属性: 长、宽  方法:计算周长和面积
# a.创建不同的矩形，并且打印其周长和面积
# class Rectangle:
#     def __init__(self,length,width):
#         self.length = length
#         self.width = width
#     def perimeter(self):
#         return (self.length+self.width)*2
#     def area(self):
#         return self.length*self.width
# rec1 = Rectangle(4,5)
# rec2 = Rectangle(3,10)
# print(rec1.perimeter())
# print(rec1.area())
# print(rec2.perimeter())
# print(rec2.area())
#
# 4.创建一个学生类:
# 属性:姓名，年龄，学号   方法:答到，展示学生信息
# 创建一个班级类:
# 属性:学生，班级名  方法:添加学生，删除学生，点名
# class Student:
#     def __init__(self,name, age=0, id=''):
#         self.name = name
#         self.age = age
#         self.id = id
#     def answer(self):
#         print('%s到！'%self.name)
#     def show(self):
#         print(self.name, self.age, self.id)
#
# class Class:
#     def __init__(self, class_name):
#         self.student = []
#         self.name = class_name
#         self.__count = 0
#     def add_student(self):
#         name = input('姓名:')
#         age = input('年龄:')
#
#         # 学号
#         self.__count += 1
#         id = 'stu' + str(self.__count).rjust(3,'0')
#         stu = Student(name,int(age),id)
#
#         # 将学生保存到班级中
#         self.student.append(stu)
#         print('添加成功！')
#     def del_student(self):
#         del_name = input('请输入要删除的学生名字:')
#
#         flag = True
#         # 遍历列表拿到的是学生对象
#         for stu in self.student[:]:
#             if stu.name == del_name:
#                 self.student.remove(stu)
#                 print('删除成功！')
#                 break
#         else:
#             flag = False
#         if not flag:
#             print('没有该学生！')
#     def call(self):
#         for stu in self.student:
#             print(stu.name)
#             stu.answer()


#
# 5.写一个类，封装所有和数学运算相关的功能(包含常用功能和常用值，例如:pi,e等)
#
# class Function:
#     pi = 3.141592653589793
#     e = 2.718281828459045
#
#     @staticmethod
#     def add(*number):
#         """
#         多个数的和
#         :param number:
#         :return:
#         """
#         return sum(number)
#
#     @staticmethod
#     def sub(*number):
#         """
#         多个数相减
#         :param number:
#         :return:
#         """
#         number1 = list(number)[0]
#         for num in list(number)[1:]:
#             number1 -= num
#         return number1
#
#     @staticmethod
#     def mul(*number):
#         """
#         多个数相乘
#         :param number:
#         :return:
#         """
#         sum = 1
#         for num in number:
#             sum *= num
#         return sum
#
#     @staticmethod
#     def div(number1,number2):
#         """
#         两个数相除
#         :param number1: 被除数
#         :param number2: 除数
#         :return:
#         """
#         return number1/number2
#
#     @classmethod
#     def circle_are(cls,r):
#         """
#         圆的面积
#         :param r:
#         :return:
#         """
#         return cls.pi*r**2

