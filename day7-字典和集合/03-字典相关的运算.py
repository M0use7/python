"""__author__ = 唐宏进 """
# 1.字典不支持'+'和'*'
# 2.in 和 not in
computer = {'brand':'联想','color':'blank'}
print('color' in computer)

# 3.len()
print(len(computer))

# 4.字典.clear()
# 删除字典中所有的元素（键值对）
computer.clear()
print(computer)

# 5.字典.copy()
# 拷贝字典中的所有元素，放到一个新的字典中
dict1 = {'a':1, 'b':2}
dict2 = dict1 # 将dict1中的地址赋给dict2，两个变量指向同一块区域
dict3 = dict1.copy() # 将dict1中的内存复制到一个新的内存区域中，然后将新的地址给dict3
dict1['a'] = 100
print(dict2)
print(dict3)

# 6.dict.fromkeys(序列,默认值=None)
# 将序列中的每个值作为key，默认值为value创建一个新的字典
print(dict.fromkeys('abc',0))
print(dict.fromkeys(['name','age','sex'],0))

# 7.字典.keys()
# 获取字典中所有的key，以列表的形式返回
al_key = dict1.keys()
for key in al_key:
    print(key)

# 8.字典.value（了解）
all_value = dict1.values()
print(all_value)

# 9.字典.items()
print(dict1.items())
# 这种方式不推荐使用
for key,value in dict1.items():
    print(key,value)

# 10.字典.default(key,默认值 =  None)
# 给字典添加键值对。如果key本身就存在，这个方法无作为
dict1.setdefault('c',)
print(dict1)

# 11.字典1.update(字典2)
# 将字典2中的键值对更新到字典1中
# 更新方式：如果字典2的key,在字典1中是存在的，就拿字典2中的值去更新字典1中的值。不存在就添加到字典1中
dict1 = {'aa':1, 'bb':'abc', 'cc':True}
dict1.update({'aa':90, 'dd':'你好'})
print(dict1)