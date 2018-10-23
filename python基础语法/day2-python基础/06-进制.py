# 计算机中常用的进制有：二进制、八进制、十进制、十六进制

# 十进制：
# 1.基数：0，1，2，3，4，5，6，7，8，9 例如：7283， 23901
# 2.进位：逢10进1   
# 3.十进制数上的每一位：123 = 100+20+3 = 10^2*1+10^1*2+10^0*3
 # 3451 = 10^0*1 + 10^1*5 + 10^2*4 + 10^3*3

# 二进制：
# 1.基数：0，1  例如：110，10101，10001
# 2.进位：逢2进1     
# 3.二进制数上的每一位：1011 = 2^0*1 + 2^1*1 + 2^2*0 + 2^3*1 = 11(十进制)
# 数学规定：所有的数的0次方都是1

# 八进制：
# 1.基数：0，1，2，3，4，5，6，7
# 2.进位：逢8进1     
# 3.八进制数上的每一位：123 = 8^0*3 + 8^1*2 + 8^2*1 = 83(十进制)

# 十六进制：
# 1.基数：0-9,a-f(A-F) -- a(10)~f(15)  例如：1af 
# 2.进位: 逢16进1  
# 3.十六进制数上的每一位：123 = 16^0*3 + 16^1*2 + 16^2*1 = 291(十进制)



# 进制间的转换
# 1.二进制、八进制、十六进制 ---> 十进制
# 进制数^位数(从0开始)*每一位上的值的和
# 123(16) = 16^0*3 + 16^1*2 + 16^2*1 = 291(10)
# 123(8) = 8^0*3 + 8^1*2 + 8^2*1 = 83(10)
# 1011(2) = 2^0*1 + 2^1*1 + 2^2*0 + 2^3*1 = 11(10)



# 2.八进制、十六进制 ---> 二进制
# 将一位的八进制转换成3位的二进制。将一位的十六进制转换成4位的二进制
# 123(8) -> 001010011(2)
# 10(8) -> 001000(2)
# 123(16) -> 000100100011(2)
# 10(16) -> 00010000(2)

# 3.二进制 ---> 八进制、十六进制
# 将3位的二进制转换成1位的8进制。将4位的2进制转换成1位的16进制
# 001 010 011(2) -> 123(8)
# 0001 0010 0011 -> 123(16)

# 4.十进制 -> 二进制
# 相除取余法


# python对进制的支持
# python支持整数的二进制、八进制、十六进制。

# 1.python中二进制、八进制、十六进制数的表示
# 二进制：0b
print(0b11 + 10)
print(11+10)

print(bin(20))  # 将其他的数据转换成二进制 bin()
print(bin(0x20))


# 八进制:0o
print(0o11)

print(oct(20))  # 将其他的数据转换成八进制 oct()
print(oct(0b11011))


# 十六进制：0x
print(0xaf)
print(hex(20)) # 将其他的数据转换成十六进制  hex()














