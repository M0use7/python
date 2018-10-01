"""__author__ = 唐宏进 """

# 1.查：获取列表元素
# a.获取单个元素：列表[小标]
tv_name = ['请回答1988','琅琊榜','甄嬛传']
print(tv_name[1])
print(tv_name[-1])

# b.获取部分元素(切片):列表[小标1:下标2]/列表[小标1:下标2:步进]
# # 从小标1开始取到小标2前为止(注意:下标2的值取不到)
# # 步进正从前往后取，步进负从后往前取
# # 结果是列表;这里面的下标可以越界
print(tv_name[1:3])
print(tv_name[-1:-3:-1])

# c.遍历(一个一个的获取每个元素)
# 可以将列表直接放到for循环的in后面
# 循环过程中，for后面的变量取的是列表中每个元素
for item in tv_name:
    print(item)

# 练习:写一个列表来保存一个班的学生的成绩(6个)，统计班上成绩在80分以上的人的个数
count = 0
prade = [82,79,95,67,77,85]
for item in prade:
    if item > 80:
        count += 1
print(count)

# 2.改(修改元素的值)
# 语法：列表名[小标] = 新值 (通过下标获取元素，然后重新赋值)
person = ['小明',35,'乒乓球']

# 修改person列表中小标是1的元素的值，修改为25
person[1] = 25
person[2] = '篮球'
print(person)

# person[3] = '男' # 不能越界

# 3.增(增加列表的元素，添加元素)
# 注意：列表中元素个数发生改变后，列表中每个元素的下标也会重新分配
person.append('男')
print(person)

person.append('80')
print(person)

# b.列表.insert(下标,元素):在指定下标前插入一个元素
person.insert(0, '001')
print(person)

# 练习：录入5个学生的成绩，并且保存在一个列表中
# list = []
# for x in range(5):
#     grade = int(input("请输入成绩:"))
#     list.append(grade)
# print(list)

# 4.删(删除列表中的元素)
# a.del 列表[下标]
# del语句是python中删除数据的语法，他可以删除任何数据:del 变量变量(删除) del 列表名(删除整个列表)
foods = ['辣条','棒棒糖','大蒜','火锅','饼干']
del foods[2]
print(foods)

# b.列表.remove 元素
# 注意：如果这个元素在列表中有多个，只删除最前面那个
foods.remove('饼干')
print(foods)

# c.列表.pop(下标) -->将列表中指定下标对应的元素取出来
food = foods.pop(1) # 将foods中将下标是1的元素取出来，保存到变量food中
print(foods,food)
# 练习:想尽一切办法，将一个保存成绩的列表中，成绩低于60的全部删除
# [78,59,40,90,89,45,69,30] --> [78,90,89,69]
grade = [78, 59, 40, 90, 89, 45, 69, 30]
for x in grade[:]:
    if x < 60:
        grade.remove(x)
print(grade)

# 注意：以后遍历列表的元素的时候，我们一般遍历它的拷贝的值([:])



