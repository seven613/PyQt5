#!/usr/bin/python3
#-*- coding:utf-8 -*-
"""
PyQt5 教程

带图标的窗口
by 张强 2019.9.26
"""
import sys
from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QFile

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300,300,300,220)
        self.setWindowTitle("带图标的简单窗口")
        #windows下能正常显示，mac下不能显示图标
        #self.setWindowIcon(QIcon('/Users/zhangqiang/PycharmProjects/PyQt5/HelloWorld/home.png'))

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    path = "/Users/zhangqiang/PycharmProjects/PyQt5/HelloWorld/home.png"
    print(QFile.exists(path))
    app.setWindowIcon(QIcon(path))#mac 下的程序图标是在程序坞中，切记
    ex = Example()
    sys.exit(app.exec_())


