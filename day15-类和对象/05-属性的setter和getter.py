"""__author__ = 唐宏进 """

"""
1.保护类型的属性：
a.就是在声明对象属性的时候在属性名前加一个下划线来代表这个属性是受保护的属性。
那么以后访问这个属性的时候就不要直接访问，要通过getter来获取这个属性的值，setter来给这个属性赋值
b.如果一个属性已经声明成保护性的属性，那么我们就需要给这个属性添加getter，也可以添加setter

2.添加getter
添加getter其实就是声明一个没有参数有一个返回值的函数
a.格式：
@property
def 去掉下划线的属性名(self):
    函数体
    将属性相关的值返回
b.使用场景 
场景一：如果想要获取对象的某个属性的值之前，想要再干点别的事情，就可以给这个属性添加getter
场景二：想要拿到某个属性被使用的时刻

3.添加setter
添加setter就是声明一个有一个参数但是没有返回值的函数。作用是给属性赋值
a.格式
b.使用场景
在给属性赋值前想要在干点别的事情，就给属性添加setter
"""
class Car:
    def __init__(self):
        self.color = '黄色'
        self.type = '自行车'
        # _price属性是保护类型
        self._price = 2000

    # _price属性添加getter
    @property
    def price(self):
        print('在使用_price属性')
        return self._price/1000

    # 想要给一个属性添加setter，必须先给这个属性添加getter
    @price.setter
    def price(self,price):
        if isinstance(price,int) or isinstance(price,float):
            self._price = price
        else:
            self._price = 0

# 练习：声明一个员工类，其中有一个属性是是否已婚（bool），获取值之前根据存的值返回'已婚'/'未婚'
class Employee:
    def __init__(self):
        self.name = '小红'
        self.age = 22
        self.tel = 123456
        self._marriage = False

    @property
    def marriage(self):
        if self._marriage == True:
            return '已婚'
        elif self._marriage == False:
            return '未婚'
        else:
            return '未知'
    @marriage.setter
    def marriage(self,marriage):
        if isinstance(marriage, bool):
            self._marriage = marriage
        else:
            self._marriage = 'None'

if __name__ == '__main__':
    car1 = Car()
    print(car1.color, car1._price)

    # 添加完getter后就通过getter去获取属性的值
    # price就是属性_price的getter
    print(car1.price,'k') # 实质就是在调用getter对应的方法

    # 通过setter给_price属性赋值，实质就是调用setter对应的方法
    car1.price = 1000
    print(car1.price)

    car1.price = 'abc'
    print(car1.price)

    employee = Employee()
    print(employee.name,employee.age, employee.tel, employee.marriage)

    employee.marriage = True
    # employee.marriage = 123
    print(employee.marriage)
