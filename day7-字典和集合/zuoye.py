"""__author__ = 唐宏进 """

def menu():

    print('=================')
    print('****学生管理系统****')
    print('1.添加学生')
    print('2.查看学生')
    print('3.修改学生')
    print('4.删除学生')
    print('5.退出')
    print('=================')

students = [
    {'name':'stu1', 'age':16, 'tel':'110'},
    {'name':'stu2', 'age':18, 'tel':'119'},
    {'name':'stu3', 'age':20, 'tel':'120'},
    {'name':'stu1', 'age':34, 'tel':'123'}
]
while True:

    menu()

    key = int(input('请选择功能(序号):'))

    while key not in range(1,6):
        key = int(input('选项不存在，请重输：'))
    if key == 1:
        while True:
            name = input('请输入姓名:')
            age = input('请输入年龄:')
            tel = input('请输入电话:')
            student = {'name': name, 'age': age, 'tel': tel}
            students.append(student)
            print('添加成功！')
            print('1.继续\n2.退出')
            value = input('>>>')
            if value == '2':
                break
        for stu in students:
            print(stu)

    elif key == 2:
        print('1.查看单个学生信息')
        print('2.遍历所有学生信息')
        key1 = int(input('请选择查看项(序号):'))
        if key1 == 1:
            name = input('请输入查看学生姓名:')
            for stu in students:
                if stu['name'] != name:
                    continue
                print(stu)
                print('是否是您要查找的学生(Y/N)')
                value = input('>>>')
                if value == 'N':
                    continue

        elif key1 == 2:
            for stu in students:
                    print(stu)
        else:
            print('输入有误，请重新输入！')

    elif key == 3:
       name = input('请输入需要修改学生姓名:')
       for stu in students:
           if stu['name'] != name:
               continue
           print(stu)
           value = input('是否需要修改该学生信息(Y/N):')
           if value == 'N':
               continue
           new_tel = input('请输入新的电话号码:')
           stu['tel'] = new_tel
           print('修改成功!')
       for stu in students:
           print(stu)

    elif key == 4:
        name = input('请输入删除学生姓名:')
        for stu in students:
            if stu['name'] != name:
                continue
            print(stu)
            print('是否需要删除学生(Y/N):')
            value = input('>>>')
            if value == 'N':
                continue
            students.remove(stu)
            print('删除成功')
        for stu in students:
            print(stu)

    elif key == 5:
        print('欢迎使用本系统！')
        break












