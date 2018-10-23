"""__author__ = 余婷"""

a = 10

def func1():
    print('good!')

print(__name__)

# 将不希望被别的模块导入(执行)的代码放到模块的这个if语句中
if __name__ == '__main__':
    print('!!', a)
    for x in range(10):
        print('!!', x)
