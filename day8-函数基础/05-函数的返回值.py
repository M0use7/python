"""__author__ = 唐宏进 """

"""
1.返回值：函数的返回值就是return关键字后面的表达式的值。就是函数调用表达式的结果
2.python中所有的函数都有返回值，默认是None

说明：
a.如果函数体中没有return，函数的返回值就是None
b.调用函数的语句就是函数调用表达式
"""

# 写一个函数，打印'hello'
def say_hello():
    print('hello')

# 声明一个变量re，来保存函数调用后的结果
re = say_hello()
print(re)

# 2.return关键字（return只能写在函数中）
"""
a.确定返回值
b.结束函数(函数中只要遇到return，函数就直接结束)
c.单独的return相当于return None
"""

def fun1(n):
    print(n)
    return 100
    print('========')

re = fun1(10)
print(re)

# 练习：下面函数的返回值是多少？
def fun2():
    if False:
        return 200

print(fun2()) # None

"""
注意：看一个函数的返回值是多少，不是看函数中有没有return，而是看函数的执行过程中遇没遇到return
      遇到了，就是return后面的结果，否则就是None
"""
# 练习：写一个函数判断一个数是否是偶数，如果是返回Ture，否则返回False
def fun3(n):
    # if not n % 2:
    #     return True
    # else:
    #     return False
    return bool(n%2 == 0)

print(fun3(7))

"""
什么时候需要返回值？
只要实现函数的功能会产生新的数据，就通过返回值将新的数据返回，而不是打印它
"""
# 练习：
# 1.写一个函数，统计一个列表中浮点数的个数
def count_float(list:list):
    count = 0
    for item in list:
        if isinstance(item,float):
            count += 1
    return count

# 2.将一个列表中所有元素的值变成原来的二倍
def double_list(list:list):
    for x in range(len(list)):
        list[x] *= 2
    return list
# 3.写一个函数，获取指定元素对应的下标
def indexs(list:list, item):
    index_list = []
    for x in range(len(list)):
        if item == list[x]:
            index_list.append(x)
    return index_list
# 补充：判断一个值是否是指定的类型
# isinstance(值，类型) ---> 返回值是布尔
# isinstance(10,int)# 判断10是否是int类型
# print(isinstance(10.0,int))
list1 = [1.0, 2, 3, 2.5, 10.0 ,3]
print(count_float(list1))
print(double_list(list1))
print(indexs([1.0, 2, 3, 2.5, 10.0 ,3], 3))