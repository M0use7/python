"""__author__ = 余婷"""

"""
1.函数的调用过程是一个压栈的过程：
每次调用一个函数，系统就会在内存区域中的栈区间去开辟空间，保存函数调用过程中产生的数据。
当函数调用完成后，对应的栈区间会自动销毁

函数调用时产生的栈区间中保存的数据有：形参、在函数中声明的变量
"""
def func1(a, b):
    c = 100
    print(a, b, c)

func1(20, 30)
func1(100, 200)

"""
2.什么是作用域:
指的就是一个变量能够使用的范围

3.全局变量和局部变量
a.
全局变量:就是声明在函数和类的外面的变量都是全局变量。
全局变量的作用域: 从声明开始到文件结束(从声明开始到文件结束，任何地方都可以使用)
"""
a = 100   # 全局变量

if a > 10:
    b = 20  # 全局变量

# x也是全局变量
for x in range(10):
    print(x)
    for y in range(10):
        print(y)


print(a, b)
print(x, y)

def func2():
    print(x, a, b, y)

func2()

"""
b.
局部变量:声明在函数中或者类中的变量就是局部变量
局部变量的作用域: 从声明开始到函数结束或者是从声明开始到类结束
注意: 函数的参数是声明在函数中的局部变量
"""
# x, y, z都是局部变量
def func3(x1, y1):
    z = 'abc'
    print(x1, y1, z)

# def func4():
#     print(x1, y1, z)  # 不能再别的函数中使用

func3('a', 'b')


# 局部变量只能在声明变量的那个函数中使用，不能在函数外面使用
# print(x1)
# print(y1)
# print(z)


"""
c.
global关键字：是在函数中声明一个全局变量

global 变量名
变量名 = 值

"""
# 全局变量
num1 = 100
# 全局变量
num2 = 10

def func4():
    # 局部变量
    num1 = 200
    print(num1)  # 如果全局变量和局部变量同名，那局部变量的作用域内使用的是局部变量的值

    # 想要在局部区域内修改全局变量的值
    global num2  # 说明从这句开始后面的num2都是全局变量
    num2 = 199
    print(num2)

    global num3  # 直接在函数中声明一个全局变量。这个变量在外面只有函数调用后才能使用
    num3 = 'aaa'

func4()
print(num1)
print(num2)
print(num3)

"""
nonlocal 不声明局部变量
"""
def func5():
    # 局部变量
    nn = 10
    # 函数中可以声明函数
    def func6():
        nonlocal nn  # 在局部的局部中修改局部变量的值
        nn = 20
        print('func6',nn)

    func6()

    print('func5', nn)


func5()
# print(nn)


# 1.
def func():
    a = []
    for i in range(5):
        a.append(lambda x: x*i)
    return a


aa = func()
print(aa[0](2), aa[2](2), aa[3](2))






