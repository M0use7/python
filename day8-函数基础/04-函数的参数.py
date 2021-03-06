"""__author__ = 唐宏进 """

"""
参数：声明函数的时候的参数列表中的参数叫形参；调用函数的时候，参数列表中的参数加实参
传参：传参的过程就是使用实参给形参赋值的过程。一定要保证每个形参都要有值

# 实参
1.位置参数：传参的时候实参的位置和形参一一对应（第一个实参传给第一个形参，第二个实参传给第二个形参...）
2.关键字参数：函数调用的时候通过'形参名=实参'的形式来传参
"""

# 位置参数
def fun1(a,b,c):
    print(a,b,c)

# a = 10, b = 'abc', c = True
fun1(10, 'abc', True)

# 2.关键字参数
fun1(b='abc',  c=True, a=10)

"""
3.参数的默认值
a.在声明函数的时候，可以给参数赋默认值的。（可以给所有的参数赋默认值，也可以给部分参数赋默认值）
！给部分参数赋默认值的时候，要求有默认值的参数必须放到参数列表的最后

b.调用参数有默认值函数的时候，有默认值得参数可以传参也可以不传参
"""

# 3.1 声明函数的时候每个参数都有默认值
def fun2(a=0, b='a', c=True):
    print(a,b,c)

# a.所有的参数都不传参，全部使用默认值
fun2()

# b.给部分参数传参
fun2(10)

fun2(b='abc')

# 3.2 参数列表中，部分参数有默认值（有默认值的必须放到后面）
def fun3(a, b, c=20):
    print(a, b, c)

# 没有默认值的参数必须传参，有默认值的参数可以传也可以不传
fun3(100,200)
fun3(b=300, a=200)

"""
4.不定个数参数
python中通过在形参名前加*，让这个形参变成一个元祖，来让这个形参可以同时接受多个实参。
"""
# 写一个函数，计算多个数的和
def sum2(*nums):
    # print(nums,type(nums))
    sum = 0
    for item in nums:
        sum += item
    print(sum)
sum2()
sum2(1)
sum2(20,30,1)


# 写一个函数，统计指定班级中所有学生的成绩
def class_info(class_name,*scores):
    print(class_name,scores)

class_info('python180', 90, 89, 78, 76, 67, 88)

def class_info2(class_name,location,*scores):
    print(class_name,location,scores)

class_info2('python180', '地址',90, 89, 78, 76, 67, 88)


"""
5.对参数的类型进行说明
python不能直接约束一个变量的类型，但是可以通过说明，来提示用户调用函数的时候，参数的类型
"""
def func4(name:str,age:int, stuy_id:str):
    print(name,age)
    print(stuy_id.ljust())
# func4('abc', 10, [90,89,78])

