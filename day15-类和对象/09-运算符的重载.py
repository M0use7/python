"""__author__ = 唐宏进 """

"""
如果希望类的对象支持相应的运算符操作(例如：+,-,*,/,<,>)，就必须实现相应的魔法方法。
这个过程就叫运算符的重载

+:__add__()
>:__gt__()
...
一般情况需要对>或者<进行重载，重载后可以通过sort方法直接对对象的列表进行排序
"""
class Students:
    def __init__(self, name='', age=0, score=0):
        self.name = name
        self.age = age
        self.score = score

    # 重载 + 符号
    # self:+前面的对象
    # other:+后面的对象
    def __add__(self, other):
        return self.score+other.score

    # 重载 > 符号
    # 注意：重载>和<可以只重载一个，另外一个对应的功能自动取反
    def __gt__(self, other):
        return self.age>other.age

    # 重写魔法方法__str__，用来定制对象的打印样式
    def __str__(self):
        return str(self.__dict__)

class SchoolChild(Students):
    def __add__(self, other):
        return self.age+other.age

if __name__ == '__main__':
    stu1 = Students('小明', 18, 90)
    stu2 = Students('老王', 28, 88)
    stu3 = Students('小红', 24, 85)

    print(stu1)

    all_students = [stu1,stu2,stu3]
    all_students.sort()
    for stu in all_students:
        print(stu.name,stu.age,stu.score)

    print(stu1 + stu2)
    print(stu1 > stu2)
    print(stu3 < stu2)

    c1 = SchoolChild('小明明', 18, 90)
    c2 = SchoolChild('老王王', 28, 88)
    print(c1 + c2)
    print(c1 > c2)
    print(c1 < c2)