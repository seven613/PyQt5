#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2019/12/2 6:28 下午
@Author:  zhangqiang
@File: py213property02.py
@Software: PyCharm
@Title:类的动态属性
"""


class MyClass(object):
    def __init__(self):
        self._param = None

    @property
    def param(self):
        print("get param :%s" % self._param)
        return self._param

    @param.setter
    def param(self, value):
        print("set param :%s" % self._param)
        self._param = value

    @param.deleter
    def param(self):
        print("del param :%s" % self._param)
        del self._param


if __name__ == '__main__':
    cls = MyClass()
    cls.param = 10
    print("当前对象：%s" % cls.param)
    del cls
