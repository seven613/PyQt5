#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2019/11/23 3:14 下午
@Author:  zhangqiang
@File: py213property01.py
@Software: PyCharm
@Title:类的动态属性
"""


class MyClass(object):

    def __init__(self):
        self._param = None

    def getParam(self):
        print("getparam:%s" % self._param)
        return self._param

    def setParam(self, value):
        print("setparam:%s" % self._param)
        self._param = value

    def delParam(self):
        print("delparam:%s" % self._param)
        del self._param

    param = property(getParam, setParam, delParam)


if __name__ == "__main__":
    cls = MyClass()
    cls.param = 10
    print("currentparam:%s" % cls.param)
    del cls.param
