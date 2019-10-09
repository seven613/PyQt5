#!/usr/bin/python3
#-*- coding:utf-8 -*-
"""
PyQt5 教程

提示框
by 张强 2019.9.26
"""

import sys
from PyQt5.QtWidgets import QApplication,QWidget,QToolTip,QPushButton
from PyQt5.QtGui import QFont

class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('SansSerif',10))

        btn = QPushButton('Button',self)
        btn.setToolTip('这是一个<b>QPushButton<b>')
        btn.resize(btn.sizeHint())
        btn.move(50,50)

        self.setGeometry(300,300,300,300)
        self.setWindowTitle('提示')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())