import random  


# 补充:python控制台输入函数 input(提示信息)
"""
1.程序遇到input,会停下来，等待输入完成后才会执行后面的代码(阻塞线程)
2.输入结束：遇到return就结束
3.获取到输入的内容的类型是字符串(不管输入的是什么)
"""
# name = input('请输入名字:')  
# number = input('请输入一个数字:')

# print(name, number, type(number))
# print('==========')

# break、continue、else
"""
break: 程序执行过程中，只要遇到break,就结束/跳出包含break的最近的一个循环
"""
# 练习：随机生成一个整数，然后去猜，猜中为止

# number = random.randint(0, 100)
# count = 0  # 统计猜的次数

# while True:
# 	num = input('请输入一个数字(0-100):')
# 	count += 1

# 	if int(num) == number:
# 		print('猜对了')

# 		if count >= 7:
# 			print('智商已欠费!')

# 		break
# 	else:
# 		print('猜错了')
# 		if int(num) > number:
# 			print('再小点儿')
# 		else:
# 			print('再大点儿')




# while True:
# 	num = input('请输入一个数字(0-100):')
# 	# 每输入一次数字，就说明猜了一次
# 	count += 1

# 	if int(num) == number:
# 		print('恭喜你，猜对了! %d' % (number))
# 		# 根据总共才的次数，评定智商
# 		if count > 7:
# 			print('智商欠费，请充值')
# 		elif count > 3:
# 			print('机智')
# 		else:
# 			print('大神！！')
			
# 		break  # 猜对了，就不用再重复的猜了。就让循环结束
# 	else:
# 		if int(num) > number:
# 			print('大了，再小点儿')
# 		else:
# 			print('小了, 再大点儿')


# 计算1000以内，不能被15整除的数的和
sum1 = 0
for x in range(1000):
	if x % 15 == 0:
		continue

	sum1 += x
	print(x)  


# else: python中的循环的最后可以添加else语句，代表循环结束后要执行的代码
"""
for 变量 in 序列:
	循环体
else:
	循环结束后要执行的代码


while 条件语句:
	循环体
else:
	循环结束后要执行的代码

注意:写到else里面的语句，和写在循环外边的区别是。break的时候，else中的内容不会执行
"""
for x in range(5):
	print(x)
	if x == 2:
		break
else:
	print('for结束1')


for x in range(5):
	print(x)
	if x == 2:
		break
print('for结束2')


n = 1
while n < 5:
	print(n)
	n += 1
else:
	print('while结束')










