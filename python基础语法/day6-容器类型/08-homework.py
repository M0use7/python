"""__author__ = 余婷"""

# 9.输出9*9口诀。 1.程序分析：分行与列考虑，共9行9列，i控制行，j控制列。
# x*y
# x: 每一行从1 ~ 行数
# y: 就是行数
for y in range(1, 10):
    for x in range(1, y + 1):
        print('%dx%d=%d' % (x, y, x*y), end=' ')
    # 换行
    print()


