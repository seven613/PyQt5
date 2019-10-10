'''
计算a*a + b*b + c*c +...
'''

def cacl(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n*n
    return sum