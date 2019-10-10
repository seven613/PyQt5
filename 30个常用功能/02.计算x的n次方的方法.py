'''
计算 x的n次方的方法
'''

def power(x,n):
    s =1
    while n > 0:
        n = n -1
        s = s * x
    return s

