"""__author__ = 余婷"""
"""
1.返回值：函数的返回值就是return关键字后面的表达式的值。就是函数调用表达式的结果
2.python中所有的函数都有返回值，默认是None(没有return)

说明：
a.如果函数体中没有return，函数的返回值就是None
b.调用函数的语句就是函数调用表达式


a.先回到函数声明的位置
b.用实参给形参赋值
c.执行函数体
d.将返回值返回给函数调用者
e.回到函数调用的位置(这个时候，函数调用表达式的值就是返回值)
"""

# 1.没有return
# 写一个函数，打印'hello'
def say_hello():
    print('hello')

# 声明一个变量re,来保存函数调用后的结果
# say_hello()
re = say_hello()
print(re)


# 2.return关键字（return只能写在函数体中）
"""
a. 确定返回值
b. 结束函数（函数中只要遇到return，函数就直接结束）
c. 单独的return相当于return None
"""
def func1(n):
    print(n)
    return 100
    print('=====')


re = func1(10)
print(re)


# 练习：下面的函数的返回值是多少？
def func2():
    if False:
        return 200

print(func2())  # None

"""
注意：看一个函数的返回值是多少，不是看函数中有没有return,而是看函数的执行过程中遇没有遇到return。
     遇到了，就是return后面的结果，否则就是None
"""


# 练习: 写一个函数判断一个数是否是偶数，如果是返回True,否则返回False
def is_even_number(number):
    if number % 2 == 0:
        return True
    return False

re = is_even_number(100)
print(is_even_number(100))
if is_even_number(100):
    print('是偶数')


def is_even_number2(number):
    if number % 2 == 0:
        print('偶数')
    else:
        print('奇数')

re = is_even_number2(91)

"""
什么时候函数需要返回值？
只要实现函数的功能会产生新的数据，就通过返回值将新的数据返回。而不是打印它
"""
# 练习：
# 1.写一个函数，统计一个列表中浮点数的个数
def count_of_float(list1:list):
    # 统计个数
    count = 0
    for item in list1:
        # 判断每个元素是否是浮点数
        if isinstance(item, float):
            count += 1
    return count

result = count_of_float([1, 90.9, 899, 'abc', 0.12, True])
print('这个列表的浮点数的个数是:%d' % result)



# 2.写一个函数，将一个数字列表中所有的元素的值都变成原来的二倍
def double_list(list1:list):
    for index in range(len(list1)):
        list1[index] *= 2
    return list1

list1 = [1, 2, 3, 4]
result = double_list(list1)
print(list1, result)

result = double_list([9, 8, 7, 6])
print(result)



# 3.写一个函数，获取指定元素对应的下标
def indexs(list1:list, item):
    # 保存符合要求的所有下标
    index_list = []
    for index in range(len(list1)):
        if list1[index] == item:
            index_list.append(index)

    return index_list

all_index = indexs([10, 'abc', 89, 10, 0.12, 10, 98], 10)
print(all_index)

# 将第二个200换成'abc'
numbers = [1, 200, 89, 200, 89, 87, 200, 9, 90]
all_index = indexs(numbers, 200)
numbers[all_index[1]] = 'abc'
print(numbers)

# [10, 'abc', 89, 10, 0.12, 10, 98]



# 补充: 判断一个值是否是指定的类型
# isinstance(值, 类型)  ---> 返回值是布尔
# isinstance(10, int) 判断10是否是int类型
print(isinstance(10.0, int))
str1 = True
print(isinstance(str1, str))












