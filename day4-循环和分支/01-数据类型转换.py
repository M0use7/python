# int,float,bool,str
# 1.数据类型的自动转换
a = 10 # 整型(int)
b = 12.5 # 浮点型(float)
result = a + b #会自动将整型a,转换成浮点型，然后再计算
print(result)

result2 = a + True # 会自动将布尔Ture,转换成整型1
print(result2,type(result2))

# 2.强制转换
# 基本语法：类型名(需要转换的数据)
# a.将其他数据转换成int类型

# 浮点型、布尔和部分字符串可以转换

print(int(12.55)) # 去掉小数点后面的数
print(int(True),int(False)) # Ture为1,False为0

# 去掉字符串的引号后，字符串的内容本身就是一个整数的时候，才能被转换成整型
print(int('123'))
# print(int('12.3')) 不可以转换

# b.将其他的数据类型转换成float类型
# 整数、布尔和部分字符串可以转换
print(float(100)) # int -> float 在整数后加.0
print(float(True),float(False))

# 去掉引号后，字符串的内容本身就是一个整数或者浮点数的时候，才能被转换成浮点型
print(float('2e3'),float('-12.5'),float('100'))


# c.将其他类型的数据转换成bool
''' 
所有的数据的类型都可以转换成bool

数字中:除了0是False,其他的都是True
字符串中：除了空串其他都是Ture

总结：所有为空、为0的值全部是False,否则是True
'''
print(bool('0.0000'))
print(bool(''))
print(bool([]))
print(bool({}))
print(bool(None))

# d.其他类型转换成字符串
'''
所有的数据都可以转换成字符串。转换的时候就是在数据的外面加引号

'''
print(str(100),str(18.9),str(True),str([1,2,3]))


