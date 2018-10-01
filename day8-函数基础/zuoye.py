"""__author__ = 唐宏进 """

# 1.编写一个函数，求1+2+3+...+N
# def my_sum(n:int):
#     sum = 0
#     for x in range(1,n+1):
#         sum += x
#     return sum
# print(my_sum(100))

# 2.编写一个函数，求多个数中的最大值
# def max_num(*num):
#     return max(num)
# print(max_num(1,23,14,5,8))

# 3. 编写一个函数，实现摇骰子的功能，打印n个骰子的点数和
# import random
# def dian_sum(n):
#     sum = 0
#     for item in range(1,n+1):
#         num = random.randint(1,6)
#         sum += num
#         print('第%d次骰子数为：%d'%(item,num))
#     return sum
# print(dian_sum(3))

# 4.编写一个函数，交换指定字典的key和value。
# 例如:{'a':1, 'b':2, 'c':3} ---> {1:'a', 2:'b', 3:'c'}
# def change_dict(dict:dict):
#     new_dict = {}
#     for item in dict:
#         new_dict.setdefault(dict[item],item)
#     return new_dict
# print(change_dict({'a':1, 'b':2, 'c':3}))

# 5.编写一个个函数，三个数中的最大值
# def largest(a,b,c):
#     list = [a,b,c]
#     return max(list)
# print(largest(12,5,7))

# 6.编写一个函数，提取指定字符串中的所有的字母，然后拼接在一起后打印出来
# 例如：'12a&bc12d--' ---> 打印'abcd'
# def print_words(str:str):
#     new_str = ''
#     for item in range(len(str)):
#         if str[item].isalpha():
#             new_str += str[item]
#     return new_str
# print(print_words('12a&bc12d'))

# 7.写一个函数，求多个数的平均值
# def average(*num):
#     length = len(num)
#     sum1 = sum(num)
#     avg = sum1 / length
#     return avg
# print(average(3,7.5,12,23))

# 8.写一个函数，默认求10的阶层，也可以求其他数的阶层
# def jie_cheng(n=10):
#     sum = 1
#     for item in range(1,n+1):
#         sum *= item
#     return sum
# print(jie_cheng())
# print(jie_cheng(5))

# 9.写一个函数，可以对多个数进行不同的运算
# 例如: operation('+', 1, 2, 3) ---> 求 1+2+3的结果
#  operation('-', 10, 9) ---> 求 10-9的结果
#  operation('*', 2, 4, 8, 10) ---> 求 2*4*8*10的结构
def yun_suan(str:str,*num):
    if str == '+':
        return sum(num)

    elif str == '-':
        sub = num[0]
        for item in range(1,len(num)):
            sub -= num[item]
        return sub

    elif str == '*':
        mul = num[0]
        for item in range(1,len(num)):
            mul *= num[item]
        return mul

    elif str == '/':
        div = num[0]
        for item in range(1,len(num)):
            div /= num[item]
        return div
    elif str == '%':
        mod = num[0]
        for item in range(1,len(num)):
            mod %= num[item]
        return mod

    elif str == '//':
        div_int = num[0]
        for item in range(1,len(num)):
            div_int //= num[item]
        return div_int

    elif str == '**':
        jie_cheng = num[0]
        for item in range(1,len(num)):
            jie_cheng **= num[item]
        return jie_cheng
    else:
        print('输入错误！')

print('%d %s %d = %.2f'%(9,'+',2,yun_suan('+',9,2)))
print('%d %s %d = %.2f'%(9,'-',2,yun_suan('-',9,2)))
print('%d %s %d = %.2f'%(9,'*',2,yun_suan('*',9,2)))
print('%d %s %d = %.2f'%(9,'/',2,yun_suan('/',9,2)))
print('%d %s %d = %.2f'%(9,'%',2,yun_suan('%',9,2)))
print('%d %s %d = %.2f'%(9,'//',2,yun_suan('//',9,2)))
print('%d %s %d = %.2f'%(9,'**',2,yun_suan('**',9,2)))