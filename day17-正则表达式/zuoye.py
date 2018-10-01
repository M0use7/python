"""__author__ = 唐宏进 """

import re
# 1. 写一个正则表达式判断一个字符串是否是ip地址
# 规则：一个ip地址由4个数字组成，每个数字之间用.连接。每个数字的大小是0-255
# 255.189.10.37   正确
# 256.189.89.9    错误
# IP = input('请输入IP地址:')
#
# re_str = r'((\d|[1-9]\d|1\d{2}|2[0-4]\d|25[0-5])\.){3}(\d|[1-9]\d|1\d{2}|2[0-4]\d|25[0-5])'
#
# if re.fullmatch(re_str, IP):
#     print('地址格式合法！')
#
# else:
#     print('地址格式不合法！')
#
# 2.计算一个字符串中所有的数字的和
# 例如：字符串是：‘hello90abc 78sjh12.5’ 结果是90+78+12.5 = 180.5
# sum = 0
# str1 = 'he001llo90abc 78sjh12.5'
# re_str = r'[1-9]\d*[.]?\d*|0[.]\d+'
# result = re.findall(re_str, str1)
# for x in result:
#     sum += float(x)
# print(sum)

# 3. 验证输入的内容只能是汉字
# str1 = input('请输入汉字:')
# re_str = r'[\u4E00-\u9FA5]+'
# if re.fullmatch(re_str,str1):
#     print('格式正确')
# else:
#     print('格式错误')

#
# 4. 电话号码的验证
# tel = input('请输入电话号码:')
# re_str = r'1[358][0-9]{9}'
# if re.fullmatch(re_str, tel):
#     print('格式正确')
# else:
#     print('格式错误')
#
# 5. 简单的身份证号的验证
# id_number = input('请输入身份证号码:')
# re_str = r'\d{6}(19\d\d|200\d|201[0-8])([0][1-9]|[1][0-2])(0[1-9]|[1-2]\d|3[0-1])\d{3}[\dxX]'
# if re.fullmatch(re_str, id_number):
#     print('格式正确')
# else:
#     print('格式错误')
print(re.fullmatch('\w{4}|\w{4}-\w{3}','back-end'))