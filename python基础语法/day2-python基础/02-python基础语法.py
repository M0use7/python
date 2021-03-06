# 1.注释
# 注释是不会参与代码的编译和执行的。只是对代码进行解释和说明的文字。（要常写注释）

# 单行注释就是在注释文字前加#
"""
这是多行注释1
这是多行注释2
这是多行注释3
"""
'''
这是多行注释1
这是多行注释2
这是多行注释3
'''
# 这是多行注释1
# 这是多行注释2
# 这是多行注释3

# 2.标识符（专门用来命名的-变量、函数、类）
# 1）要求
# a.是由字母数字下划线组成（只能少不能多）
# b.数字不能开头的
# c.大小写敏感的(大写和小写不一样，例如：abc和Abc、ABC不一样)
# d.python3以后，标识中可以包含非ASCII码(可以包含中文),但是在实际开发中不建议使用

# A.B.C  A-大版本，重大修改

na = 90
a1 = 1
a1_ = 2
姓名 = 100
# a'sh = 100
# h%9 = 20
# 1abc = 100
_hsj = 100

# 3. 关键字(保留字)
# python中保留用来作为特殊语法和拥有特殊功能的一些单词
'''
'False', 'None', 'True', 'and',
'as', 'assert', 'break', 'class', 'continue',
'def', 'del', 'elif', 'else', 'except', 'finally', 
'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 
'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while',
 'with', 'yield'
'''
import keyword
print(keyword.kwlist)  

# 4.行与缩进
# 缩进的要求：
'''
a.同一级的代码必须保持同一缩进。(统一使用tab来产生缩进)
b.通过缩进来产生代码块（类似于其他语言中的{}）
'''
# 行的规范
'''
a.声明函数的前后必须有两个换行
b.声明类的前后也需要两个换行
c.多个功能模块间用换行隔开
'''


a = 10
b = 20

if a > 10:
	print('abc')
	print('123')

# 5. 多行显示（一句代码多行显示）
# a.在需要换行的地方加\,然后在后面换行。换行后缩进不受限制

a = 100000+ 10000000 / 900000 * 2999 - 83883\
	- 82939339+ 29393 +2387387 - \
	273838 - 2388 + 2788
print(a)

[
	120, 
	23,
	'asdf', 
	278, 
	'bhkj',
	 889
 ]

# 6.字面量（具体的值）
# a.数字字面量: 10, 12.5, -20, +10.0, 2e2, 10j
# b.布尔值：True(-- 真), False (-- 假)
# c.字符串：'76sh&*^', "hello",  "123"
# d.列表：[10, 20, 'python', 'hello', True]
# e.字典：{'a':10, 'name':'余婷'}

# 7.python中的基本数据类型
# a.数字相关的
# int(整型)，float(浮点型)，complex(复数)
# b.bool(布尔)
# 只有True和False两个值
# c.str(字符串)
# d.list(列表)
# e.dict(字典)
# f.tuple(元祖)
# g.set(集合)
# h.function(函数)
# i.bytes(字节)



















