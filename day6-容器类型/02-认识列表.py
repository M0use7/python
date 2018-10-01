"""__author__ = 唐宏进 """

"""
列表是python中的容器类型。有序的，可变的容器。(可变是列表中的元素和元素位置可变、个数可变)
元素：指的是列表中的每一个内容
有序 -> 可以通过下标来获取元素
可变 -> 可以增删改(查)
"""


# 1.列表的声明
# 声明了一个列表，列表中的5个元素，本别是90,80,97,67,55
scores = [90, 80, 97, 67, 55]
print(scores, type(scores))
# 声明了一个列表，列表中有3个元素，分别是'余婷', 18, '女'，(一个列表中的元素的类型可以不一样)
person = ['余婷', 18, '女']
print(person)
name = '王海飞'
age  = 20
person2 = [name,age]
print(person2)

# [] --> 代表空列表
names = []
print(names,type(names))

# 2.将其他类型的数据类型转换成列表(只有序列类型才能转换:字符串，字典，元祖，集合，生成式和迭代器)
chars = list('abcdef')
print(chars)

numbers = list(range(10))
print(numbers)
