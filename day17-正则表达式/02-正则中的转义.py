"""__author__ = 唐宏进 """
from re import fullmatch

"""
1.
正则表达式中的转义和字符串中的转义字符没有任何关系。
在python中的字符串前加r阻止的是字符串的转义，不能阻止正则表达式的转义
2.
在正则表达式中，可以通过在有特殊意义的符号前加'\'来表示符号本身
\+ \. \* \? \\ \( \) \[ \] \^ \$ \|
注意：
a.- 号只有在中括号中的两个字符之间才有特殊的意义
b.如果特殊符号放在[]中作为字符集的内容，那么除了-号在两个字符之间以外，其他的都不需要转义
c.\不管在哪儿都需要转义，^放在中括号的最前面需要转义

"""
re_str = r'a\+-'
print(fullmatch(re_str, 'a+-'))

re_str = r'\\w'
print(fullmatch(re_str, '\w'))

re_str = r'\(\d{2}\)'
print(fullmatch(re_str, '(12)'))

re_str = r'[\^.\\?*]abc'
print(fullmatch(re_str, '^abc'))
