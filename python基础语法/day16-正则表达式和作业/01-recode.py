"""__author__ = 余婷"""

"""
1.文件操作
a.操作流程: 打开文件（open） --- 操作文件 --- 关闭文件(close)
with open() as 文件变量名:
    文件操作
    
open(文件路径,打开方式,encoding=编码方式)

b.打开方式
r/br/rb : 
w/bw/wb/a : 文件路径不存在会自动创建那个文件

c.编码方式
文本编码，二进制不能去设置！！

d.读(read)、写(write)

e.json文件/json数据
json数据的格式：只有一个数据，并且类型必须是json支持的数据类型
数据类型及其表现：数组、对象(字典)、数字、字符串、布尔、null
            [元素1,元素2...]、{key1:value1,key2:value2...}、190/12.78/-1、"abc"、true/false、null
python对json的支持：
load(文件对象): 获取json文件中的数据，并且转换成相应python数据
loads(json格式的字符串): 将字符串转换成python数据
dump(): 将python数据转换成json数据然后再写到json文件中
dumps()：将python数据转换成json格式的字符串
    
f.数据本地化和持久化
比如将数据number的值转数据本地化
先从本地去取值 --> 对取出来的值进行处理 --> 再将新的值存到本地

2.异常捕获
try:
    需要捕获异常的代码
except:
    异常发生
finally:
    不管异常是否发生，都执行
    
a.except: 捕获所有异常   b.except 类型名: 捕获指定的异常（这个结构可以出现多次）c.except (类型名1, 类型名2...):

抛出异常
raise 异常类型

异常类型：要求必须是Exception的子类


3.类和对象
1概念
类：具有相同功能和属性的对象的集合(抽象的)
对象：类的实例（具体）

2)类的声明
class 类名(父类):
    类的说明文档
    类的内容

3)**创建对象
a.格式：对象 = 类名()
b.通过调用构造方法创建对象的时候，会自动调用__init__方法去对对象进行初始化
c.__init__方法的传参

4)属性
对象属性：
a.init方法中声明，self.属性名 = 值
b.通过对象去使用
c.对象属性的增删(了解)， 获取对象属性的值和修改对象属性值（掌握）---> 对象.属性

类的字段：
a.直接声明在类中的变量
b.通过类去使用 --> 类.字段

私有化、保护类型(getter和setter)等 ----> 能掌握最好

5)方法
对象方法：
a.直接声明在类的方法
b.自带一个self参数（self不需要传参，指向当前对象）
c.对象方法通过对象调用
d.需要使用对象的属性才用对象方法

类方法：
a.@classmethod修饰
b.自带一个cls参数（cls不需要传参，指向当前类）
c.类方法通过类调用
d.需要使用类的字段的时候使用类方法

静态方法：
a.@staticmethod修饰
b.没有自带参数
c.通过类来调用
d.不需要对象属性的时候就可以使用


**本质上，python中的类可以调用类中所有的方法

"""
import json


class Person:
    number = 10
    def __new__(cls, *args, **kwargs):
        print('创建对象')

    def __init__(self, a, b):
        self.name = '张三'
        print('初始化对象', a, b)

    def eat(self):
        print('%s:abc' % self.name)



p1 = Person(10, 20)


if __name__ == '__main__':
    # 10 > 30
    pass