"""__author__ = 唐宏进 """

import re

# 1.compile(正则表达式)：将正则表达式转换成正则表达式对象
re_str = r'\d+'
re_object = re.compile(re_str)
print(re_object)

# 不转成对象，调用相应的函数
re.match(re_str, '78s')
# 转换成对象，调用相应的方法
re_object.match('78r')

# 2.match(正则表达式,字符串)和fullmatch
# match:判断字符串的开头是否能够和正则表达式匹配
# fullmatch:判断整个字符串是否能够和正则表达式匹配
# 返回值都是匹配结果，如果匹配成功返回匹配对象，否则返回None
re_str = r'abc\d{3}'
match1 = re.match(re_str, 'abc123abcdef')
match2 = re.fullmatch(re_str, 'abc123')
print(match1)
print(match2)

# a.匹配到的范围。匹配结果字符的下标范围
print(match1.span())
# 获取起点
print(match1.start())
# 获取终点
print(match1.end())

# 注意：group参数，用来指定分组对应的相应的结果
re_str = r'(\d{3})\+([a-z]{2})'
match1 = re.match(re_str, '123+ab123')
print(match1.span())
print(match1.span(1))
print(match1.span(2))

# 在匹配结果中，获取第2个分组的起始下标
print(match1.start(2))

# b.获取匹配结果对应的字符串
print(match1.group())
print(match1.group(1))
print(match1.group(2))

# c.获取被匹配的原字符串
print(match1.string)

# 3.search(正则表达式, 字符串)：
# 在字符串中去查找第一个满足正则表达式要求的子串,如果找到了就返回匹配对象，否则返回None
search1 = re.search(r'\d+aa', 'hel11aalo wo3aarpld')
print(search1)
if search1:
    print(search1.span())

# 练习：使用search将一个字符串中所有的数字字符串全部找到
# '工资是10000元，年龄是18岁，身高：180，颜值100分'
re_str = r'[1-9]\d*'
str1 = '工资是10000元，年龄是18岁，身高：180，颜值100分'
search1 = re.search(re_str, str1)
while search1:
    print(search1.group())
    end = search1.end()
    str1 = str1[end:]
    search1 = re.search(re_str,str1)

# 4.split(正则表达式，字符串)
# 按满足正则表达式的子串去切割字符串
str1 = '窗前明月光，疑是地上霜。举头望明月，低头思故乡！'
result = re.split(r'\W',str1)
print(result)

# 中文属于\w范围
# 5.sub(正则表达式,替换字符串,被替换字符串)
word = '你是SB吗，操你大爷的，Fuck you'
result = re.sub(r'SB|操|Fuck','*',word)
print(result)

# 6.findall(正则表达式,字符串)
# 获取字符串中所有满足正则表达式的子串
# 返回值是列表
# 注意：分组中的捕获效果在这儿有效
result = re.findall(r'\d([a-z]+)','北京1beijing,欢迎welcome你2you')
print(result)