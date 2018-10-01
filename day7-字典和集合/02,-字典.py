"""__author__ = 唐宏进 """

# 字典(dict)
"""
1.字典是容器类型（序列）、以键值对作为元素（字典里面存的数据全是以键值对的形式出现）
{key1:value1,key2:value2...}
2.键值对：键:值(key:value)
键(key)：要唯一，不可变的(数字、布尔、字符串和元祖，推荐使用字符串)
值(value)：可以不唯一，可以是任何类型的数据
3.字典是可变（增删改) --- 可变指的是字典中的键值对的值和个数可变
"""
# 1.声明字典
dict1 = {10:100, 'a':97, True:100, (10,10):'start', 'a':'A'}
print(dict1)

person1 = ['余婷',20,5]

# 声明一个字典，有三个键值对，key分别是:name,age和work_age
person2 = {'name':'余婷','age':20,'work_age':5}

dict2 = {} # 空的字典
print(type(dict2))
# 2.查（获取值）
# 获取字典的元素对应的值（字典存数据，实质存的value,key是获取value的手段）
# a.字典[key] --- 通过key获取值
print(person2['name'])

# 通过字典[key]获取value的时候，如果key不存在会发生keyError异常
# print(person2['sex']) # KeyError: 'sex'

# b.字典.get(key)
print(person2.get('age'))
# 字典.get(key),如果key不存在不会报错，返回None
print(person2.get('sex')) # None -- python中的特殊值，代表没有

# 总结：确定key值肯定存在的时候用[]语法获取value。
#       key值可能不存在，不存在的时候不希望报错，而是想要自己对它进行特殊t处理的时候使用get获取value
person = {'name':'叶玉', 'age':17, 'grade':90}
# 想要获取性别，如果没有就默认为'男'
if person.get('sex') != None:
    print(person['sex'])
else:
    print('男')

# c.遍历字典
# 遍历字典直接取到的是字典的所有key值
for x in person2:
    print(x,end = ' ')
    print(person2[x])

# 3.改（修改key对应的值）
# 字典[key] = 新值 （key是本来就存在）
person2['name'] = '酒坛坛儿'
print(person2)

# 4.增加（添加键值对）
# 字典[key] = 值   （key本来不存在）
person2['sex'] = '女'
print(person2)

# 5.删（删除键值对）
# a.del 字典[key]
del person2['work_age']
print(person2)

# b.字典.pop(key)
name = person2.pop('name')
print(name,person2)

