"""__author__ = 余婷"""

# 字典(dict)
"""
1.字典是容器类型(序列)，以键值对作为元素（字典里面存的数据全是以键值对的形式出现的）
{key1:value1, key2:value2...}
2.键值对： 键:值(key:value)
键(key): 要唯一，不可变的(数字、布尔、字符串和元祖，推荐使用字符串)
值(value):可以不唯一，可以任何类型的数据

3.字典是可变(增删改) --- 可指的是字典中的键值对的值和个数可变
"""
# 1.声明字典
dict1 = {10: 100, 'a': 97, True: 100, (10, 10): 'start', 'a': [1, 2]}
print(dict1)

person1 = ['酒坛坛儿', 20, 5, 90]

# 声明一个字典，有三个键值对儿，key分别是:name， age和work_age
person2 = {'name': '酒坛坛儿', 'age': 20, 'work_age': 5}

dict2 = {}  # 空的字典
print(type(dict2))


# 2.查(获取值)
# 获取字典的元素对应的值（字典存数据，实质还是存的value, key是获取value的手段）
# a.字典[key] --- 通过key获取值
print(person2['name'], person2['age'])

# 通过字典[key]获取value的时候,如果key不存在会发生KeyError异常
# print(person2['sex'])    # KeyError: 'sex'

# b.字典.get(key)
print(person2.get('age'))
# 字典.get(key),如果key不存在不会报错，返回None
print(person2.get('sex'))  # None -- python中的特殊值，代表没有

# print(person2.get('name2'))

# 总结: 确定key肯定存在的时候用[]语法获取value。
#      key值可能不存在，不存的时候不希望报错，而是想要自己对它进行特殊处理的时候使用get获取value
person = {'name': '叶玉', 'age': 17, 'grade': 90, 'sex': 'girl'}
# 想要获取性别sex，如果没有就默认为'男'
if person.get('sex') != None:
    print(person['sex'])
else:
    print('男')


# c. 遍历字典
dog = {'name': '旺财', 'color': 'yellow', 'age': 3}
# 遍历字典直接取到是字典的所有的key值
for key in dog:
    # 打印key
    print(key)
    print(dog[key])


# 3.改(修改key对应的value)
# 字典[key] = 新值  （key是本来就存在）
dog['name'] = '大黄'
print(dog)

# 4.增(添加键值对)
# 字典[key] = 值   （key本来不存在）
dog['type'] = '土狗'
print(dog)

# 5.删(删除键值对)
# a.del 字典[key]
del dog['age']
print(dog)

# b.字典.pop(key)
color = dog.pop('color')
new_dict = {'a': color}
print(color, dog)
print(new_dict)



























