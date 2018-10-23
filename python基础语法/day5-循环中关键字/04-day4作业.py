# 1.读程序
numbers = 1
for i in range(0,20):
	numbers *= 2
print(numbers)

"""
numbers = 1
i = 0 ~ 19
i = 0  numbers = 1*2
i = 1  numbers = 2*2
i = 2  numbers = 2*2*2
...
i = 19 numbers = 2*2*2...*2 = 2**20
计算2的20次方
"""

summation=0
num=1
while num<=100:
	if (num%3==0 or num%7==0) and num%21!=0:
		summation += 1
	num+=1
print(summation)

"""
sum = 0
num = 1

num = 1 ~ 100

统计1-100中，能够被3或者7整除，但是不能同时被3和7整除的数的个数
"""

# 2.求1到100之间所有数的和、平均值
sum1 = 0
for x in range(1,101):
	sum1 += x
print('1-100的和:%d, 平均值:%.2f' % (sum1, sum1/100))


sum1 = 0
x = 100
while x >= 1:
	sum1 += x
	x -= 1
print('1-100的和:%d, 平均值:%.2f' % (sum1, sum1/100))


# 3.计算1-100之间能3整除的数的和
sum1 = 0
for x in range(3,101,3):
	sum1 += x
print(sum1)

sum1 = 0
for x in range(1,101):
	if x % 3:
		continue
	sum1 += x
print(sum1)


sum1 = 0
x = 1
while x <= 100:
	if x % 3 == 0:
		sum1 += x
	x += 1
print(sum1)


#4. 给一个正整数，要求：1、求它是几位数 2.逆序打印出各位数字
import random
number = random.randint(100, 1000000)
print('数字:',number)

# a.
# 将数字转换成字符串
num_str = str(number)
# 获取字符串的长度就是数字的位数
print('数字%d是%d位数' % (number, len(num_str)))  

# b.
print(num_str[-1::-1])

# for循环
length = len(num_str)
for index in range(0, length):
	print(num_str[length-1 - index])

"""
       '1234'
下标    0123
长度 4
index:0~3; 4-1-index

"""
print(number)
index = -1
while index >= -length:
	print(num_str[index],end=',')
	index -= 1

	








