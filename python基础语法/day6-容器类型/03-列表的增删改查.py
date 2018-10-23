"""__author__ = 余婷"""

# 1.查: 获取列表元素
# a.获取单个元素：列表[下标]
# 下标范围:0 ~ 元素个数-1 或者 -1 ~ -元素个数
# 注意: 下标不能越界
tv_names = ['请回答1988', '琅琊榜', '甄嬛传', '生活大爆炸', '尼基塔']
print(tv_names[0])
print(tv_names[1])
print((tv_names[-1]))
# print(tv_names[10])  # IndexError: list index out of range

# b.获取部分元素(切片): 列表[下标1:下标2] / 列表[下标1:下标2:步进]
# 从下标1开始获取下标2前为止(注意：下标2对应的值是取不到)
# 步进值是正的就从前往后取，步进是负的就从后往前取
# 结果是列表;这儿的下标可以越界
print(tv_names[1:3])  # ['琅琊榜', '甄嬛传']
print(tv_names[-1:-4:-1])  # ['尼基塔', '生活大爆炸', '甄嬛传']
print(tv_names[:4])  # ['请回答1988', '琅琊榜', '甄嬛传', '生活大爆炸']
print(tv_names[3:])  # ['生活大爆炸', '尼基塔']
print(tv_names[:])   # ['请回答1988', '琅琊榜', '甄嬛传', '生活大爆炸', '尼基塔']

# c.遍历(一个一个的获取每个元素)
# 可以将列表直接放到for循环的in的后边。
# 循环过程中，for后面的变量取的是列表中的每个元素
for item in tv_names:
    print(item)

# 练习:写一个列表来保存一个班的学生的成绩(6个)，统计班上成绩在80分以上人的个数
scores = [89, 90, 67, 65, 81, 78]
count = 0  # 统计个数
for score in scores:
    if score > 80:
        count += 1
print(count)


# 2.改(修改元素的值)
# 语法: 列表名[下标] = 新值  （通过下标获取元素，然后重新赋值）
# 注意：下标不能越界
person = ['小明', 35, '乒乓球']

# 修改person列表中下标是1的元素的值，修改为25
person[1] = 25
print(person)

person[2] = '篮球'
print(person)

# person[3] = '男'  # IndexError: list assignment index out of range

# 3.增(增加列表的元素,添加元素)
# 注意: 列表中元素的个数发生改变后，列表中每个元素的下标会根据新的位置重新分配
# a.列表.append(元素) : 在列表的最后去添加一个元素
person.append('男')
print(person)

person.append(80)
print(person)

# b.列表.insert(下标,元素) : 在指定的下标前插入一个元素
person.insert(0, '001')
print(person)
print(person[1])

person.insert(2, 'H5')
print(person)

# 练习：录入(输入)5个学生的成绩，并且保存在一个列表中
# scores = []
# for _ in range(5):
#     score = input("请输入学生的成绩:")
#     scores.append(int(score))
#
# print(scores)
"""
scores = []
_ = (0,1,2,3,4)
_ = 0   score = 20  [20]
_ = 1   score = 80  [20, 80]
...
"""

# 4.删(删除列表中的元素)
# a. del 列表[下标]  ---> 根据下标去删除列表中的元素
# del 语句是python中删除数据的语法，它可以删除任何数据: del 变量(删除变量)  del 列表(删除整个列表)
foods = ['辣条', '棒棒糖', '大蒜', '火锅', '饼干', '小龙虾', '大虾', '花甲']
del foods[2]  # 删除下标是2的元素
print(foods)

del foods[4]
print(foods)

# b. 列表.remove(元素) ---> 删除列表中的某个值
# 注意：如果这个元素在列表中有多个，只删除最前面的那一个
foods.remove('饼干')
print(foods)

# c. 列表.pop(下标)  ---> 将列表中指定下标对应的元素取出来
food = foods.pop(1)  # 将foods中下标是1对应的元素取出来，保存到变量food中
print(foods, food)

# 练习：想尽一切办法，将一个保存成绩的列表中，成绩低于60分的全部删除
# [78, 59, 40, 90, 89, 45, 69, 30]  --> [78, 90, 89, 69]
scores = [78, 59, 40, 90, 89, 45, 69, 30]
for score in scores[:]:
    if score < 60:
        scores.remove(score)
print(scores)

# 注意：以后遍历列表的元素的时候，我们一般遍历它的拷贝的值([:])
"""
scores = [78, 90, 89, 69]
[:] = [78, 59, 40, 90, 89, 45, 69, 30]

"""



























