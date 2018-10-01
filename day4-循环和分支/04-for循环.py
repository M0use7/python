# 1+2+3+4+5+...+100
# 在完成某个功能的时候，如果需要重复某个操作，就可以使用循环。
# python中循环结构有两种：for循环和while循环

'''
1.for循环的结构:
for 变量名 in 序列:
	循环体

说明:
a.for:关键字
b.变量名:和声明变量时的要求一样
c.in:关键字
d.序列:容器(数据本身是由多个数据组成)
	   例如:字符串、列表、字典、元祖、集合、range、生成式和生成器
e.循环体：需要重复执行的代码	   

执行过程：
	让变量去序列中去数据，取完为止。每取一个数据，执行一次循环体
'''

for x in 'abc123':
	print(x)


# range函数是python中的内置函数，作用是产生指定范围中的数字
# xrange是python2中的函数,python3不能用
'''
range(N):产生0~N-1的所有整数
range(N,M):产生N~M-1的所有整数
range(N,M,step):产生从N开始,每step产生一个整数,到M之前
'''
print('==============')
for x in range(10):
	print(x)

print('==============')
for x in range(10,21):
	print(x)	

for x in range(1,11,2):
	print(x)

# 计算1+2+3+...+100
sum = 0
for x in range(1,101):
	sum += x
print(sum)

# 统计1~1000中能够被3整除的个数
count = 0
for x in range(1,1001):
	if  not x % 3:
		count += 1
print(count)


# 注意：for循环中的用来获取序列值的变量，在循环体中不一定要使用
#   	如果不用，那么变量名可以声明为_
# 打印50行***
for _ in (0,50):
	print('***')

