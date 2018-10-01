"""__author__ = 唐宏进 """
from random import randint
import re
# def sum1(n:int):
#     sum = 0
#     for x in range(1,n+1):
#         sum += x
#     return sum
# print(sum1(100))

# def fun(n:int):
#     sum = 0
#     for x in range(1,n+1):
#         num = randint(1,6)
#         sum += num
#         print('第%d个骰子:%d' % (x,num))
#
#     print('%d个骰子的点数和:%d'% (n,sum))
#
# fun(5)

# def exchange(dict1:dict):
#     new_dict = {}
#     for item in dict1:
#         new_dict[dict1[item]] = item
#     return new_dict
# print(exchange({'a':1,'b':2,'c':3}))

# def get(str1):
#     global new_str
#     new_str = ''
#     for item in range(len(str1)):
#         if 'a'<=str1[item]<='z' or 'A'<=str1[item]<='Z':
#             new_str += str1[item]
#     return new_str
# print(get('12a&bc12d'))

# def start(n):
#     def a():
#         print('good')
#     if n == 1:
#         print('*'.center(10))
#         return
#     start(n - 2)
#     print(('*' * n).center(10))

# def nixu(list1):
#     list1.sort(reverse=True)
#     return list1
#
# print(nixu([1,2,3,4,5]))

# def fibo(n=7):
#     if n == 1 or n == 2:
#         return 1
#
#     return fibo(n-2)+fibo(n-1)
#
# print(fibo())

# list1 =[]
# list2 =[]
# for x in range(10):
#     def fun2(y):
#         print(x+y)
#     list1.append(fun2)
#     list2.append(fun2(x))
#
# print(list1)
# print(list2)
#
# list1[0](100)

print(re.fullmatch('^\d\d', '12'))