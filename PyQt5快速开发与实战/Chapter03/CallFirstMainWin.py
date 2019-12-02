#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2019/12/2 7:58 下午
@Author:  zhangqiang
@File: CallFirstMainWin.py
@Software: PyCharm
@Title:
"""
import sys
from PyQt5.QtWidgets import QApplication,QMainWindow

from firstMainWin import Ui_MainWindow
class MyMainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self,parent = None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())