#!/usr/bin/python3
#-*- coding:utf-8 -*-
"""
PyQt5 教程

关闭窗口
by 张强 2019.9.26
"""
import sys
from PyQt5.QtWidgets import QApplication,QPushButton,QWidget
from PyQt5.QtCore import QCoreApplication

class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        qbtn=QPushButton("关闭",self)
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        qbtn.resize(qbt.sizeHint())
        qbtn.move(50,50)

        self.setGeometry(300,300,300,200)
        self.setWindowTitle("退出按钮")
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())