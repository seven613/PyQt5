#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2019/11/23 11:13 上午
@Author:  zhangqiang
@File: py207ctrl.py
@Software: PyCharm
@Title:控制语句
"""
# 1
print('\n1,if')
x, y, z = 10, 20, 5
if x > y:
    print('x＞y')
else:
    print('x＜y')
# 2
print('\n#2,elif')
x, y, z = 10, 20, 5
if x > y:
    print('x＞y')
elif x > z:
    print('x＞z')

# 3
print('\n#3,while')
x = 3
while x > 0:
    print(x)

#4
print('\n#4,for')
xlst=['1','b','xxx']
for x in xlst:
    print(x)
#5
print('\n#5,for')
for x in range(3):
    print(x)
