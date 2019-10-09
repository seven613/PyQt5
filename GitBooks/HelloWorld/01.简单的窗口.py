#!/usr/bin/python3
#-*- coding:utf-8 -*-
"""
PyQt5 教程

简单的窗口
by 张强 2019.9.26
"""
import sys
from PyQt5.QtWidgets import QApplication,QWidget

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = QWidget()
    window.resize(250,150)
    window.move(300,300)
    window.setWindowTitle("简单窗口")
    window.show()

    sys.exit(app.exec_())