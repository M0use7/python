# 判断一个数是否是偶数的两种写法
number = 10

#初学者
if number % 2 == 0:
	print('偶数')

#推荐
if not number % 2:
	print('偶数')

if number % 2:
	print('奇数')
else:
	print('偶数')


# 判断一个字符是否空串
# 初学者
str1 = 'abc'
if str1 == '':
	print('是空串')
else:
	print('不是空串')

if len(str1) == 0:
	print('是空串')
else:
	print('不是空串')	

# 推荐
if str1:
	print('不是空串')
else:
	print('是空串')	


if not str1:
	print('是空串')
else:
	print('不是空串')	
