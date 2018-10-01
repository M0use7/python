"""__author__ = 余婷"""

# 设计一个学生管理系统，可以用来保存多个学生的信息
# 添加学生
# 修改学生信息
# 删除学生

# 1.声明一个列表保存所有的学生
all_student = []

# 2.添加学生(分析出一个学生应该对应的是一个字典)
while True:
    name = input('姓名:')
    age = input('年龄:')
    tel = input('电话:')
    student = {'name': name, 'age': age, 'tel_num': tel}
    all_student.append(student)
    print('添加成功!')
    print('1.继续\n2.退出')
    value = input('请选择:')
    if value == '2':
        break

print(all_student)

# 3.修改学生信息
all_student = [
    {'name': 'a', 'age': '23', 'tel_num': '1224124'},
    {'name': 'b', 'age': '23', 'tel_num': '234124'},
    {'name': 'a', 'age': '234', 'tel_num': '2313412'}
]
name = input('请输入需要修改的学生的名字:')
# 去找到输入的名字对应的学生
for stu in all_student:
    if stu['name'] != name:
        continue
    # 名字相等的时候
    print(stu)
    value = input('是否需要修改该学生信息(Y/N):')
    if value == 'N':
        # 如果不想修改就继续查找下一个学生
        continue

    # 修改
    new_tel = input('请输入新的电话号码:')
    stu['tel_num'] = new_tel
    print('修改成功!')

print(all_student)


