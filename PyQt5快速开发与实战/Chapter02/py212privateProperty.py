#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2019/11/23 3:07 下午
@Author:  zhangqiang
@File: py212privateProperty.py
@Software: PyCharm
@Title:类的私有属性、私有方法，两个短_开头，只能在类中调用
"""


class MyCounter:
    __secretCount = 0  # 私有变量
    publicCount = 0  # 公共变量

    def __privateCountFun(self):#私有方法
        print("这是私有方法")
        self.__secretCount += 1
        self.publicCount += 1

    def publicCountFun(self):
        print("这是公有方法")
        self.__privateCountFun()


if __name__ == '__main__':
    counter = MyCounter()
    counter.publicCountFun()#只能访问公有方法，私有方法访问不到
    counter.publicCountFun()
    print('instancepublicCount=%d' % counter.publicCount)
    print('ClasspublicCount=%d' % MyCounter.publicCount)
