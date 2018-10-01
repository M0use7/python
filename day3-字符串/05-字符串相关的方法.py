# python为字符串提供了很多的内建函数
# 字符串.函数()
# 注意：这些所有函数的功能都不会影响原来的字符串，而是产生一个新的字符串

str1 = 'hello python'
# 1.capitalize() 将字符串的第一个字符转换成大写
newstr = str1.capitalize()
print(newstr,str1)

# 2.center(width,fillchar)
# 让字符串变成width对应的长度，原内容居中，剩余的部分用fillchar的值来填充
# width - 整数；fillchar - 任意字符
print('abc'.center(10,'*'))

# 3.rjust(width,fillchar)
# 让字符串变成width对应的长度，原内容右对齐，剩余的部分用fillchar的值来填充
# 1 ---> 0001  11 ---> 0011  123 -> 0123

number = '1'
print(number.rjust(4,'0'))

# 4.原字符串.count(str)
# 判断str值在字符串中出现的次数
# str -> 字符串

print('abcabaa'.count('a'))

# 5.str1.join(str2)
# 在str2中的每个字符串之间插入str1
print('+'.join('abc'))

# 6.str1.replace(old,new)
# 将str1中old全部替换成new
new_str = 'abcdahulapuyeahj'.replace('a','+')
print(new_str)





