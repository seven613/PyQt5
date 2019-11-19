#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2019/11/14 1:52 下午
@Author:  zhangqiang
@File: qt102_PrintApi.py
@Software: PyCharm
"""
import sys
from PyQt5.QtWidgets import QWidget, QTableWidget

out = sys.stdout
sys.stdout = open(r'/Users/zhangqiang/PycharmProjects/PyQt5/PyQt5快速开发与实战/Chapter01/QWidget.txt', 'w')
help(QTableWidget)
sys.stdout.close()
sys.stdout = out
