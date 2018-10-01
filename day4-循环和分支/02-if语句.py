# python中的分支结构只有一种：if分支结构
'''
1.if

if 条件语句:
	执行语句块

说明：
a.if:python中的关键字，'如果'的意思,用来做判断
b.条件语句：最终的结果会被转换成布尔值
c.冒号：冒号是固定写法，必须写！
d.执行语句块：这儿可以是多行语句，但是每行语句必须和前面的if保持一个缩进

执行过程：先判断条件语句的结果是否为True,如果为True就执行冒号后面的执行语句，
		  否则执行if模块后的其他语句
'''
age = 20 
if age >= 123:
	print('成年')
	print('ads ')

# 练习：用一个变量保存一个学生的成绩，要求当学生成绩大于90的时候,打印优秀
# 不管成绩是多少，都把成绩打印出来
score = 92
if score>90:
	print('优秀')
print(score)

'''
2.if-else
语法：
if 条件语句:
	执行语句块1
else:
	执行语句块2

说明：
else:关键字(else后边的冒号不能省)

执行过程：先判断条件语句的结果是否为True，如果为True就执行语句块1
		  执行语句块1后再执行其他语句;如果为False就执行语句块2
		  执行语句块2后再执行其他语句
'''
# 要求年龄大于等于十八就打印成年，否则打印未成年
age = 17
if age > 18:
	print('成年')
else:
	print('未成年')


'''
3.if-elif-else

'''
# 要求成绩大于90打印优秀，80-90打印良好，60-79打印及格，小于60打印不及格

# 语法：
# if 条件语句1:
# 	语句块1
# elif 条件语句2:
# 	语句块2
# ...
# else:
# 	语句n

grade = 90

if grade > 90:
	print('优秀')

elif grade >= 80:
	print('良好')

elif grade >= 60:
	print('及格')

else:
	print('不及格')



'''
4.if语句的嵌套
没个if中都可以嵌套其他的if语句

if 条件1:
	执行语句1
	if 条件2:
		执行语句2
	else:
		执行语句4
else:
	执行语句4
'''

# 成绩和年龄：如果成绩大于90并且年龄18以上就获取100万
#			  年龄小于18就获取200万。成绩小于90就没有奖金

score = 90   
age = 18
if score >= 90:
	if age >= 18:
		print('100万')
	else:
		print('200万')
else:
	print('没有奖金')

# 练习：产生一个随机数(0-100)，判断随机数是否是偶数，如果是打印偶数，否则打印奇数
#		如果能够被4整除，再打印能被4整除
import random
num = random.randint(0-100)
if num%2==0:
	print('偶数')
	if num%4==0:
		print('能被4整除')
else:
	print('奇数')

# import是python中导入模块或者模块中内容的关键字
# random是python内置的产生随机数的模块
import random
number = random.randint(10,20) # 产生10到20之间的随机数，并且存到number中
print(number)



