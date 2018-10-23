"""__author__ = 余婷"""

# 学生管理系统
# 1.一个系统可以存储多个学生
# 系统应该是一个容器：列表、字典
# 2.一个学生可以存储：姓名，电话，籍贯，专业，学号等等
# 3.添加学生
# 4.删除学生
# 5.修改学生的信息
# .....

# 什么使用列表？  什么时候使用字典？
# 1.保存的多个数据的类型是同一个类型时候，用列表
# 例如：声明一个变量保存所有的数学成绩， 声明一个变量保存所有的学生信息

# 2.保存的多个数据的类型不同，就使用字典
# 声明一个变量保存一个学生的信息


# 1.列表中有字典
student_system = [
    {'name': 'stu1', 'age': 18, 'tel': 110, 'native_place': '四川.成都'},
    {'name': 'stu2', 'age': 20, 'tel': 120, 'native_place': '重庆'}
]

# 取出第一个学生的籍贯
print(student_system[0]['native_place'])

# 2.字典中有列表
py_class = {
    'class_name': 'python1806',
    'students': [
        {'name': 'studen1', 'age': 20, 'id': '001'},
        {'name': 'studen2', 'age': 30, 'id': '002'},
        {'name': 'studen3', 'age': 18, 'id': '003'}
    ]
}

# 取班级名
print(py_class['class_name'])
# 取第三个学生的名字
print(py_class['students'][2]['name'])


# 练习1：在班级python1806中添加一个学生,学生的信息自己输入，名字、年龄和id
name1 = input('姓名:')
age1 = int(input('年龄:'))
id1 = input('id:')
# 一个学生对应一个字典
student = {'name': name1, 'age': age1, 'id': id1}
# 将学生对应的字典添加到列表中
py_class['students'].append(student)
print(py_class)

# 练习2：输入一个学生的姓名，根据姓名去删除对应的学生
del_name = input('请输入需要删除的学生姓名:')
# 获取班级所有的学生
all_student = py_class['students']
# 遍历取出每个学生对应的字典
for student_dict in all_student[:]:
    # 判断name对应的值是否和输入的要删除的姓名相同
    if student_dict['name'] == del_name:
        all_student.remove(student_dict)

print(py_class)






