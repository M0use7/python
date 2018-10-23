"""__author__ = 余婷"""

# tuple(元祖)
# 元祖就是不可变的列表。列表中除了和可变相关的内容以外，其他的全部适用于元祖
# 不支持增、删除、修改，只支持和查相关的操作

# 1.声明元祖
tuple1 = (1, 2, 'abc', True, [1, 2])
print(tuple1, type(tuple1))

# 注意：如果要写一个元祖元素个数是1的字面量，需要在那一个元素的后面加逗号
t2 = (100,)
print(t2, type(t2), len(t2))

# () --> 空的元祖
t3 = ()
print(t3, type(t3))

# 2.查相关的
t3 = ('red', 'yellow', 'green', 'pink')
print(t3[2])
print(t3[0:3])

for item in t3:
    print(item)

# 3.特殊操作
point = (100, 200, 'red')
print(point[0], point[1])

# 通过两个变量来获取元祖中的唯一的两个元素的值
x, y, color = point
print(x, y)

# 通过在变量前加*,获取元祖/列表中的一部分元素值，结果是一个列表
user = ('小吕', 90, 98, 56, 100, '男')
name, *score, sex = user
print(name, score, sex)

user2 = ('小红', 90, 100, 89, 67, 78)
name, *score = user2
print(name, score)

*score, name, sex = (89, 98, 78, 67, '小蓝', 'boy')
print(score, name, sex)


# 4.多个值之间用逗号隔开，对应的数据也是元祖
a = 1, 2, 3, 4    # 相当于 a = (1, 2, 3, 4, 5)
print(a,  type(a))

x, y = 100, 200  # 相当于x,y = (100, 200)
print(x, y)

