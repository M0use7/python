"""__author__ = 余婷"""

"""
参数: 声明函数的时候的参数列表中的参数叫形参；调用函数的时候，参数列表中的参数叫实参
传参: 传参的过程就是使用实参给形参赋值的过程。一定保证每个形参都要有值

# 实参
1.位置参数: 传参的时候实参的位置和形参一一对应（第一个实参传给第一个形参，第二个实参传给第二个形参....）
2.关键字参数: 函数调用的时候通过'形参名=实参'的形式来传参
"""


# 1.位置参数
def func1(a,b,c):
    print(a, b, c)


# a = 10, b='abc',  c=True
func1(10, 'abc', True)

# a='abc' b=10, c=False
func1('abc', 10, False)

# 2.关键字参数
func1(b='abc', c=True, a=10)


"""
3.参数的默认值
a.在声明函数的时候，可以参数赋默认值的。（可以给所有的参数赋默认值，也可以给部分参数赋默认值）
！给部分参数赋默认值的时候，要求有默认值的参数必须放到参数列表的最后

b.调用参数有默认值的函数的时候，有默认值的参数可以传参也可以不传
"""


# 3.1声明函数的时候每个参数都有默认值
def func2(a=100, b='a', c=True):
    print(a, b, c)


# a.所有的参数都不传参，全部使用默认值
func2()

# b.给部分参数传参
func2(10)
"""
a=100;b='a';c=True
a=10
"""
func2(b='abc')


# 3.2 参数列表中，部分参数有默认值(有默认的必须放到后面)
def func3(a, b, c=20):
    print(a, b, c)


# 没有默认值的参数必须传参，有默认值的参数可以传也可以不传
func3(100, 200)
func3(b=300, a=200)
# func3(b=100)  # TypeError， a没有值


"""
4. 不定个数参数
python中通过在形参名前加*，让这个形参变成一个元祖,来让这个形参可以同时接受多个实参。多个包含0个
"""


# 写一个函数，计算多个数的和
def sum2(*nums):
    # print(nums, type(nums))
    sum1 = 0
    for item in nums:
        sum1 += item

    print(sum1)


sum2()
sum2(1)
sum2(20, 3, 40)
sum2(100, 300, 400, 9, 823, 90, 98, 89, 9, 9)


# 写一个函数，统计指定班级中所有学生的成绩
def class_info(class_name, *scores):
    print(class_name, scores)


class_info('python1806', 90, 89, 78, 76, 67, 88)


def class_info2(class_name, location, *scores):
    print(class_name, location, scores)


class_info2('班级名', '地址', 90, 89, 67, 89, 56)


"""
5.对参数的类型进行说明
python不能直接约束一个变量的类型。但是可以通过说明，来提示用户调用函数的时候，参数的类型
"""


def func4(name: str, age: int, study_id: str):
    print(name, age)
    # print(study_id.ljust())


# func4('abc', '10', '001')







