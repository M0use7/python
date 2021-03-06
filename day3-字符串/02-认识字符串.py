# 1.什么是字符串
'''
a.用单引号或者双引号括起来的字符集就是字符串
'asd123!%&^中文',"a k789"
b.字符串中的每个独立的单元我们叫字符，
例如：字符串'abc123'中的'a','b','c','1','2','3'就是字符
'''
name = '李好'

#2.转义字符
'''
说明：python中没有字符类型，如果要表示字符，就用长度是1的字符串表示
长度：指的就是字符串中字符的个数。
例如：'abc' - 长度是3，'abc123, 你好' - 长度是10


通过\将一些特殊的字符转换成一个具有特殊功能或者特殊意义的字符就是转义字符
常见的转义字符：
\n --- 换行
\t --- 制表符(相当于tab键)
\\ ---\
\' ---'
\" ---"
转义字符的的长度是1
'''
poem = '床前明月光,\n疑是地上霜'
print(poem)

str1 = '(a + c)\\b'
print(str1)

str2 = '\'abc\''
print(str2)

# 3.Unicode编码
'''
a.python中字符的编码采用的是Unicode编码
b.Unicode是采用两个字节对一个字符进行编码(2^5),能够将世界上所有的符号进行编码
c.Unicode编码中包含了ascii码

将字符转成指定的数值，这个过程就是编码。(编码的目的是方便计算机存储)
将数值转换成对应的符号的过程就是反编码
0 --> 0
'0' --> 48
'''
# 1.将Unicode码转换成字符：chr(编码)
print(chr(0xA000))
print(chr(0x4E00))

# 2.将字符转换成Unicode编码：ord(字符)
code1 = ord('唐') #结果是10进制
code2 = ord('宏')
code3 = ord('进')
print(hex(code1),hex(code2),hex(code3))


