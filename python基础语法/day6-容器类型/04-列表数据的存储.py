"""__author__ = 余婷"""

# python中，变量在存数据的值的时候，会根据数据类型的不同，使用两种方式来存值
"""
值类型：变量存数据直接存值，例如：整型、浮点型、布尔、字符串
引用类型：变量存数据的时候，存的是数据在内存中的地址。例如：列表、字典、元祖、集合、函数、自定义的类的对象等！
"""
a = 10
b = a
print(a, b)
a = 100
print(a, b)

a1 = [1, 2]
# 引用类型赋值的时候赋的是地址
b1 = a1

# 先将列表a1中的元素拷贝一份存到一个新的地址中，然后把新的地址赋给c1
c1 = a1[:]
print(a1, b1)

a1.append(100)
print(a1, b1,c1)

