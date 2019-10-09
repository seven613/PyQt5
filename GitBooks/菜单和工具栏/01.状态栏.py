#!/usr/bin/python3
#-*- coding:utf-8 -*-
"""
PyQt5 教程

状态栏

by 张强 2019.10.1
"""
import sys
from PyQt5.QtWidgets import QApplication,QMainWindow

class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.statusBar().showMessage('Ready')

        self.setGeometry(300,300,250,150)
        self.setWindowTitle('状态栏')

        self.show()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())