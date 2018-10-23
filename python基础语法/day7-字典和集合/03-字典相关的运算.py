"""__author__ = 余婷"""

# 1.字典不支持'+'和'*'
# 2. in 和 not in : 是判断key是否存在
computer = {'brand': '联想', 'color': 'black'}
print('color' in computer)

# 3.len()
print(len(computer))

# 4.字典.clear()
# 删除字典中所有的元素(键值对)
computer.clear()
print(computer)

# 5.字典.copy()
# 拷贝字典中的所有的元素，放到一个新的字典中
dict1 = {'a': 1, 'b': 2}
dict2 = dict1    # 将dict1中的地址赋给dict2，两个变量指向同一块内存区域
dict3 = dict1.copy()   # 将dict1中的内存复制到一个新的内存区域中，然后将新的地址给dict3
dict1['a'] = 100
print(dict2)   # {'a': 100, 'b': 2}
print(dict3)   # {'a': 1, 'b': 2}

# 6.dict.fromkeys(序列,默认值=None)
# 将序列中的每个值作为key,默认值为value创建一个新的字典。
# 注意：默认值可以不写，写的话只能写一个值
print(dict.fromkeys('abc', 0))  # {'a': 0, 'b': 0, 'c': 0}
print(dict.fromkeys(['name', 'age', 'sex'], [1, 2]))



# 7.字典.keys()(了解)
# 获取字典中所有的key，以dict_keys的形式返回
all_key = dict1.keys()
for key in all_key:
    print(key)

# 8.字典.values()(了解)
# 获取字典中所有的value
print(dict1)
all_value = dict1.values()
print(all_value)

# 9.字典.items()
print(dict1.items())
# 这种方式不推荐使用
for key, value in dict1.items():
    print(key, value)


# 10.字典.setdefault(key, 默认值=None)
# 给字典添加键值对。如果key本身就存在，这个方法无作为
dict1.setdefault('ab', 'abc')
dict1.setdefault('dd')
print(dict1)

# 11.字典1.update(字典2)
# 将字典2中的键值对更新到字典1中
# 更新方式: 如果字典2的key,在字典1中是存在的，就字典2中的值去更新字典1中的值。不存在就添加到字典1中
dict1 = {'aa': 1, 'bb': 'abc', 'cc': True}
dict1.update({'aa': 99, 'dd': '你好'})
print(dict1)












