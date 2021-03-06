# 1.数学运算符：+, -, *, /, //(整除), %, **(幂运算)
# a.+, -, *, /, %和数学中的加、减、乘、除、求余的功能一模一样

# b.//(整除)
# 求商，商只取整数部分
print(5//2)
print(6.3//2)

# c.**(幂运算)
# x**y -- x的y次方
print(2**3)
print(8**(1/3))

#练习： 取出一个4位整数的百位上的数。例如，取出1234中的2
num = 1234
qian = num//1000
bai = num//100%10
shi = num//10%10
ge = num%10
print(qian,bai,shi,ge)

# 2.比较运算：>(大于),<(小于),==(等于)，!=(不等于)，>=(大于等于)，<=(小于等于)
# 所有的比较运算的结果都是布尔值
print(10 > 20)
print(10 < 20)
print(10 == 20)
print(10 != 20)

# 3.逻辑运算符:and(与运算)，or(或)，not(非)
# 逻辑运算符操作的数据是布尔值，返回的结果也是布尔
# a.and(与) -- 和、并且
# 两个都是True结果才是True,只要有一个是False结果就是False
print(True and True) # Ture
print(True and False) # False
print(False and False) # False

# 要求学习成绩的绩点是3.5以上，并且操评分不低于90
score = 4.0
score2 = 80
print(score>3.5 and score2>=90)

# 什么时候使用：要求两个或者多个条件同时满足

# b.or(或) -- 或者
# 只要有一个True结果就是True。两个都是False才是False
print(score>3.5 or score2>=90)

# 什么时候使用：要求两个或者多个条件只要一个满足就行

# c.not(非)
# True变成False,False就变成True
age = 18

# 年龄不小于18
print(not age<18)
print(age >= 18)

# 4.赋值运算符：=(赋值)，+=，-=，*=，/=，%=，//=，**=
# 赋值符号的左边必须是变量；运算顺序是，先算赋值符号右边的值，然后再将右边的结果赋给左边
# a.变量 = 值
a = 10
b = 10 + 20
c = a+b  # 40
d = a > 10
print(d)

# b.变量 += 值
# 这儿的变量必须是已经声明过的变量
a += 2 # 相当于a = a + 2
print(a)

b -= 10 # b = b - 10
print(b)


# 5.运算符的优先级
# 正负>数学运算符>比较运算符>逻辑运算符>赋值运算符
# 数学运算符中：**>(*,/,%,//)>(+,-)
# 优先级高的先计算，如果优先级相同就从左往右依次计算，可以通过加括号改变计算顺序。
print(10 * 20 + 30 < 40 / 2 -100)

print(2 * 2**3)



	

