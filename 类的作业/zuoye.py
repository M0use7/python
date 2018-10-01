"""__author__ = 唐宏进 """


class Student:
    def __init__(self, name='', age=0, stu_id=''):
        self.name = name
        self.age = age
        self.stu_id = stu_id

    def response(self):
        print('%s到！'%self.name)

    def show(self):
        print('姓名:%s 年龄:%s 学号:%s'%(self.name, self.age, self.stu_id))


class Class:
    __number = 0
    def __init__(self,class_name=''):
        self.all_student = []
        self.class_name = class_name


    def add_stu(self):
        name = input('请输入学生姓名:')
        age = input('请输入学生年龄:')
        Class.__number += 1
        stu_id = 'python' + str(Class.__number).rjust(3,'0')
        stu = Student(name, int(age), stu_id)
        self.all_student.append(stu)
        print('添加成功！')

    def del_stu(self):
        name = input('请输入删除学生姓名:')
        for stu in self.all_student:
            if stu.name == name:
                self.all_student.remove(stu)
                print('删除成功！')
                break
        else:
            print('没有该学生！')

    def call_stu(self):
        for stu in self.all_student:
            print(stu.name)
            stu.response()


c1 = Class('python1806')
c2 = Class('python1807')

for _ in range(2):
    c2.add_stu()
for stu in c2.all_student:
    stu.show()

for _ in range(2):
    c2.add_stu()
for stu in c2.all_student:
    stu.show()