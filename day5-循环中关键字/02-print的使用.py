# 1.一个print打印完内容后，默认会换行
str1 = 'abc'
print(str1)
print(str1)

# 2.一个print可以同时打印多个内容，多个内容之间用逗号隔开。
# 打印效果，多个内容间默认是空格隔开
print(str1,'aaa',123)

# 3. 设置一个print打印结束后的样式(默认是换行)
# end=字符串
print('aaa',end = ',')
print('bbb')
print('ccc')

# 4.设置同时打印多个内容，内容之间的样式(默认是空格)
print('a','b','c',sep='*')



