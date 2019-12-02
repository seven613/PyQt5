#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2019/12/2 9:13 下午
@Author:  zhangqiang
@File: CallMainWinSignalSlog03.py
@Software: PyCharm
@Title:
"""

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from MainWinSignalSlog03 import Ui_MainWindow


class MyMainWin(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainWin, self).__init__(parent)
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyMainWin()
    myWin.show()
    sys.exit(app.exec_())
