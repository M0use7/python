"""__author__ = 唐宏进 """

# tuple(元祖)
# 元祖就是不可变的列表。列表中除了和可变相关的内容以外，其他的全部适用于元祖
# 不支持增加、删除、修改，只支持查找
# 1. 声明元祖
tuple1 = (1,2,3,10)

# 注意：如果要写一个元祖元素个数是1的字面量，需要在那一个元素后面加逗号
t2 = (100,)
print(t2,type(t2))

# 2.查相关的元素
t3 = ('red','yellow','green','pink')
print(t3[2])
print(t3[0:3])

for item in t3:
    print(item)

# 3.特殊操作
point = (100,200,'red')
print(point[0],point[1])

# 通过两个变量来获取元素中唯一的两个元素的值
x,y,color = point
print(x,y)

# 通过在变量加*,获取元祖/列表中的一部分元素值，结果是一个列表
user = ('小吕',90,98,56,'男')
name,*score,sex = user
print(name,score,sex)

# 多个值之间用逗号隔开，对应的数据也是元祖
a = 1, 2, 3, 4 # 相当于 a = (1, 2, 3, 4 )
print(a,type(a))

x,y = 100,200 # x,y = (100,200)
print(x,y)
