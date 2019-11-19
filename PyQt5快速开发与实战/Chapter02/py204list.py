#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2019/11/15 9:12 上午
@Author:  zhangqiang
@File: py204list.py
@Software: PyCharm
@Title:list 列表 有序序列
"""

"""
（1）列表操作包含以下函数。
●cmp(list1,list2)：比较两个列表的元素。
●len(list)：列表元素个数。
●max(list)：返回列表元素的最大值。
●min(list)：返回列表元素的最小值。
●list(seq)：将元组转换为列表。

（2）列表操作包含以下方法。
●list.append(obj)：在列表末尾添加新的对象。
●list.count(obj)：统计某个元素在列表中出现的次数。
●list.extend(seq)：在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）。
●list.index(obj)：从列表中找出某个值第一个匹配项的索引位置。
●list.insert(index,obj)：将对象插入列表中。
●list.pop(obj=list[1])：移除列表中的一个元素（默认是最后一个元素），并且返回该元素的值。
●list.remove(obj)：移除列表中某个值的第一个匹配项。
●list.reverse()：反向列表中元素。

"""
#1
print('\n#1')
zlst=['hello','PyQt5','.','com']
vlst=['Top','Quant','.','vip']
print('zlst,',zlst)
print('vlst,',vlst)
#2
print('\n#2')
s2=zlst[1:]
print('s2,',s2)
s3=zlst[1:3]
print('s3,',s3)
s4=vlst[:3]
print('s4,',s4)
#3
print('\n#3')
print('s2+s3,',s2+s3)#列表合并
print('s3*2,',s3*2)#列表重复
