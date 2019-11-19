#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2019/11/15 9:21 上午
@Author:  zhangqiang
@File: py205tuple.py
@Software: PyCharm
@Title:元组 tuple
"""
# 1
print('\n#1')
zlst = ('hello', 'PyQt5', '.', 'com')
vlst = ('Top', 'Quant', '.', 'vip')
print('zlst,', zlst)
print('vlst,', vlst)
# 2
print('\n#2')
s2 = zlst[1:]
print('s2,', s2)
s3 = zlst[1:3]
print('s3,', s3)
s4 = vlst[:3]
print('s4,', s4)
# 3
print('\n#3')
print('s2+s3,', s2 + s3)
print('s3*2,', s3 * 2)
