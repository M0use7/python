"""__author__ = 唐宏进 """

class Student:
    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id

    def response(self):
        print('%s到'% self.name)

    def show(self):
        print(self.__dict__)

class Class:
    def __init__(self, class_name):
        self.student = []
        self.class_name = class_name
        self.__count = 0

    def add(self):
        name = input('学生姓名:')
        age = input('学生年龄:')

        self.__count += 1
        id = 'python'+str(self.__count).rjust(3,'0')
        stu = Student(name,int(age),id)
        self.student.append(stu)
        print('添加成功！')
        stu.show()

    def del_stu(self):
        name = input('请输入删除学生姓名:')

        for stu in self.student[:]:
            if stu.name == name:
                self.student.remove(stu)
                print('删除成功！')
                break
        else:
            print('没有该学生！')


    def call(self):
        for stu in self.student:
            print(stu.name)
            stu.response()

stu1 = Student('张三', 21, 'python001')
stu1.show()

c1 = Class('python三班')
print(c1._Class__count)
for _ in range(4):
    c1.add()
c1.del_stu()
c1.call()

