# 题目1
'''
name = 'ZhangSan'
print('Hello %s, would you like to learn some Python today?'%(name))

'''

# 题目2
'''
name = 'zHaNgsAn'
print(name.lower())
print(name.upper())
print(name.capitalize())
'''

# 题目3
# name = 'Ralph Waldo Emerson'
# word = 'Don’t be pushed by your problems. Be led by your dreams.'
# print('%s said,\"%s\"'%(name,word))

# 题目4
'''
famous_person = 'Ralph Waldo Emerson' 
message = 'Don’t be pushed by your problems. Be led by your dreams.'
print(famous_person,message)
'''

# 题目5
'''
name = '\tZhangSan\n'
print(name)
print(name.lstrip())
print(name.rstrip())
print(name.strip())
'''

# 字符串1.lstrip(字符串2)
# 从字符串1中的第一个字符开始，判断字符是否在字符串2中，如果在就删除这个字符，
# 然后再看下一个字符是否在字符串2，依次类推，直到字符串1中的字符不在字符串2中
str = 'aaa123aa123'
print(str.lstrip('a3'))
print(str.rstrip('a3'))
