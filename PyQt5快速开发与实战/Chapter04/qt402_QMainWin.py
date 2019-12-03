#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2019/12/3 7:48 下午
@Author:  zhangqiang
@File: qt402_QMainWin.py
@Software: PyCharm
@Title:
"""
import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5.QtGui import QIcon

class MainWin(QMainWindow):
    def __init__(self,parent =None):
        super(MainWin, self).__init__(parent)
        self.resize(400,200)
        self.status=self.statusBar()
        self.status.showMessage("这是状态栏提示",5000)
        self.setWindowTitle("PyQt5 MainWindow 例子")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('/Users/zhangqiang/PycharmProjects/PyQt5/PyQt5快速开发与实战/Chapter04/images/window.ico'))
    mainWin = MainWin()
    mainWin.show()
    sys.exit(app.exec_())