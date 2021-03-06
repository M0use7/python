# python中的分之结构只有一种：if分之结构
"""
1. if

语法：
if 条件语句:
	执行语句块

其他语句

说明：
a. if: python中的关键字，'如果'的意思,用来做判断
b. 条件语句: 最终的结构会被转换成布尔值
c. 冒号: 冒号是固定写法，必须写！
d. 执行语句块：这儿可以是多行语句，但是每行语句必须和前面的if保持一个缩进(一个tab)

执行过程：先判断条件语句的结果是否为True,如果为True就执行冒号后面的执行语句块。
		否则直接执行if模块后的其他语句

"""

age = 10

if age >= 18:
	print('成年')
	print('可以进网吧')  

# 练习：用一个变量保存一个学生的成绩，要求：当学生的成绩大于90的时候，打印优秀。
#      不管成绩是多少，都把成绩打印出来
score = 99

if score > 90:
	print('优秀')

print(score)


"""
2. if-else
语法:
if 条件语句:
	执行语句块1
else:
	执行语句块2

其他语句

说明：
else: 关键字（else后边的冒号不能省）

执行过程：先判断条件语句的结果是否为True,如果为True就执行执行语句块1，
		 执行完语句块1后再执行其他语句；如果为False就执行语句块2，
		 执行完语句块2后再执行其他语句
"""
# 要求年龄大于等于18就打印成年，否则打印未成年
age = 12

if age >= 18:
	print('成年')
else:
	print('未成年')
	print('不能进网吧')  


"""
3.if-elif-(else)

语法:
if 条件语句1:
	语句块1

elif 条件语句2:
	语句块2

elif 条件语句3:
	语句块3

	...
else:
	语句块n

其他语句

"""
# 要求成绩大于90分打印优秀，80-90打印良好，60-79及格，60以下不及格
score = 50

if score > 90:
	print('优秀')

elif score >= 80:
	print('良好')

elif score >= 60:
	print('及格')

else:
	print('不及格')



"""
4.if语句的嵌套
每个if分之中都可以嵌套其他的if语句

if 条件1:
	执行语句1
	if 条件2：
		执行语句2
	else:
		执行语句3
else:
	执行语句4


"""
# 成绩和年龄：如果成绩大于等于90并且年龄是18以上就获取 奖金100万，
#           年龄小于18就获取奖金200万。成绩小于90不管多少岁打印没有奖金
score = 90
age = 18
if score >= 90:
	if age >= 18:
		print('100万')
	else:
		print('200万')
else:
	print('没有奖金')

# 练习: 产生一个随机数(0-100)，判断随机数是否是偶数，如果是打印偶数，否则打印奇数。
#      如果能够被4整数，再打印能被4整除
import random
number = random.randint(0, 100)
print('随机数是:%d' % (number))

if number % 2 == 0:
	print('偶数')
	if number % 4 == 0:
		print('能够被4整除')
else:
	print('奇数')


# 补充：
# import是python中导入模块或者模块中内容的关键字
# random是python内置的产生随机数的模块

number = random.randint(10, 20)  # 产生一个10到20的随机整数，并且存到number中
print(number)



























