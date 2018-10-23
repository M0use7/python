# 1. + 运算符
"""
字符串1+字符串2:
python支持两个字符串相加, 其效果就是将两个字符串拼接在一起产生一个新的字符串

注意：如果+的一边是字符串，那么另外一个也必须是字符串
"""
print('abc'+'123')
str1 = 'world'
newstr = 'hello' + ' ' + str1
print(newstr)

# print(10+'abc')  # TypeError: unsupported operand type(s) for +: 'int' and 'str'

# 2. * 运算符
"""
字符串1*整数: 字符串重复多次
"""
print('abc'*3)

# 3. 所有的比较运算符
str1 = 'abc'
print('abc' == str1)
print(str1 != 'ab')

# 比较大小
"""
str1 > str2; str1 < str2
让str1中的每一位的字符，分别和str2中每一位的字符依次比较。
直到不同为止，再看不同字符中谁的编码值大或者小
"""
print('dbcd' > 'abcde')
print('二' > '余婷')
print(ord('二'), ord('余'))   


# 4.in 和 not in
"""
str1 in str2: 判断str1是否在str2中(str2是否包含str1 / str1是否是str2的子串)

结果是布尔值
"""
print('abc' in 'a1b2cdefg')
print('f' not in 'python')  

# 5.获取字符串长度
# 字符串的长度，指的是字符串中字符的个数
# len()内置函数
str3 = 'project'
print(len(str3), len('abc 123\n'))

# 补充：空串
str4 = ''
str5 = ""
print(len(str5))

len1 = len(str3)   # len1 = 7
index = len1 - 1   # 6
print(str3[-1], str3[index])    


# 6.阻止转义
# 在字符串的最前面添加r/R可以阻止转义
print('a\nb','a\nb\\')
print(len('a\nb\\'))   # 4

print(r'a\nb',R'a\nb\\')
print(len(r'a\nb\\'))  # 6


print('a\\nb\\\\')  # a\nb\\
print('\\\n\\')  # \换行\

print(r'\\\n\\')  # \\\n\\  

# 练习
# str1 = r'\nabc123'  求：str1[3]   b 
# str2 = 'abc123\\123'  求： str2[-5]  3













