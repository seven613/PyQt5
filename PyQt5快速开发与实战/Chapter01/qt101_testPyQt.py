#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2019/11/14 8:06 上午
@Author:  zhangqiang
@File: qt101_testPyQt.py
@Software: PyCharm
"""
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget

app = QtWidgets.QApplication(sys.argv)

widget= QtWidgets.QWidget()
widget.resize(360,360)
widget.setWindowTitle("Hello PyQt5")

widget.show()

sys.exit(app.exec_())