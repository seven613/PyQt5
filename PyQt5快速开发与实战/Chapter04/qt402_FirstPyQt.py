#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2019/12/3 8:31 下午
@Author:  zhangqiang
@File: qt402_FirstPyQt.py
@Software: PyCharm
@Title:
"""
import sys
from PyQt5.QtWidgets import QApplication,QWidget

app = QApplication(sys.argv)
window = QWidget()
window.resize(300,300)
window.setWindowTitle("sfas ")
window.show()
sys.exit(app.exec_())