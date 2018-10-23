"""__author__ = 余婷"""

"""
1.什么是递归函数?
在函数的函数体中调用函数本身，这样的函数就是递归函数

2.递归的特点
while循环能做的事情，递归都可以做
"""


# 这儿的func1就是递归函数
def func1():
    print('aaaa')
    func1()

# func1()


"""
3.怎么写递归函数
第一步: 找临界值 (找到让循环结束的值/找到能够确定函数结果值)
第二步: 假设函数的功能已经实现的前提下，找关系 (找f(n)和f(n-1)/当次循环和上次循环的关系)
第三步：根据f(n)和f(n-1)的关系，来通过f(n-1)实现f(n)的效果
"""
# 1+2+3+4+...+100
sum1 = 0
for x in range(101):
    sum1 += x
print(sum1)


# 用递归实现1+2+3...+n
def my_sum(n):
    # 1.找临界值(在临界值的位置一定要让函数结束)
    if n == 0:
        return 0

    # 2.找关系
    """
    my_sum(n) : 1+2+3+...+n-1+n
    my_sum(n-1) : 1+2+3+...+n-1
    my_sum(n) = my_sum(n-1)+n
    """
    # 3.使用f(n-1)实现f(n)的效果
    return my_sum(n-1) + n

print(my_sum(5))

"""
my_sum(5) n=5  return 1+2+3+4+5 = 15
my_sum(4) n=4  return 1+2+3+4
my_sum(3) n=3  return 1+2+3
my_sum(2) n=2  return 1+2
my_sum(1) n=1  return 0+1
my_sum(0) n=0  return 0
"""


# 练习：使用递归计算斐波那契数列中1,1,2,3,5,8,13,21...第n个数
def sequence(n):
    # 1.找临界值
    if n == 1 or n == 2:
        return 1

    # 2.找关系
    """
    sequence(n) = sequence(n-1) + sequence(n-2)
    """
    return sequence(n-1) + sequence(n-2)

print(sequence(4))

# 练习：使用递归完成以下的效果:
"""
n=3
***
**
*
n=5
*****
****
***
**
*
"""


def star(n):
    # 1.找临界值
    if n == 1:
        print('*')
        return  # 临界值的地方让循环结束(函数结束)

    """
    star(3):
    ***
    **
    *
    star(2):
    **
    *
    star(n) = 先打印n颗星 + star(n-1)
    """
    print('*'*n)
    star(n-1)


star(4)


"""
4.在实际开发中，递归是能不用就不要用
递归需要不断调用函数，开辟空间，消耗内存。
"""
















