"""__author__ = 唐宏进 """

"""
1.
程序中不管操作任何文件，不管怎么操作，过程都是：打开文件 -> 操作(读/写) -> 关闭文件

2.
做数据持久化、本地化，都要使用文件来保存数据
（数据库文件、txt文档、jsan文件、plist文件，xml文件等、二进制文件(图片、视频、音频等)）

程序中通过变量、列表、字典等保存的数据，在程序结束后都会被销毁的。
"""

"""
1.打开文件
open(文件地址,打开方式,encoding=编码方式)
a.文件地址：告诉open函数要打开的是哪个文件，填文件路径。可以填绝对路径，也可以填相对路径
绝对路径：C:/Users/Administrator/Desktop/1.txt
相对路径:./相对路径（相当于当前文件所在的目录）
        ../相对路径（相当于当前文件所在的目录的上一层目录）
        .../相对路径（相当于当前文件所在的目录的上一层目录的上一层）

b.打开方式：获取文件的内容以读的形式打开，往文件中写内容就以写的形式打开
'r' --> 读(默认值)，读出来的内容以文本的形式返回
'rb/br' --> 读，读出来的内容以二进制(bytes)的形式返回
'w' --> 写，写文本到文件中
'wb/bw' --> 写，写二进制数据到文件中
'a' --> 写，追加

c.编码方式：以文本的形式读和写的时候才需要设置编码方式。
utf-8:万国码
gbk:只支持中文

d.open函数的返回值是被打开的文件对象

2.关闭文件
文件对象.close()
"""
# 1.打开文件
# f1 = open('C:/Users/Administrator/Desktop/1.txt')
# f2 = open('./test.txt',encoding='utf-8')
#
# # 2.关闭文件
# f1.close()
# f2.close()

# 3.操作文件
# a.读操作
# 打开文件，f就是被打开的文件对象
f = open('./test.txt', 'r', encoding='utf-8')
content = f.read()
print(content)
f.close()

f1 = open('./test.txt', 'r', encoding='utf-8')
# 从文件开始读到第一行结束
print('------------------------华丽的分割线---------')
content = f1.readline()
print(content)
# 从第二行开始，读到第二行结束
print(f1.readline())

# 从第三行开始，读到文件结束
print(f1.read())
f1.close()

# 练习：读文件中的内容，一行一行的读
print('~~~~~~~~~~~~~~~~~~~~~~~')
f = open('./test.txt', 'r', encoding='utf-8')
content = f.readline()
while content:
    print(content)
    content = f.readline()
f.close()

# b.写操作
"""
'w' --> 写操作,完全覆盖原文件的内容
'a' --> 写操作，在源文件的内容后去追加新内容
"""
# f = open('./test.txt', 'a', encoding='utf-8')
# f.write('程序员的诗')
# f.close()

# 4.文件不存在的情况
"""
当以读的形式打开文件的时候，如果文件不存在，程序会崩溃
当以写的形式打开一个不存在的文件的时候，会自动创建一个新的文件
"""
f = open('./test2.txt', 'a', encoding='utf-8')
f.write('程序员的诗')
f.close()

# 练习：统计一个模块执行的次数
f = open('./number', 'r', encoding='utf-8')
# 从文件中获取次数
number = int(f.read())
# 打印次数
print(number)
f.close()

number += 1
f = open('./number', 'w', encoding='utf-8')
f.write(str(number))
f.close()

