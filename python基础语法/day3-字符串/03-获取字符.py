# 字符串实质可以是一个不可变的序列，序列内容是字符。
# 一旦字符串确定，那么里面的字符和字符的位置就不可变了，例如:'abc'
# 1.怎么获取单个字符
'''
python中的字符串，可以通过下标(索引)来获取指定位置上的字符：字符串[索引]
说明：
	a.字符串：可以是字符串值，也可以是字符串变量
	b.[]: 中括号使固定语法
	c.索引：从0开始到字符串长度减1 （0对应第一个字符）； 
	       -1 ~ -长度（-1对应的是最后一个字符, -2对应的是倒数第2个字符）

注意：索引不能越界，否则会报错(产生异常)
'''

str1 = 'acbd' # a->0, c->1, b->2, d->3
print(str1[0])
# print(str1[4])  # IndexError: string index out of range

name = '王海飞'
print(name[1])

print(name[-1], name[-2], name[-3])
print('abc'[2])
# print(name[-4]) # IndexError: string index out of range

# 2. 获取部分字符(获取子串) -- 切片
# 字符串[下标1:下标2] ： 从下标1开始，获取到下标2前的所有的字符
# （从下标1开始，每次下标值加1，一直加到下标2前）
# 注意：下标1对应的位置，一定要在下标2对应的位置前
str2 = 'hello world'

print(str2[0:4])  # hell
print(str2[2:7])  # llo w
print(str2[2:-1]) # llo worl
print(str2[3:12]) # 切片时下标可以越界，越界的时候就取临界值
print(str2[-5:-2])
print(str2[-5:9])  


# 字符串[下标1:下标2:步进]
"""
从下标1开始获取，每次下标值增加步进值，没增加一次取一个字符，直到取到下标2前为止
注意：a.步进如果是正数，那么下标1对应的字符的位置一定要下标2对应的位置的前面；
	 步进是负数，那么下标1对应的位置一定要在下标2对应的位置的后面
	 b.下标2对应字符是取不到的
"""
str3 = 'helloPython'
print(str3[0:5:2])  # hlo   步进:3  hl  
print(str3[-1:5:-1]) # nohty

# 下标的省略
"""
切片的时候，下标1和下标2是可以省略的

下标1省略：默认从开头开始获取(开头可能是字符串的第一个字符，也可能是字符串的最后一个字符)

"""
str4 = 'good good study,day day up'
print(str4[:4])
print(str4[:4:-1])

"""
下标2省略: 从下标1位置开始获取，获取到结束(结束可能是字符串的最后一个字符，也可能是字符串的第一个字符)
"""
print(str4[1:])
print(str4[3::-1])

print(str4[:])  #  good good study,day day up
print(str4[::-1])  # pu yad yad,yduts doog doog

# 练习：要求将一个字符串中所有下标是奇数位上的字符获取出来
str5 = 'abcdefgh'
print(str5[1::2])  




















