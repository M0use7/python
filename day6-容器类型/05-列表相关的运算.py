"""__author__ = 唐宏进 """

# 1.+操作
# 列表1 + 列表2：将列表1中的元素和列表2中的元素一次合并，产生一个新的列表
a = [1,2]
list1 = a + ['abc',100]
print(list1)

# 2.*操作
# 列表1*N:将列表1中的元素重复N次，然后产生一个新的列表
list2 = a * 3
print(list2)

# 3.in/not in
# 元素 in 列表：判断一个元素是否在列表中
print(10 in [1,2,3,10])

# 4.获取列表的长度
# len(序列)
name = ['海贼','一拳超人','一人之下','进击的巨人']
print(len(name))

# 5.相关的方法
num = [1,2,1,11,1,20,]
# 5.1列表.count(元素):统计指定的元素在指定的列表中有多少个
print(num.count(1))

# 5.2 列表.extend(序列)：将序列中的元素添加到列表中
# num.extend([100,200])
num.extend('abc')
print(num)

# 5.3 列表.index(元素)：获取指定元素的第一个下标
index1 = num.index(1)
print(index1)

# 5.4 列表.pop():将列表中的的最后一个元素从列表中去取出来
item = num.pop()
print(item,num)

# 5.5 列表.reverse()：列表中的元素反序
num = [1,20,3,40,5]
num.reverse()
print(num)

# 5.6 列表.sort():对列表进行排序(默认是升序)
# 列表.sort(reverse = Ture):对列表进行降序排序
num.sort(reverse = True)
print(num)

# 5.7 列表.clear():将列表中的元素全部清除
num.clear()
print(num)

# 5.8 列表.copy():将列表中的元素全部拷贝一份产生一个新的列表，相当于列表[:]
num = [1,2,3,4]
num1 = num.copy()
print(num1)


