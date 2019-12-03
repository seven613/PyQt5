#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2019/12/3 8:35 下午
@Author:  zhangqiang
@File: qt404_QToolTip.py
@Software: PyCharm
@Title:
"""
import sys
from PyQt5.QtWidgets import QApplication, QToolTip, QWidget
from PyQt5.QtGui import QFont


class WinForm(QWidget):
    def __init__(self):
        super(WinForm, self).__init__()
        self.initUi()

    def initUi(self):
        QToolTip.setFont(QFont('SansSerif', 20))
        self.setToolTip("这是一个<b>气泡提示</b>")
        self.setGeometry(200, 300, 400, 400)
        self.setWindowTitle("气泡提示")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    winForm = WinForm()
    winForm.show()
    sys.exit(app.exec_())
