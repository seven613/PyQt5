#-*-coding:utf-8 -*-
"""..."""
__author__ = '张强'

from PyQt5.Qt import *

#print(QObject.__subclasses__())
#print(QWidget.__subclasses__())

#查找子类
def getSubClasses(cls):
    for subcls in cls.__subclasses__():
        print(subcls)
        if len(cls.__subclasses__()) > 0:
            getSubClasses(subcls)


getSubClasses(QWidget)