"""__author__ = 余婷"""

from re import fullmatch, search, findall

"""
正则表达式就是用来检测字符串是否满足某种规则的工具
例如：1.账号是手机号/邮箱/多少位由什么东西组成等.....
     2.烧开后付款后，按时发哈哈哈。安徽省发动机卡死？卡喝咖啡会！
     3.脏话替换成*等.....
     

1.正则语法
2.python对正则表达式的支持，提供了一个内置模块：re
fullmatch(正则表达式, 字符串)：判断整个字符串是否符合正表达式规则
"""
# ==========================1.单个字符==========================
# 1) . 匹配任意字符
# 匹配一个字符串，只有一位字符并这个字符是任意字符
re_str = r'.'
result = fullmatch(re_str, 'a')
print(result)

# 匹配一个字符串，只有两位字符并这每个字符都是任意字符
re_str = r'..'
result = fullmatch(re_str, 'an')
print(result)

# 匹配一个字符串，前三位分别是abc，最后一位是任意字符
re_str = r'abc.'
result = fullmatch(re_str, 'abc%')
print(result)

# 2) \w 匹配字母数字下划线
# 匹配一个字符串，前三位分别是abc,最后两位是字母数字或者下划线
re_str = r'abc\w\w'
result = fullmatch(re_str, 'abc2g')
print(result)

# 3) \s 匹配空白字符（空白指空格、制表符(\t)和回车(\n)等所有能产生空白的字符）
# 匹配一个字符串，前三位是字母数字下划线第四位是一个空白字符最后一位是任意字符
re_str = r'\w\w\w\s.'
result = fullmatch(re_str, 'hu2\t?')
print(result)

# 4) \d 匹配一个数字字符
# 匹配一个字符串，前三位是数字字符，最后一位是任意字符
re_str = r'\d\d\d.'
result = fullmatch(re_str, '782L')
print(result)

# 5) \b 检测是否是单词边界(单词的开头、单词的结尾、单词和单词之间的标点空格等)
# 注意：正则中遇到\b，匹配的时候先不管它，匹配成功后再回头看\b位置是否是单词边界
# 匹配一个字符串是前四位是when，第五位是空白，空白后边是where。并且第四位n的后面是个单词边界
re_str = r'when\b\swhere'
result = fullmatch(re_str, 'when where')
print(result)

re_str = r'abc\b'
result = fullmatch(re_str, 'abc')
print(result)

# 6) ^ 检测字符串是否以给定的正则表达式开头
# 匹配一个字符串，是否以两个数字字符开头
re_str = r'^\d\d'
result = fullmatch(re_str, '23')
print(result)

result = search(r'^\d\d', '99abc11hkj')
print(result)

# 7) $ 检测字符串是否以给定的正则表达式结束
# 匹配一个字符串a数字，并且a数字是字符串的结尾
re_str = r'a\d$'
result = fullmatch(re_str, 'a8')
print(result)

result = search(re_str, 'a9aaa8')
print(result)


# 8) \W 匹配一个非数字、字母、下划线的字符
re_str = r'\W\w'
result = fullmatch(re_str, '!a')
print(result)

# 9) \S 匹配非空白字符
re_str = r'\S\w\w\w'
result = fullmatch(re_str, '@a2h')
print(result)

# 10) \D 匹配一个非数字字符
# 11) \B 检测非单词边界

# =============================匹配次数=============================
# 1) [] 匹配中括号中出现的任意字符
# 注意：一个中括号只匹配一个字符
# 匹配一个3位的字符串，第一位是a或者b或者c,后两位是数字
re_str = r'[abc+]\d\d'
result = fullmatch(re_str, '+67')
print(result)

# - 在正则中的中括号中的应用：如果将减号放到两个字符的中间代表的是谁到谁。如果想要表示'-'符号本身，就放在开头或者结尾
# [1-8]: 代表的字符集是：'1','2','3','4','5','6','7','8'
# [-18]或者[18-]: 代表的字符集是'1','8','-'
# 要求一个字符串中的第一个是1-8中的一个，后面两位是小写字母
re_str = r'[1-8][a-z][a-z]'
result = fullmatch(re_str, '2hn')
print(result)

re_str = r'[!+-][A-Z]'
result = fullmatch(re_str, '-D')
print(result)

# 2) [^字符集] 匹配不在[]字符集中的任意一个字符
# 匹配一个四位的字符串，第一位不是大写字母也不是数字，后三位是abc
re_str = r'[^A-Z\d]abc'
result = fullmatch(re_str, '#abc')
print(result)

# 3) * 匹配0次或者多次
# 匹配一个字符串，最后一位是b,b的前面有0个或者多个a
re_str = r'a*b'  # 'b', 'ab','aab', 'aaab', 'aaaab' .....
print(fullmatch(re_str, 'aaaaab'))

re_str = r'\d*'
re_str = r'[abc]*'   # '','a', 'ab', 'aa', 'abccabc' .....

# 4) + 匹配1次或者多次（至少一次）
# 判断一个字符串是否是无符号的正整数
re_str = r'[1-9]+\d*'  # 10， 11， 100 ,1000
print(fullmatch(re_str, '1010'))

# 5) ? 匹配0次或者一次
re_str = r'@?\d+'
print(fullmatch(re_str, '@16723'))

# 判断一个字符串是否是整数(包含正整数和负整数)
# +200, -120, 99, -1, 3, +4
re_str = r'[+-]?[1-9]+\d*'
print(fullmatch(re_str, '200'))

# 6) {N} 匹配N次
re_str = r'\d{3}'      # 匹配3位数字字符串
re_str = r'[a-zA-Z]{3}'   # 匹配3位字母字符串
print(fullmatch(re_str, 'aHh'))

# 7) {N,} 至少匹配N次
re_str = r'\w{4,}'
print(fullmatch(re_str, 'hanc_123'))

# 8) {,N} 最多匹配N次
re_str = r'a{,4}b'  # 'b', 'ab', 'aab', 'aaab','aaaab'
print(fullmatch(re_str, 'aaaab'))

# 9) {M,N} 匹配至少M次，最多N次 (N>M)
re_str = r'a{2,4}b'  # 'aab', 'aaab', 'aaaab'
print(fullmatch(re_str, 'aaab'))

# ==============================3.分之和分组======================
# 1) | 分之(相当于逻辑运算中的or)
# 匹配一个字符串是三个字母或者是三个数字
re_str = r'[a-zA-Z]{3}|\d{3}'
print(fullmatch(re_str, 'abc'))

# '\d{3}[a-z]{2}'是分之中的第一个条件， '[A-F]{3}'是分之的第二个条件
re_str = r'\d{3}[a-z]{2}|[A-F]{3}'
print(fullmatch(re_str, 'ABC'))

# 注意：正则中的分之有短路操作：如果使用|去连接多个条件，前面的条件已经匹配出结果，那么就不会使用后面的条件再去匹配了
# 练习：写一个正则表达式，能够匹配出字符串中所有的数字（包括整数和小数）
# 'abc12.5hhh60,30.2kkk9nn0.12'
# 100, 89.89, 20.12, 0.23
# re_str = r'[1-9]\d*[.]?\d*|0[.]\d+'
# # print()
re_str = r'[1-9]\d*|\d+[.]\d+'
re_str = r'\d+[.]\d+|[1-9]\d*'
print(findall(re_str, 'abc12.5hhh60,30.2kkk9nn0.12'))

# 2) 分组
# a.分组
# 通过加()来对正则条件进行分组
# 两位数字两位字母出现3次   ac23bn45hj34
re_str = r'([a-z]{2}\d{2}){3}'
print(fullmatch(re_str, 'ac23bn45hj34'))

# 匹配一个字符串，按照一个数字一个字母的规律出现一次或者多次
re_str = r'(\d[a-z])+'
print(fullmatch(re_str, '9a2s3k4k9o'))

# b.重复
# 可以通过\数字来重复匹配前面的分组中匹配的结果。数字的值代表前面的第几个分组
re_str = r'(\d{2}[A-Z])=%\1\1'
print(fullmatch(re_str,'23B=%23B23B'))

re_str = r'(\d{3})-(\w{2})\1{2}\2'
print(fullmatch(re_str,'123-aa123123aa'))

# c.捕获
# 按照完整的正则表达式去匹配，只捕获()中的内容。只有在findall中有效
re_str = r'a(\d{3})b'
print(fullmatch(re_str, 'a786b'))
print(findall(re_str, 'a786b'))




# 练习：
# 用户名必须由字母、数字或下划线构成且长度在6~20个字符之间
# QQ号是5~12的数字且首位不能为0
user_name = input('用户名:')
qq = input('QQ:')

if fullmatch(r'\w{6,20}', user_name):
    print('用户名合法')
else:
    print('用户名不合法')

if fullmatch(r'[1-9]\d{4,11}', qq):
    print('QQ号合法')
else:
    print('QQ号不合法')






# 注意：次数相关的操作，都是约束的次数符号前的前一个字符































