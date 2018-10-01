"""__author__ = 唐宏进 """
import file_manager

user_name = ''

# =====================添加学生======================
"""
一个账号对应管理不同的学生 --- 不同的用户对应不同的json文件

json文件中的格式:
{
    'name':''
    'number':个数，
    'all_students':[]
}
"""
key_number = 'number'
key_all_students = 'all_students'
key_name = 'name'
key_age = 'age'
key_tel = 'tel'
key_id = 'id'


def get_system_info():
    # 获取系统文件内容
    system_info = file_manager.read_json_file(user_name+'.json')
    if system_info:
        return system_info
    return {}


def create_id():
    # 产生学号
    system_info = get_system_info()
    number = system_info.get(key_number,0)
    number += 1
    id = 'python' + str(number).rjust(3,'0')
    return id,number


def add_student():
    while True:
        # 1.输入信息
        name = input('姓名:')
        age = input('年龄:')
        tel = input('电话:')

        # 2.产生id
        id,number = create_id()

        # 3.创建学生
        stu = {key_name:name, key_age:age, key_tel:tel, key_id:id}

        # 4.保存学生信息
        system_info = get_system_info()
        all_studnets = system_info.get(key_all_students,[])
        all_studnets.append(stu)

        # 5.保存到文件中
        system_info[key_all_students] = all_studnets
        system_info[key_number] = number
        re = file_manager.write_json_file(user_name+'.json',system_info)
        if re:
            print('添加成功！')
        else:
            print('添加失败！')
        print('1.继续添加')
        print('2.返回')
        value = input('请选择:')
        if value == '1':
            continue
        else:
            break
# ====================查找学生=======================
def find_student():
    print('1.查看所有学生')
    print('2.根据姓名查找')
    print('3.根据学号查找学生')

    value = input('请选择(1-3):')
    all_students = get_system_info().get(key_all_students,[])
    if not all_students:
        print('目前还没有学生！')
        return
    # 查找所有学生
    if value == '1':
        for stu in all_students:
            print('姓名:%s 学号:%s 年龄:%s 电话:%s'%(stu[key_name],stu[key_id],stu[key_age],stu[key_tel]))

    elif value == '2':
        name = input('请输入查找学生姓名:')
        for stu in all_students:
            if stu[key_name] == name:
                print('姓名:%s 学号:%s 年龄:%s 电话:%s' % (stu[key_name], stu[key_id], stu[key_age], stu[key_tel]))
                return
        print('您查找的学生不存在！')
    elif value == '3':
        id = input('请输入学号:')
        for stu in all_students:
            if stu[key_id] == id:
                print('姓名:%s 学号:%s 年龄:%s 电话:%s' % (stu[key_name], stu[key_id], stu[key_age], stu[key_tel]))
                return
        print('您查找的学生不存在！')
    else:
        print('输入错误，请重新输入！')
# =====================删除学生======================
def del_student():
    print('1.删除所有学生')
    print('2.根据姓名删除学生')
    print('3.根据学号删除学生')
    value = input('请选择(1-3):')
    # 获取所有学生
    system_info = get_system_info()
    all_students = system_info[key_all_students]
    if not all_students:
        print('目前还没有学生！')
        return

    if value == '1':
        sure = input('您确认要删除所有学生？(YES/NO)')
        if sure == 'YES':
            all_students.clear()
            print('删除成功！')

    elif value == '2':
        name = input('请输入删除学生姓名:')
        for stu in all_students:
            if stu[key_name] == name:
                all_students.remove(stu)
                print('删除成功！')

    elif value == '3':
        id = input('请输入删除学生学号:')
        for stu in all_students:
            if stu[key_id] == id:
                all_students.remove(stu)
                print('删除成功！')

    # 保存学生信息到文件中
    system_info[key_all_students] = all_students
    file_manager.write_json_file(user_name+'.json',system_info)

# =====================修改学生======================
def alter_student():
    print('1.根据姓名修改学生')
    print('2.根据学号修改学生')
    value = input('请选择(1-2):')

    # 获取所有学生
    system_info = get_system_info()
    all_students = system_info.get(key_all_students,[])

    if value == '1':
        name = input('请输入需修改学生姓名:')
        for stu in all_students:
            if stu[key_name] == name:
                stu[key_tel] = input('请输入新的电话号码:')
                print('修改成功！')
    elif value == '2':
        id = input('请输入需修改学生学号:')
        for stu in all_students:
            if stu[key_id] == id:
                stu[key_tel] = input('请输入新的电话号码:')
                print('修改成功！')
    else:
        print('输入错误，请重新输入！')
    # 保存学生信息到文件中
    system_info[key_all_students] = all_students
    file_manager.write_json_file(user_name+'.json',system_info)

# =======================主页========================
def main_page():
    while True:
        print(file_manager.read_text_file('system.txt'))
        value = input('请选择(1-5):')

        # 1.返回
        if value == '5':
            break
        elif value == '1':
            add_student()
        elif value == '2':
            find_student()
        elif value == '3':
            del_student()
        elif value == '4':
            alter_student()
        else:
            print('输入有误,请重新输入！')
