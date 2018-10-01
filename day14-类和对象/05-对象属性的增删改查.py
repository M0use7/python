"""__author__ = 唐宏进 """
"""
python是动态语言，python中类的对象的属性可以进行增删的操作
"""
class Person:
    """人类"""
    def __init__(self):
        self.name = '张三'
        self.age = 18
        self.height = 160


if __name__ == '__main__':
    p1 = Person()
    p2 = Person()
    # 1.查（获取属性的值）
    """
    方法一：对象.属性名
    方法二：def getattr(对象, 属性名,default=None)
    方法三：对象.__getattribute__(属性名)
    """
    print(p1.name)
    # print(p1.name2) # 属性不存在会报错
    print(getattr(p1, 'age'))
    print(getattr(p1, 'age2',0)) # 属性不存在可以通过设置默认值，让程序不崩溃，并且返回默认值
    print(p1.__getattribute__('height'))

    # 2.改（修改属性的值 -- 属性存在）
    """
    方法一：对象.属性 = 新值
    方法二：def setattr(对象, 属性名, 新值)
    方法三：对象.__setattr__(属性名,新值)
    """
    p1.name = '李四'
    setattr(p1,'age', 20)
    print(p1.age)

    p1.__setattr__('height',170)
    print(p1.height)

    # 3.增（添加属性 -- 属性不存在）
    # 注意：添加属性只能给某一个对象添加属性
    """
       方法一：对象.属性 = 新值
       方法二：def setattr(对象, 属性名, 新值)
       方法三：对象.__setattr__(属性名,新值)
    """
    p1.sex = '男'
    print(p1.sex)

    setattr(p1,'weight',45)
    print(p1.weight)

    p1.__setattr__('color','绿色')
    print(p1.color)

    # print(p2.sex) # 添加属性只影响一个对象

    # 4.删（删除对象属性）
    # 注意：删除值针对指定的对象
    """
    方法一：del 对象.属性
    方法二：delattr(对象，属性名)
    方法三：对象.__delattr__(属性名)
    """
    del p1.name
    # print(p1.name)

    delattr(p1, 'age')
    # print(p1.age)

    p1.__delattr__('height')
    print(p1.height)

