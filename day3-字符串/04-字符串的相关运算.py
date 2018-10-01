# 1.+ 运算符
'''
 python支持两个字符串相加,
 其效果就是将两个字符串拼接在一起，产生一个新字符串

 注意：如果+的一边是字符串，那么另外一个也必须是字符串
'''
print('abc'+'123')
str1 = 'world'
newstr = 'hello' + ' ' + str1
print(newstr)

# 2.* 运算符
'''
字符串*整数；字符串重复多次

'''
print('abc'*3)

# 3.所有的比较运算符
str2 = 'abc'
print('abc'== str2)
print('abc'!= str2)

# 比较大小
'''
str1 > str2; str1 < str2
让str1中的每一位字符，分别和str2中的每一位字符比较，
直到不同为止，再看不同字符中谁的编码大还是小
'''
print('dbcd' > 'abcde')
print('唐宏进' > '余婷')
print(ord('唐'),ord('余'))


# 4.in 和 not in
'''
str1 in str2:判断str1是否在str2中

结果是布尔值
'''
print('abc' in 'a1bc123')
print('f' not in 'python')


# 5.获取字符串长度
# 字符串的长度指的是字符串字符的个数
# len()内置函数
str3 = 'project'
print(len(str3),len('abc 123\n'))

# 补充：空串
str4 = ''
str5 = ""
print(len(str5))

print(str3[-1],str3[len(str3)-1])


# 6.阻止转义
# 在字符串的最前面添加r/R可以阻止转义
print('a\nb')
print(len('a\nb\\')) # 4

print(r'a\nb',R'a\nb\\')
print(len(r'a\nb\\')) # 6


# 练习
# str1 = r'\nabc123' 求：str1[3] b
# str2 = 'abc123\\123' 求：str2[-5] 3



