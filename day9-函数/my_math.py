"""__author__ = 唐宏进 """

def sum1(*num):
    my_sum = 0
    for x in num:
       my_sum +=  x
    return my_sum

def sum_add(n):
    my_sum = 0
    for x in range(1,n+1):
        my_sum += x
    return my_sum

def sum_mul(n):
    my_sum = 1
    for x in range(1,n+1):
        my_sum *= x
    return my_sum

def fibo(n):
    if n == 1 or n == 2:
        return 1
    return fibo(n-2)+fibo(n-1)
