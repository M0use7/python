"""__author__ = 唐宏进 """

# 学生管理系统
# 1.一个系统可以存储多个学生
# 系统应该是一个容器：列表、字典

# 2.一个学生可以存储：姓名、电话、籍贯、学号等等
# 3.添加学生
# 4.删除学生
# 5.修改学生信息
#....

# 什么时候使用列表？ 什么时候使用字典
# 1.保存的多个数据的类型是同一个类型时候，用列表
# 例如：声明一个变量保存所有的数学成绩，声明一个变量保存所有的信息
#
# 2.保存的多个数据的类型不同，就使用字典
# 声明一个变量保存一个学生的信息

# 1.列表中有字典
student_system = [
    {'name':'stu1', 'age':18 , 'tel':123456, 'native_place':'四川.成都'},
    {'name': 'stu2', 'age': 21, 'tel': 654321, 'native_place': '重庆'}
]
# 获取第一个学生的籍贯
print(student_system[0]['native_place'])

# 2.字典中有列表
py_class = {
    'class_name':'python1806',
    'students':[
        {'name': 'stu1', 'age': 18, 'id': '001'},
        {'name': 'stu2', 'age': 19, 'id': '002'},
        {'name': 'stu3', 'age': 20, 'id': '003'}
    ]
}
# 取班级名字
print(py_class['class_name'])
# 去取第三个学生的名字
print(py_class['students'][2]['name'])

# 练习1：在班级python1806中添加一个学生
# name = input('姓名：')
# age = int(input('年龄：'))
# id = input('学号：')
# 一个学生对应一个字典
# student = {'name':name, 'age':age, 'id':id}
# 将学生对应的字典添加到列表中
# py_class['students'].append(student)
# print(py_class)

# 练习2：输入一个学生的姓名，根据姓名删除学生
py_class = {
    'class_name':'python1806',
    'students':[
        {'name': 'stu1', 'age': 18, 'id': '001'},
        {'name': 'stu2', 'age': 19, 'id': '002'},
        {'name': 'stu3', 'age': 20, 'id': '003'}
    ]
}
name1 = input('姓名：')
# 获取班级所有学生
all_student = py_class['students']

# 遍历取出每个学生对应字典
for stu_dict in all_student[:]:
    # 判断name对应的值是否和输入的要删除的姓名相同
    if stu_dict['name'] == name1:
        all_student.remove(stu_dict)
print(py_class)


