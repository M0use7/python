# python为字符串提供了很多的内建函数
# 字符串.函数()
# 注意：这些所有的函数的功能都不会影响原来的字符串，而是产生一个新的字符串

str1 = 'hello python'
# 1.capitalize() 将字符串的第一个字符转换为大写
newstr = str1.capitalize()
print(newstr, str1)

print('abc'.capitalize())

# 2.center(width, fillchar) 
# 让字符串变成width对应的长度，原内容居中，剩余的部分使用fillchar的值来填充
# witdh - 整数； fillchar - 任意字符
print('abc'.center(10, '*'))  # ***abc**** 

# 3. rjust(width, fillchar)
# 让字符串变成width对应的长度，原内容靠右，剩余的部分使用fillchar的值来填充
# 2015103001 2015103002 2015103015
# 1 2  3  4  5  11  20  ----> 001 002 003 010 011 012
# 1 --> 0001  11 -> 0011  123 -> 0123
number = '12'
new_id = number.rjust(4, '0')
print(new_id)  

# 3.原字符串.count(str)
# 判断str值在原字符串中出现的次数
# str -> 字符串
print('abcabaa'.count('ab'))  

# print('贰1壹二2一'.isnumeric())

# 4.str1.join(str2)
# 在str2中的每个字符串之间插入一个str1
print('-+'.join('abc'))

# 5.str1.replace(old, new)
# 将str1中old全部替换成new
new_str = 'abcdahulapuyeahj'.replace('a','+')
print(new_str)













