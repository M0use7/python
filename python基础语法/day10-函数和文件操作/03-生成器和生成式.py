"""__author__ = 余婷"""

"""
可以把迭代器看成一种容器，类似列表。生成器就是来生成迭代器。


"""


if __name__ == '__main__':
    # 1.生成式 ---- 产生一个迭代器的表达式
    # a是生成器，能够生成0-9中的所有的数字
    a = (x for x in range(10))
    print(a, type(a))

    a0 = (x*2 for x in range(10))

    a1 = (char for char in 'hello world')

    a2 = (char for char in 'h0el761lo p2yt3ho4n902' if '0'<=char<='9')

    #2.生成器和迭代器都是通过next来获取里面的数据
    print(next(a))
    print(next(a))
    print(next(a))
    print(next(a))

    print('=======')
    for x in a:
        print(x)

    # 3.将生成器转换成列表
    # 通过将生成式产生的迭代器转换成了一个列表
    list1 = [x for x in range(10)]
    print(list1)

    # 4.将生成器转换成字典
    # 注意：容器类型的元素是元祖，并且元素中有且只有两个元素的，才能转换成字典
    dict1 = dict((x, x*2) for x in range(5))  # {0: 0, 1: 2, 2: 4, 3: 6, 4: 8}
    print(dict1)

    # 练习:一句代码实现交换一个字典中的key和value的值. {'a':1, 'b':2} --> {1:'a', 2:'b'}
    dict2 = dict((value, key) for key,value in {'a': 1, 'b': 2, 'c': 3}.items())

    old = {'a': 1, 'b': 2, 'c': 3}
    dict3 = dict((old[key], key) for key in old)
    print(dict3)








