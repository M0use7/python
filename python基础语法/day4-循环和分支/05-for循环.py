# 1+2+3+4+5+....+100
# 在完成某个功能的时候，如果需要重复某个操作，就可以使用循环。
# python中循环结构有两种：for循环和while循环

"""
1.for循环的结构:
for 变量名 in 序列:
	循环体

说明：
a.for: 关键字
b.变量名: 和声明变量时的变量名的要求一样
c.in: 关键字
d.序列: 容器(数据本身是由多个数据组成)，
	   例如：字符串、列表、字典、元祖、集合、range、生成式和生成器（迭代器）
e.循环体：需要重复执行的代码

执行过程：
	让变量去序列中取数据，一个一个的取，取完为止。每取一个数据，执行一次循环体
"""

"""
x = a
a
x = b
b
x = c
c
x = 1
1
x = 2
2
x = 3
3
"""
for x in 'abc123':
	print(x) 


# range函数是python中内置函数，作用是产生指定范围中的数字
# xrange是python2中的函数，python3中用range来代替了
"""
range(N): 产生0 ~ N-1的所有整数
range(N,M): 产生 N ~ M-1的所有整数
range(N,M,step): 产生从 N开始，每step产生一个整数,到M之前
"""
print('===============')
for x in range(10):
	print(x)

print('------------')
for num in range(10,21):
	print(num)

for x in range(1,11,2):
	print(x)


# 练习:计算1+2+3+...+100
# a.先取出1，2，3，... 100

"""
sum1 = 0
x = 1,2,3,4,5
第一次:  x = 1  sum1 += 1  sum1 = sum1 + 1 = 0+1
第二次： x = 2  sum1 += 2  sum1 = sum1 + 2 = 0+1+2
第三次:  x = 3  sum1 += 3  sum1 = sum1 + 3 = 0+1+2+3
第四次:  x = 4  sum1 += 4  sum1 = sum1 + 4 = 0+1+2+3+4
第五次:  x = 5  sum1 += 5  sum1 = sum1 + 5 = 0+1+2+3+4+5
"""
sum1 = 0
for x in range(1, 101):
	sum1 += x

print(sum1)


# 统计1~1000中能够被3整除的数的个数
count = 0
for x in range(1, 1001):
	if x % 3 == 0:
		print('%d可以被3整除' % (x))
		count += 1

print('1-1000中能被3整除的个数:%d' % (count))


# 注意: for循环中用来获取序列值的变量，在循环体不是一定要使用。
#       如果不用，那么变量名可以声明为_
# 打印50行'****'
for _ in range(50):
	print('****')





