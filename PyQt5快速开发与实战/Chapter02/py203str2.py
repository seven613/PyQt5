#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2019/11/14 2:21 下午
@Author:  zhangqiang
@File: py203str2.py
@Software: PyCharm
@Title:字符串
"""
# 1
dss = ' hellopyqt5,,'
print('\n#1,去空格和特殊自负')
s1 = dss.strip().lstrip('').rstrip(',')
print('s1', s1)
print('dss', dss)

# 2
print('\n#2,字符串连接')
s2 = dss.join(['a', '.', 'c'])
print('s2', s2)
s3 = 's3'
s3 += 'xx'
print('s3', s3)
# 3
print('\n#3,查找字符')
css = 'abc1c2c3'
pi = css.find('c')
print('pi', pi)
# 4
print('\n#4 字符串比较')
print(s1 > s2)
print(s1 == s2)
print(s1 < s2)
# 5
print('\n#5 字符串长度')
s1, s2 = 'abc', 'c123'
print('len(s1),', len(s1))
print('len(s2),', len(s2))
# 6
print('\n#6 大小写转换')
s1, s2 = 'abc', 'ABC123efg'
print('大写，s1.upper()', s1.upper())
print('小写,s2.lower()', s2.lower())
print('大小写互换,s2.swapcase()', s2.swapcase())
print('首字母大写,s1.capitalize()', s1.capitalize())
#7
print('\n#7 分割字符串')
s2 =' hello,ziwang,com,,'
print('分割字符串,s2.split',s2.split(','))
