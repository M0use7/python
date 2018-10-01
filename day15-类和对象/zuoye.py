"""__author__ = 唐宏进 """

# 0.定义一个学生类。有属性：姓名、年龄、成绩（语文，数学，英语)[每课成绩的类型为整数]
# 方法： a. 获取学生的姓名：getname() b. 获取学生的年龄：getage()
# c. 返回3门科目中最高的分数。get_course()
# class Student:
#     def __init__(self, name='', age=0):
#         self.name = name
#         self.age = age
#         self.score = []
#
#     def get_name(self):
#         return self.name
#
#     def get_age(self):
#         return self.age
#
#     def get_score(self):
#         return max(self.score)
#
# stu1 =Student('小明', 20)
# stu1.score = [78, 86, 92]
# print(stu1.get_name())
# print(stu1.get_age())
# print(stu1.get_score())


# 1.建立一个汽车类Auto，包括轮胎个数，汽车颜色，车身重量，速度等成员变量，
# 并通过不同的构造方法创建实例。至少要求 汽车能够加速 减速 停车。
# 再定义一个小汽车类CarAuto 继承Auto 并添加空调、CD等成员变量 覆盖加速 减速的方法
# class Auto:
#     def __init__(self, tyre_number=0, color='', weight='', speed=''):
#         self.tyre_number = tyre_number
#         self.color = color
#         self.weight = weight
#         self.speed = speed
#
#     def speed_up(self):
#         print('加速!!')
#     def slow_down(self):
#         print('减速!!')
#     def stop(self):
#         print('停车~~')
#
# class CarAuto(Auto):
#     def __init__(self, air_conditioner='制冷', CD='god is a girl'):
#         super().__init__(4, '黑色', '1.5t', '60km/h')
#         self.air_conditioner = air_conditioner
#         self.CD = CD
#
#     def speed_up(self):
#         print('覆盖加速!!')
#     def slow_down(self):
#         print('覆盖减速!!')
#
# car1 = CarAuto()
# print(car1.__dict__)
# car1.speed_up()
# car1.slow_down()
# car1.stop()

# 2.创建一个名为User的类，其中包含属性firstname 和lastname ，
# 还有用户简介通常会存储的其他几个属性。在类User中定义一个名为describeuser() 的方法，
# 它打印用户信息摘要;再定义一个名为greetuser() 的方法，它向用户发出个性化的问候。
# class User:
#     def __init__(self, firstname='', lastname=''):
#         self.firstname = firstname
#         self.lastname = lastname
#     def describeuser(self):
#         print('firstname:%s lastname:%s'%(self.firstname,self.lastname))
#     def greetuser(self):
#         print('尊敬的%s用户，您好！'%(self.lastname))
#
# user1 = User('爱新觉罗', '玄烨')
# user2 = User('爱新觉罗', '弘历')
# user1.describeuser()
# user1.greetuser()
# user2.describeuser()
# user2.greetuser()

# 3.创建一个Person类，添加一个类字段用来统计Perosn类的对象的个数
# class Person:
#     count = 0
#     def __init__(self):
#         Person.count += 1
#
# p1 = Person()
# P2 = Person()
# print(Person.count)

# 4.写一个类，其功能是：
# 1.解析指定的歌词文件的内容
# 2.按时间显示歌词 提示：歌词文件的内容一般是按下面的格式进行存储的。歌词前面对应的是时间，
# 在对应的时间点可以显示对应的歌词
import time
class Lyrics:
    """歌词类"""
    def __init__(self):
        self.lrc = ''
        self._time = 0

    @property
    def time(self):
        return self._time


    @time.setter
    def time(self,time):
        index = time.index(':')
        fen = time[1:index]
        miao = time[index+1:]
        self._time = float(fen)*60 + float(miao)

    def __str__(self):
        return str(self.time) + ':' + self.lrc

    def __gt__(self, other):
        return self._time > other.time

class LrcAnalyze:
    """歌词解析类"""
    __all_lrcs = [] # 保存所有的歌词对象

    @classmethod
    def __analyze(cls,file):
        """读取歌词内容"""
        with open(file, 'r', encoding='utf-8') as f:
            line = f.readline()
            while line:
                cls.__create_lrc(line)
                line = f.readline()
            cls.__all_lrcs.sort(reverse=True)

    @classmethod
    def __create_lrc(cls,line):
        """创建歌词对象"""
        lrcs = line.split(']')
        lrc = lrcs[-1]
        for index in range(0,len(lrcs)-1):
            time = lrcs[index]
            lrc_obj = Lyrics()
            lrc_obj.lrc = lrc
            lrc_obj.time = time
            cls.__all_lrcs.append(lrc_obj)

    @classmethod
    def get_lrc(cls, time, file):
        """根据时间获取歌词"""
        if not cls.__all_lrcs:
            cls.__analyze(file)

        for lrc_obj in cls.__all_lrcs[:]:
            if lrc_obj.time <= time:
                return lrc_obj

number = 0
while True:
    time.sleep(1)
    number += 1
    print(LrcAnalyze.get_lrc(number,'./files/蓝莲花.txt'))