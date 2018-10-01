
#补充：python控制台输入函数 input(提示信息)
'''
1.程序遇到input会停下来，等待输入完成后才会执行后面的代码(阻塞线程)
2.输入结束：遇到return就结束
3.获取到输入的内容的类型是字符串(不管输入什么)
'''
# name = input('请输入名字:')
# number = input('请输入一个数字:')
# print(number,type(number))
# print('==========')

# break、continue、else
'''
break:程序执行过程中，只要遇到break，就结束/跳出包含break的最近的循环
'''
# 练习：随机生成一个整数，然后去猜，猜中为止
# import random
# number = random.randint(0,100)
# count = 0

# while True:
# 	num = input('请输入一个数字(0-100):')
# 	count += 1
# 	if int(num) == number:
# 		print('恭喜你猜对了')
# 		if count > 7:
# 			print('机智')
# 		else:
# 			print('你真厉害')
# 		break
# 	else:
# 		if int(num) > number:
# 			print('大了,继续猜')
# 		else:
# 			print('小了,继续猜')
		

# 计算1000以内，不能被15整除所有数的和
# sum = 0
# for x in range(1000):
# 	if x % 15 == 0:
# 		continue
# 	sum += x
# print(sum)


# else:python中的循环的最后可以添加else语句，代表循环结束后要执行的代码
'''
for 变量 in 序列：
	循环体
else:
	循环结束后要执行的代码

while 条件语句：
	循环体
else:
	循环结束后要执行的代码

注意：写到else里面的语句，和写到外面的区别是。beak的时候，else中的内容不会执行。
'''

for x in range(5):
	if x == 2:
		break
	print(x)
else:
	print('for结束1')

for x in range(5):
	if x == 2:
		break
	print(x)
print('for结束2')


