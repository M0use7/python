"""__author__ = 唐宏进 """


if __name__ == '__main__':
    def fun1():
        for x in range(10):
            return x
    # 0 < class 'int'> < class 'function' >
    print(fun1(),type(fun1()),type(fun1))

    # 1.yield关键字
    """
    只要函数中有yield关键字，那么这个函数就会变成一个生成器。
    
    a.有yield的函数，在调用函数的时候不再是获取返回值，
    而是产生一个生成器对象，生成器对象中保留的是函数体
    b.当通过next获取生成器中的数据的时候，才会去执行函数体，执行到yield为止，
    并且将yield后面的结果作为生成器的数据返回，同时记录结束的位置，下次再调用next的时候，
    从上次结束的位置接着往后执行
    """
    def fun2():
        print('abc')
        for x in range(10):
            yield x
            print('aaa')

    # 注意：函数中只要有yield，不管yield会不会执行到，函数的调用结果都是生成器
    def fun3(x):
        print('abc')
        if x > 10:
            yield 100
        return 20
    # print(fun2(), type(fun2()), type(fun2))
    # 这儿的fun2()是一个生成器
    gen = fun2()
    print(next(gen))
    print(next(gen))
    print(next(gen))

    gen2 = fun3(1)
    print(gen2)

    # 练习：写一个生成器，可以产生斐波那契数列
    def fibo():
        a = 0
        b = 1
        while True:
            yield b
            a,b = b,a+b

    gen3 = fibo()
    for _ in range(10):
        print(next(gen3))

    # 生成器和生成式产生的对象就是迭代器
    # 将列表转换成迭代器对象
    iter1 = iter([1,2,3,4])
    print(iter1)
    print(next(iter1))
    print(next(iter1))
    for item in iter1:
        print(item)