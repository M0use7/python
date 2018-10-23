"""__author__ = 余婷"""
# 1.已知一个列表，求列表中心元素
numbers = [1, 2, 5, 3, 7, 8, 9]
length = len(numbers)

if length % 2:
    # 如果是奇数个,中心元素的下标是长度//2
    print(numbers[length//2])
else:
    # 如果是偶数个，中心元素有两个
    print(numbers[length//2], numbers[length//2-1])

# 2.已知一个列表，求所有元素和
numbers = [1, 2, 5, 3, 7, 8, 9]
sum1 = 0
for item in numbers:
    sum1 += item
print(sum1)

# 3.已知一个列表，输出所有下标是奇数的元素
numbers = [1, 2, 5, 3, 7, 8, 9]

# index 是下标
for index in range(len(numbers)):
    if index % 2:
        # 打印奇数下标对应的值
        print(numbers[index])
print('================================')

# 4.已知一个列表，输出所有元素中，值为奇数的元素。
numbers = [1, 2, 5, 3, 7, 8, 9]
for item in numbers:
    if item % 2:
        print(item, end=' ')

print('===============================')

# 5.已知一个列表，将所有的元素乘以2。
numbers = [1, 2, 5, 3, 7, 8, 9]
# 因为要修改每个元素的值，所以使用下标去遍历
for index in range(len(numbers)):
    numbers[index] *= 2  # numbers[index] = numbers[index]*2

print(numbers)



"""
index = (0 ~ 6)
index = 0   numbers[0] = number[0]*2 = 1*2 = 2
index = 1   numbers[1] = number[1]*2 = 2*2 = 4
...
index = 6   numbers[6] = numbers[6]*2 = 9*2 = 18
"""

# 6.已知一个列表，将所有元素加到第一个元素中。
numbers = [1, 2, 5, 7, 8, 9]
# numbers = [[1,2,5,3,7,8,9], 2, 5, 3, 7, 8, 9]
# numbers[0] = numbers[:]
# print(numbers)

# sum(序列): python内置的求序列中元素的和的方法
numbers[0] = sum(numbers)
print(numbers)

# 7.已知一个列表A，将奇数位置元素存到B列表中，偶数元素存到C列表中。
A = [1, 2, 5, 7, 8, 9]
B = []
C = []
for index in range(len(A)):
    if index % 2:
        B.append(A[index])
    else:
        C.append(A[index])
print(B, C)

# 用切片做
B = A[1::2]
C = A[::2]
print(B, C)

# 9.有一个长度是10的列表，按递增排列，用户输入一个数，插入适当位置
numbers = [1, 2, 4, 5, 7, 8, 9, 18, 98, 100]
# # # 排序
# numbers.sort()
num = int(input('请输入一个数字:'))
for index in range(len(numbers)):
    # 找列表中第一个比输入的数大的位置，然后插入到它的前面
    if numbers[index] > num:
        numbers.insert(index, num)
        break
else:
    # 如果前面的数字都比输入的小，就添加到最后
    numbers.append(num)

print(numbers)

























