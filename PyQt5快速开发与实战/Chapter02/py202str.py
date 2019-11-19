#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2019/11/14 2:17 下午
@Author:  zhangqiang
@File: py202str.py
@Software: PyCharm
@Title:字符串
"""
dss = 'hellopyqt5'
print('dss', dss)

# 1
print('\n#1')
s2 = dss[1:];
print('s2,', s2)
s3 = dss[1:3];
print('s3,', s3)
s4 = dss[:3];
print('s4,', s4)
# 2
print('\n#2')
s2 = dss[1];
print('s2,', s2)
s3 = dss[1:2];
print('s3,', s3)
dn = len(dss);
print('dn,', dn)
# 3
print('\n#3')
print('s2+s3,', s2 + s3)
print('s3*2,', s3 * 2)
