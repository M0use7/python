"""__author__ = 唐宏进 """

"""
json是没有特定格式的一种文本形式，它有自己的语法
json文件就是后缀是.json的文本文件

1.json格式对应的数据类型及其表现
a.每个json文件中只能存一个数据，这个数据的类型必须是以下类型中的一个
类型：                         格式：                     意义
对象(object):                  {"a":10,"b":[1,2]}         相当于字典
数组(array):                   [100,"abc",true,[1,2]]     相当于列表，里面的元素可以是任何类型
数字(number):                  0,100,3.14,-200            包含整数和小数                       
字符串(string):                "abc","hello jason"        相当于字符串
布尔                            true/false                是(真)/否(假)
null:                           null                      空值
"""

"""
2.python对json数据的支持
json       --->      python
对象                 字典(dict)
数组                 列表(list)
数字                 整数(int)和浮点数(float)
布尔/true,false      布尔(bool)/True,False
null                  None
"""
# json模块是python中内置的，专门用来处理json数据的一个模块
import json

"""
1.load(json文件对象)：以json的格式，获取文件中的内容。将内容转换成相应的python数据
2.loads(json格式内容的字符串，编码方式)：将json格式的字符串转换成python对应的数据
3.dump（需要写入json文件中的python数据，json文件对象）
4.dumps（需要转换成json格式字符串的python数据）
"""
# 1.json转python数据
with open('./files/json1.json', 'r', encoding='utf-8') as f:
    content = json.load(f)
    print(content)
    print(type(content))
    print(content[3])

content1 = json.loads('{"a":100, "abc":true}', encoding='utf-8')
print(content1,type(content1))

# 2. python转json数据
"""
python       --->          json
字典                        对象
列表，元祖                  数组
整数/浮点数                 数字
布尔/True,False             true,false
字符串                      字符串(双引号) 
None                        null
"""
with open('./files/new.json', 'w', encoding='utf-8') as f:
    json.dump({'a': 100, 'hn': 200},f)
    # json.dump((1,'a',True,3.14), f)
    # 注意：集合不能转换成python数据
    #json.dump({1,2,'a',True}, f)


# 将python数据，转换成json字符串
json_str = json.dumps([1,2,3,True,'abc'])
print(json_str,type(json_str))

# 练习：用json文件保存一个班的班级信息，包括班级名和班上的所有学生（名字、年龄和电话）
# 输入学生信息添加学生
# 根据姓名删除学生
# （做到数据持久化）
"""
{
    "class_name":"班级名",
    "all_students":[
        {"name":"名字", "age":年龄, "tel":"电话"}
        {"name":"名字", "age":年龄, "tel":"电话"}
        {"name":"名字", "age":年龄, "tel":"电话"}
    ]
}
"""
# 1.读出保存班级信息对应的json文件中的内容
with open('./files/class_info.json', 'r', encoding='utf-8') as f:
    class_content = json.load(f)
f.close()

# 2.输入信息添加数据
name = input('姓名:')
age = input('年龄:')
tel = input('电话:')
stu = {"name": name, "age": int(age), "tel": tel}

class_content['all_students'].append(stu)
# class_info = {
#     "class_name":"python",
#     "all_students":[
#         stu
#     ]
# }
# 3.将最新的数据写入文件中
with open('./files/class_info.json', 'w', encoding='utf-8') as f:
    json.dump(class_content,f)
f.close()

# 根据姓名删除学生
with open('./files/class_info.json', 'r', encoding='utf-8') as f:
    class_content = json.load(f)
f.close()
students = class_content['all_students']
del_stu = input('请输入要删除学生姓名:')

for stu in students:
    if del_stu == stu['name']:
        students.remove(stu)
        print('删除成功！')
with open('./files/class_info.json', 'w', encoding='utf-8') as f:
    json.dump(class_content, f)
f.close()
"""
1.将数据从文件中读出来
2.修改数据（增、删、改）
3.将新的数据再写入文件中
"""

