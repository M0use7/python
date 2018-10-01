'''
1.结构：
while 条件语句:
	循环体

2.说明:
while:关键字
条件语句：结果是True或者False
循环体:要重复执行的代码

3.执行过程：
判断条件语句的结果是否为True,如果为True就执行循环体
执行完循环体在判断条件语句是否为True,如果为True就执行循环体
直到条件语句的结果为false为止

'''
count = 1
sum = 0
while count <= 5:
	
	sum += count
	count += 1
print(sum,count)

# 练习，问：循环结束后，x和sum1的值分别是多少

x = 1
sum1 = 0
while x <= 5:
	x += 1
	sum1 += x
	
print(x,sum1)



# for循环和while循环的比较：
# for循环循环次数是有限的，并且固定(确定)；while循环次数不确定
# for循环：1.遍历序列中的值  2.循环次数确定
# while:1.死循环  2.循环次数不确定

# 练习：找大于10000的数中，第一个能被23整除
x = 10001
while  x % 23 != 0:
	x += 1
print(x)

