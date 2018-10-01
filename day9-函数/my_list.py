"""__author__ = 唐宏进 """

empty = []

def count1(list1,item):
    """
    统计指定列表中指定元素的个数
    :param list1: 指定的列表
    :param item: 指定的元素
    :return: 个数
    """
    count = 0
    for x in list1:
        if x == item:
            count += 1
    return count

def len1(list:list):
    """
    计算列表的长度
    :param list: 指定的列表
    :return: 长度
    """
    length = 0
    for _ in list:
        length += 1
    return length

def sort1(list:list):
    """
    给列表中的元素升序排序
    :param list: 指定的列表
    :return: 排序后的列表
    """
    for i in range(len1(list)):
        for j in range(i+1,len1(list)):
            if list[i] > list[j]:
                list[i],list[j] = list[j],list[i]
    return list

def max1(list:list):
    """
    找出列表中的最大值
    :param list: 指定的列表
    :return: 最大值
    """
    sort1(list)
    return list[-1]

