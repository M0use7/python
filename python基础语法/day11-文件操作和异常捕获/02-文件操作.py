"""__author__ = 余婷"""

"""
1.基本过程：打开文件 - 操作 - 关闭文件
2.open(路径,打开方式,encoding=编码方式)
a.路径: 绝对路径(了解), 相对路径: ./相对路径， ../, .../
b.打开方式: r,rb/br -- 读， w, bw/wb, a ---写
注意：路径不存在的时候，读的形式打开会报错。写的形式打开会自动新建文件
c.设置编码：utf-8, gbk
注意：如果是以二进制的形式打开文件(rb/br, wb/bw),不能设置编码方式

3.文件的读和写
read()/readline()  -- 读
write()  --- 写

4.关闭
f.close()  --- 良好的习惯
"""


"""
1.打开文件和关闭文件的简写方式(常用的):
with oepn() as 文件变量名:
    文件操作

文件打开操作完成后，会自动关闭文件
    
"""
if __name__ == '__main__':
    # 读二进制文件（上传文件）
    with open('./files/luffy4.jpg', 'rb') as f:
        # bytes是python中内置的数据类型，用来表示二进制数据
        content = f.read()
        print(type(content))
        print(content)

    # 将二进制数据写入文件(下载图片)
    with open('./files/new.jpg', 'wb') as ff:
        ff.write(content)



