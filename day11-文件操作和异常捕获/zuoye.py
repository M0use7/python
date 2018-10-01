"""__author__ = 唐宏进 """

import json
# 1.提取data.json中的数据，将每条数据中的name、text、love和comment信息。并且保存到另外一个json文件中
# with open('./files/data.json', 'r', encoding='utf-8') as f:
#     contents = json.load(f)
#     data = contents['data']
# f.close()
# list1 = []
# for msg in data:
#     new_data = {'name': msg['name'], 'text': msg['text'], 'love': msg['love'], 'comment': msg['comment']}
#     list1.append(new_data)
# with open('./files/new_data.json', 'w', encoding='utf-8') as f:
#     json.dump(list1, f, ensure_ascii=False, indent=4)
# f.close()

# 2.统计data.json中comment数量超过1000的个数
# with open('./files/data.json', 'r', encoding='utf-8') as f:
#     contents = json.load(f)
#     data = contents['data']
# f.close()
# count = 0
# for msg in data:
#     if int(msg['comment']) > 1000:
#         count += 1
# print(count)

# 3.将data.json文件中所有点赞数(love)对应的值超出1000的用k来表示，例如1000修改为1k, 1345修改为1.3k
# with open('./files/data.json', 'r', encoding='utf-8') as f:
#     contents = json.load(f)
#     data = contents['data']
# f.close()
# for msg in data:
#     if int(msg['love']) >= 1000:
#          msg['love'] = str(round(int(msg['love'])/1000, 1)) + 'k'
# with open('./files/data.json', 'w', encoding='utf-8') as f:
#     json.dump(contents, f, ensure_ascii=False, indent=4)
# f.close()

# 4.写猜数字游戏，如果输入有误，提示重新输入，直达输入正确为止。比如：输入数字的时候没有按要求输入，提示重新输入
# import random
# num = random.randint(0,100)
# try:
#     num1 = int(input('请输入数字(0-100):'))
#     while True:
#         if num1 == num:
#             print('恭喜你，猜对了！！！')
#             break
#         else:
#             if num1 > num:
#                 print('大了，再小点！')
#                 num1 = int(input('请重新猜:'))
#             else:
#                 print('小了，再大点！')
#                 num1 = int(input('请重新猜:'))
# except ValueError:
#     num1 = int(input('您的输入有误，请重新输入:'))

# 5.写学生管理系统的添加学生功能(数据需要本地化)，要求除了保存学生的基本信息以外还要保存学生的学号，但是学号需要自动生成
# 生成原则：
# 添加第一个学生对应的学号是:py001 第二次添加的学生的学号是:py002 ... 如果前面的学生因为各种原因被移除了，那后面
# 添加学生的时候原则不变，就是比如上次已经添加到py012,那么前面不管有没有删除情况，再次添加学生的学号是py013

# key_students = 'students'
# key_number = 'number'
# key_name = 'name'
# key_age = 'age'
# key_tel = 'tel'
# key_id = 'id'
# def read_data(filename):
#     try:
#         with open('./files/'+filename, 'r', encoding='utf-8') as f:
#             return json.load(f)
#     except:
#         return None
#
# def write_data(filename,contents):
#     try:
#         with open('./files/'+filename, 'w', encoding='utf-8') as f:
#             json.dump(contents, f, ensure_ascii=False, indent=4)
#             return True
#     except:
#         return False
#
# def get_system_info():
#     system_info = read_data('stu.json')
#     if system_info:
#         return system_info
#     else:
#         return {}
#
# def create_id():
#     system_info = get_system_info()
#     number = system_info.get(key_number,0)
#     number += 1
#     id = 'python' + str(number).rjust(3,'0')
#     return id,number
#
# while True:
#     print('===================')
#     print('1.添加学生\n2.退出')
#     print('===================')
#     value = input('请选择:')
#     if value == '1':
#         name = input('请输入学生名字:')
#         age = input('请输入学生年龄:')
#         tel = input('请输入学生电话:')
#         id,number = create_id()
#         stu = {key_name:name, key_age:age, key_id:id, key_tel:tel}
#         # 保存学生信息
#         system_info = get_system_info()
#         students = system_info.get(key_students,[])
#         students.append(stu)
#
#         # 保存到文件中
#         system_info[key_students] = students
#         system_info[key_number] = number
#         re = write_data('stu.json',system_info)
#         if re:
#             print('添加成功！')
#         else:
#             print('添加失败！')
#     elif value == '2':
#         break
#     else:
#         continue




