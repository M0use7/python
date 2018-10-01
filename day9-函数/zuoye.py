"""__author__ = 唐宏进 """

# 1.写一个函数将一个指定的列表中的元素逆序
# 例如[1, 2, 3] -> [3, 2, 1])(注意：不要使用列表自带的逆序函数)
# negative_sequence = lambda list:list[::-1]
# print(negative_sequence(['a','b','c', 1, 2, 3]))

# 2.写一个函数，提取出字符串中所有奇数位上的字符
# odd_number_list = lambda str:str[1::2]
# print(odd_number_list('abc123'))

# 3.写一个匿名函数，判断指定的年是否是闰年
leap_year = lambda year:bool(not year % 4 and year % 100 or not year % 400)
print(leap_year())

# 4.使用递归打印：
# n = 3的时候
# @
# @@
# @@@
# n = 4的时候:
# @
# @@
# @@@
# @@@@

# def at(n):
#     if n == 1:
#         print('@')
#         return
#     at(n-1)
#     print('@' * n)
#
# at(5)
# 5..写函数，检查传入列表的长度，如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。
# def two_len_list(list:list):
#     if len(list) > 2:
#         return list[0:2]
#     else:
#         return list
#
# print(two_len_list(['a', 'b', 'c', 1, 2, 3]))

# 6.写函数，利用递归获取斐波那契数列中的第 10 个数，并将该值返回给调用者。（自己背着写）
# def fibo(n=10):
#     if n == 1 or n == 2:
#         return 1
#     return fibo(n-2) + fibo(n-1)
# print(fibo())

# 7.写一个函数，获取列表中的成绩的平均值，和最高分
# get_average_max = lambda list:(sum(list)/len(list),max(list))
# print(get_average_max([90,78,82,86,94]))

# 8.写函数，检查获取传入列表或元组对象的所有奇数位索引对应的元素，并将其作为新的列表返回给调用者
# odd_index = lambda list:list[1::2]
# print(odd_index(['a', 'b', 'c', 1, 2 , 3]))

# 9..写一个属于自己的数学模块(封装自己认为以后常用的数学相关的函数和变量)和列表模块（封装自己认为以
# 后常用的列表相关的操作）
# import my_list
# import my_math

# print(my_list.count1([2,4,1,2,53,12,2,23],2))
# print(my_list.sort1([2,4,1,53,12,23]))
# print(my_list.max1([2,4,1,53,12,23]))
#
# print(my_math.sum1(1,2,3))
# print(my_math.sum_add(10))
# print(my_math.sum_mul(5))
# print(my_math.fibo(7))

