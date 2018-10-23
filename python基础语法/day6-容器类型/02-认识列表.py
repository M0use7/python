"""__author__ = 余婷"""

"""
list(列表)
列表是python中的容器类型。有序的，可变的容器(可变指的是列表中的元素和元素的位置、个数可变)。
有序 -> 可以通过下标来获取元素
可变 -> 可以进行增删改(查)

元素：指的是列表中的每一个内容。列表中的元素可以是任意类型的数据

"""
# 1.列表的声明
# a.声明变量赋一个列表的值
# 声明了一个列表，列表中有5个元素，分别是90，80，97，67，55
scores = [90, 80, 97, 67, 55]
print(scores, type(scores))

# 声明了一个列表，列表中有3个元素，分别是'余婷',18,'女' （一个列表中的元素的类型可以不一样）
person = ['余婷', 18, '女']
print(person)

name = '王海飞'
age = 20
person2 = [name, age, '男']
print(person2)

# [] --> 代表空列表
names = []
print(names, type(names))

# b.将其他的数据类型转换成列表(只有序列才能转换：字符串和range,字典、元祖、集合、生成式和迭代器)
chars = list('abcdef')
print(chars)

numbers = list(range(10))
print(numbers)









