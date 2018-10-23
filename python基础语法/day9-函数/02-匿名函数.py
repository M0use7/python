"""__author__ = 余婷"""

"""
匿名函数本质还是函数，之前函数的所有的内容都适用于它

1.匿名函数的声明
函数名 = lambda 参数列表:返回值

2.说明:
函数名：变量名
lambda：声明匿名函数的关键字
参数列表: 参数名1,参数名2，....
冒号: 固定写法
返回值：表达式，表达式的值就是返回值

3.调用
匿名函数的调用和普通函数一样
函数名(实参列表)
"""
# 协议个匿名函数计算两个数的和
# 声明一个匿名函数
my_sum = lambda x, y: x+y
print(type(my_sum))

# 下面这个函数和 my_sum = lambda x, y: x+y等价的
# def my_sum(x, y):
#     return x+y

print(type(my_sum))

# 调用匿名函数
result = my_sum(10, 20)
print(result)


# 练习1：写一个匿名函数，获取指定的数字列表指定下标的值的1/2
# 匿名函数的参数可以设默认值
get_value = lambda list1, index=0: list1[index]/2

# 位置参数
print(get_value([1, 2, 3, 4, 5], 3))
print(get_value([1, 2, 3, 4, 5]))
# 关键字参数
print(get_value(index=1, list1=[10, 78, 29, 8]))


# 练习2: 获取一个列表的所有的元素的和和平均值(sum函数可以计算一个序列的和)
list_operation = lambda list1: (sum(list1), sum(list1)/len(list1))

sum1, average = list_operation([1, 2, 3, 4, 5, 6])
print(sum1, average)


# 补充：python中的函数可以有多个返回值的。就是在一个return后返回多个值，多个值之间用逗号隔开
def list_operation2(list1):
    return sum(list1), sum(list1)/len(list1)   # 最终是将多个返回值放到一个元祖中返回的


print(list_operation2([1, 2, 3, 4, 5, 6]))   # (21, 3.5)

"""
变量名 = lambda 参数列表:返回值  function
变量名 = [1, 2, 3]   list
变量名 = 100    int
"""






