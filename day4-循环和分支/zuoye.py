# 基础
# 总结程序功能：
# 1.计算2的20次方，并打印出这个数

# 2.找出1~100间能被3或者7整除但不能被2整除的数，并打印这样数的个数

# 编程：
# 1.
# sum = 0
# for x in range(1,101):
# 	sum += x
# average = sum / 100
# print(sum,average)

# count = 1
# sum = 0
# while count <= 100:
# 	sum += count
# average = sum / 100
# print(sum,average)

# 2.
# sum = 0
# for x in range(1,101):
# 	if not x % 3:
# 		sum += x
# print(sum)

# count = 1
# sum = 0
# while count <= 100:
# 	if not count % 3:
# 		sum += count
# 	count += 1
# print(sum)		

# 3.
# sum = 0
# for x in range(1,101):
# 	if x % 7:
# 		sum += x
# print(sum)

# count = 1
# sum = 0
# while count <= 100:
# 	if count % 7:
# 		sum += count
# 	count += 1
# print(sum)


# 稍微困难
# 1.
# n = 9
# if n == 1 or n == 2:
# 	current = 1
# p1= 1
# p2 =1
# for index in range(3,n+1):
# 	current = p1 + p2
# 	p1 = p2
# 	p2 = current
# print(current)


# a = 0;b = 1
# n = 1
# for x in range(n-1):
# 	a,b = b,a+b
# print('第%d个斐波那契数是%d'%(n,b))

# 2.
# import math
# count = 0
# for n in range(101,201):
# 	for i in range(2,int(math.sqrt(n))+1):
# 		if n % i == 0:
# 			break
# 	else:
# 		count += 1
# 		print(n,end = ' ')
# print('101-200之间有%d个素数'%(count))	

# 3.
# for x in range(100,1000):
# 	bai = x//100
# 	shi = x//10%10
# 	ge = x%10
# 	if x == (bai**3 + shi**3 + ge**3):
# 		print(x)

# 4.
# fz = 2
# fm = 1
# for x in range(1,20):
# 	fz,fm = fz+fm,fz
# print('第20个分数:%d/%d'%(fz,fm))

# 5.
# num = 123
# str = str(num)
# length = len(str)
# print('它是一个%d位数'%(length))
# print(str[::-1])

# for x in range(0,length):
# 	print(str[length-1-x])

