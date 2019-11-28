#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2019/11/23 2:56 下午
@Author:  zhangqiang
@File: py211class.py
@Software: PyCharm
@Title:class 类
"""


class MyClass:
    count = 0
    name = 'DefaultName'#类变量

    def __init__(self, name):#类构造函数，有且仅有一个，用来初始化类及其变量
        self.name = name #self.name 是类实例后的对象的变量
        print('类的变量是%s\n对象的变量是%s' % (MyClass.name, self.name))


    def setCount(self, count):
        self.count = count

    def getCount(self):
        return self.count


if __name__ == '__main__':
    cls = MyClass('test')
    cls.setCount(10)
    print('count=%d' % cls.getCount())
