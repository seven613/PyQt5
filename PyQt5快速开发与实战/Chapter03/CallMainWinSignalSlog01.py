#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2019/12/2 9:01 下午
@Author:  zhangqiang
@File: CallMainWinSignalSlog01.py
@Software: PyCharm
@Title:
"""
import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
from MainWinSignalSolg01 import Ui_MainWindow

class MyMainWinSignalSolg(QMainWindow,Ui_MainWindow):
    def __init__(self,parent = None):
        super(MyMainWinSignalSolg, self).__init__(parent)
        self.setupUi(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myMainWinSignalSlog = MyMainWinSignalSolg()
    myMainWinSignalSlog.show()
    sys.exit(app.exec_())