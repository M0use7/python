"""__author__ = 唐宏进 """

"""
1.为什么要使用异常捕获
异常：程序崩溃了，报错了....

程序出现某种异常，但是不想因为这个异常而让程序崩溃。这个时候就可以使用异常捕获机制

2.怎么捕获异常
# a.形式1：捕获try后代码块里面的所有异常
try:
    需要捕获异常的代码块(可能会出现异常的代码块)
except:
    出现异常后执行的代码

执行过程：执行try后面的代码块，一旦遇到异常，就马上执行except后面的代码块。执行完后再执行其他的语句
           如果try里面的代码块没有出现异常，就不执行except后面的代码块。再执行其他的语句

b.形式2：
try:
    需要捕获异常的代码块(可能会出现异常的代码块)
except 错误类型:
    出现异常后执行的代码

执行过程：执行try后面的代码块，一旦遇到指定的异常，就马上执行except后面的代码块。执行完后再执行其他的语句
           如果try里面的代码块没有出现指定的异常，就不执行except后面的代码块。再执行其他的语句

c.形式3：
try:
    需要捕获异常的代码块(可能会出现异常的代码块)
except (错误类型1,错误类型2):
    出现异常后执行的代码

d.形式4:：
try:
    需要捕获异常的代码块(可能会出现异常的代码块)
except (错误类型1):
    出现异常后执行的代码
except (错误类型2):
    出现异常后执行的代码

e.形式5：
try:
    pass
except:     
    出现异常后执行代码
finally:
    不管有没有异常都会执行（就算崩溃了也会执行）
    （在这儿做程序异常退出时的善后，一般做保存数据和进度的工作）

"""

import json
# 1.什么情况...
# a.输入两个数，然后求这两个数的商是多少
# num1 = float(input('除数:'))
# num2 = float(input('被除数:'))
# print('%f / %f = %f' % (num1,num2,num2/num1))

# b.打开一个不存在的文件，不希望程序崩溃，只是让读出来的内容是空
# with open('./files/info.json', 'r', encoding='utf-8') as f:
#     content = json.load(f)

# 2.捕获异常
# try-except
a = [1, 2, 3, 4, 5]
try:
    print(int('abc'))
    # print(a[6])
except:
    print('捕获到异常')
print('=============')

dict1 = {'a':1, 'b': 2}
try:
    print(a[6])
    dict1['c']
except IndexError:
    print('下标越界')
except KeyError:
    print('key错误')

try:
    num1 = float(input('除数:'))
    num2 = float(input('被除数:'))
    print('%f / %f = %f' % (num2, num1, num2 / num1))
except ValueError:
    print('输入错误,请重新输入！')
    num1 = float(input('除数:'))
    num2 = float(input('被除数:'))
try:
 with open('./files/info.json', 'r', encoding='utf-8') as f:
    content = json.load(f)
    print(content)
except FileNotFoundError:
    content = ''
    print(content)