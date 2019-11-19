#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2019/11/15 9:24 上午
@Author:  zhangqiang
@File: py206dict.py
@Software: PyCharm
@Title:字典 dict k-v形式 无序
"""


'''
（1）Python字典包含以下内置函数。
●cmp(dict1,dict2)：比较两个字典元素。
●len(dict)：计算字典元素的个数，即键的总数。
●str(dict)：输出字典可打印的字符串标识。
●type(variable)：返回输入的变量类型，如果变量是字典，就返回字典类型。
（2）Python字典包含以下内置方法
●radiansdict.clear()：删除字典内所有元素。
●radiansdict.copy()：返回一个字典的浅复制。
●radiansdict.fromkeys()：创建一个新字典，以序列seq中的元素做字典的键，val为字典所有键对应的初始值。
●radiansdict.get(key,default=None)：返回指定键的值，如果值不在字典中，则返回default值。
●radiansdict.has_key(key)：如果键在字典中，则返回true；否则返回false。
●radiansdict.items()：以列表形式返回可遍历的(键,值)元组数组。
●radiansdict.key()以列表形式返回一个字典中所有的键。

'''
# 1
print('\n#1')
zdict = {}
zdict['w1'] = 'hello'
zdict['w2'] = 'ziwang.com'
print('zdict,', zdict)
# 2
print('\n#2')
vdict = {'url1': 'TopQuant.vip', 'url2': 'www.TopQuant.vip', 'url3': 'ziwang.com'}
print('vdict,', vdict)
# 3
print('\n#3')
s2 = zdict['w1']
print('s2,', s2)
s3 = vdict['url2']
print('s3,', s3)
