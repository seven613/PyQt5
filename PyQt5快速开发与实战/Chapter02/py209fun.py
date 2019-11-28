#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2019/11/23 11:28 上午
@Author:  zhangqiang
@File: py209fun.py
@Software: PyCharm
@Title:函数partial

"""
import functools


def add(a, b):
    return a + b


# 1
print('\n#1')
rst1 = add(4, 2)
print('add(4,2)=', rst1)
plus3 = functools.partial(add, 3)  # 3 是已经知道的值，
plus5 = functools.partial(add, 5)  # 5 是已经知道值，但是add函数中的另一个参数不知道，所以可以先把5放进参数组成另一个函数。
                                    # 这样写不能提高程序效率，只是让代码看起来更简洁
# 2
print('\n#2')
rst2 = plus3(4)
print('plus3(4)=', rst2)
rst3 = plus3(7)
print('plus3(7)=', rst3)
rst4 = plus5(10)
print('plus5(10)=', rst4)
