# 1.个性化消息: 将用户的姓名存到一个变量中，并向该用户显示一条消息。显示的消息应非常简单，
# 如“Hello Eric, would you like to learn some Python today?”。
user_name = '骆老师'
print('Hello %s, would you like to learn some Python today?' % (user_name))
print('Hello '+user_name+', would you like to learn some Python today?')

# 2.调整名字的大小写: 将一个人名存储到一个变量中，
# 再以小写、大写和首字母大写的方式显示这个人名。
name = 'LuFfY zUoLuO'
print(name.lower())
print(name.upper())
print(name.title())  # 将字符串中，每个单词的首字母大写，其余的全部变成小写

# 3.名言: 找一句你钦佩的名人说的名言，将这个名人的姓名和他的名言打印出来。
# 输出应类似于下面这样(包括引号):
# Albert Einstein once said, “A person who never made a mistake never tried anything new.”
# 一人之人
name = '宝儿姐'
word = '别人都说我瓜，其实我一点儿都不瓜，大多数的时候我都机智的一逼~'
print('%s once said,\"%s\"' % (name, word))


# 4.剔除人名中的空白: 存储一个人名，并在其开头和末尾都包含一些空白字符。
# 务必至少使用字符组合"\t" 和"\n" 各一次。
# 打印这个人名，以显示其开头和末尾的空白。
# 然后，分别使用剔除函数lstrip() 、rstrip() 和strip() 对人名进行处理，并将结果打印出来。
name = ' \t\n  xiao\t\n ming\n\t '
print('==='+name+'===')

# lstrip(): 删除字符串开头的所有的空白字符
print('==='+name.lstrip()+'===')

# rstrip(): 删除字符串中后面的空白字符
print('==='+name.rstrip()+'===')

# strip(): 同时删除字符串开头和结束的所有的空白字符
print('==='+name.strip()+'===')


numer = '000019099'
print(numer.lstrip('0'))

numer = '2abd000072763'

# 字符串1.lstrip(字符串2)：
# 从字符串1中的第一个字符开始，判断字符是否在字符串2中，如果在就删除这个字符，
# 然后再看下一个字符是否在字符串2，依次类推，直到字符串1中的字符不在字符串2中为止
# 如果字符串1中的第一个字符就不在字符串2中，就一个字符都不用删
print(numer.lstrip('0adb'))

















