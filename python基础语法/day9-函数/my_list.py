"""__author__ = 余婷"""

empty = []


def count(list1, item):
    """
    统计指定列表中指定元素的个数
    :param list1: 指定的列表
    :param item: 指定的元素
    :return: 个数
    """
    num = 0
    for x in list1:
        if x == item:
            num += 1
    return num

print('abc')
print(empty)
print(count(['a', 12, 'b', 'a'], 'a'))
