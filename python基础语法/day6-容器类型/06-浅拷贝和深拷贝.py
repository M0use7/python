"""__author__ = 余婷"""
import copy

# 总结：
"""
浅拷贝：只是单纯的将值拷贝（如果是对象就直接拷贝对象的地址）
深拷贝：会拷贝对象地址对应的值，产生一个新的地址，然后将新的地址进行赋值
"""

numbers1 = [1, 2]
numbers = [numbers1, 3, 4, 'abc']

# 浅拷贝
new_numbers = numbers.copy()
# 深拷贝
new_numbers2 = copy.deepcopy(numbers)

numbers1.append(100)
print(new_numbers)
print(new_numbers2)

# numbers.remove('abc')
# print(new_numbers)




