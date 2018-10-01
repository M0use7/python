"""__author__ = 唐宏进 """

"""
匿名函数本质还是函数，之前函数的所有内容都使用于它

1.匿名函数的声明
函数名 = lambda 参数列表：返回值

2.说明：
函数名：变量名
lamda：声明匿名函数的关键字
参数列表：参数1,参数2...
冒号：固定写法
返回值：表达式，表达式的值就是返回值

3.调用
匿名函数的调用和普通函数一样
函数名（实参列表）
"""
# 写一个匿名函数，计算两个数的和
my_sum = lambda a,b:a+b
print(my_sum(4,21))

# 练习1：写一个匿名函数，获取指定列表指定下标的值的1/2
# 匿名函数的参数可以设置默认值
fun1 = lambda list1, index=0: list1[index]/2

# 位置参数
print(fun1([1,2,3,4,5,6],4))
print(fun1([1,2,3,4,5,6]))
# 关键字参数
print(fun1(index=1,list1=[1,2,3,4,5,6]))

# 练习2：获取一个列表的所有元素的和，以及他们的平均值
fun2 = lambda list1:(sum(list1),sum(list1)/len(list1))

# print(fun2([1,2,3,4,5,6]))
sum1,average = fun2([1,2,3,4,5,6])
print(sum1,average) # (21,3.5)
#补充：python中的函数是可以有多个返回值的，就是在一个return后返回多个值，多个值之间用逗号隔开
def fun3(list1):
    return sum(list1), sum(list1)/len(list1) # 最终是将多个返回值放到一个元祖中返回的
print(fun2([1,2,3,4,5,6])) # (21,3.5)


