# 1.认识字符串，'圣诞节开发ya123', "abc%u23", '\n\t\\\'\"', '',""
# 2.python中的字符编码: Unicode , 使用两个字节来对一个字符进行编码
# 3.获取字符串中的字符
"""
a.获取单个字符
字符串[下标]
下标不能越界：0 ~ 长度-1,  -1 ~ -长度

b.获取部分字符(切片)
字符串[下标1:下标2:步进] ，没有步进的时候，相当于步进是1
"""

# 4.相关运算
# a.str1+str2 , 拼接
# b.str1*整数, 字符串重复
# c.比较运算， == ， != , >, <, >=, <=
# d. in, not in

# 5.长度
# len(str1)

# 6.相关的方法


# 字符串的格式化
"""
带格式符的字符串 % (格式符对应的值) 
说明：%是固定的格式； ()也是固定格式。
     带格式符的字符串中有几个格式符，那么后面的括号中就必须有几个和它一一对应的值。

%s ---> 字符串
%d ---> 整数
%f ---> 浮点数    %.nf ---> 保留小数点后n位小数
%c ---> 字符    可以将数字转换成字符拼接到字符串中
"""
first_name = '张'
last_name = '三'
age = 28

name = first_name + last_name
print(name)

# hello, XXX! 今年X岁
newstr = 'hello,%s%s! 今年%d岁' % (first_name, last_name, age)
print(newstr)

# 金额是：xx.xx元
money = 999
newstr = '金额是:%.2f元' % (money)
print(newstr)

# %c的用法
# a:
unit = '$'
newstr = '金额是:%.2f%c' % (money, unit)
print(newstr)

# b:
char_code = 97
newstr = '%d对应的字符是%c' % (char_code, char_code)
print(newstr)  

# %x/%X
number = 1000
newstr = '%d的十六进制是:0x%X' % (number, number)
print(newstr)


# 练习：使用变量保存学生的名字，年龄和成绩
# xxx今年xx岁，他的语文成绩是xxx分。 要求成绩只保留一位小数
student_name = '小明'
age = 30
score = 80
message = '%s今年%d岁，他的语文成绩是%.1f分。' % (student_name, age, score)
print(message)




























