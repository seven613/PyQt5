#!/usr/bin/python3
#-*- coding:utf-8 -*-
"""
PyQt5 教程

消息盒子
by 张强 2019.9.26
"""

import sys
from PyQt5.QtWidgets import QApplication,QWidget,QMessageBox

class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300,300,300,200)
        self.setWindowTitle("消息盒子")
        self.show()
    def closeEvent(self, event):
        reply=QMessageBox.question(self,"提示","确定退出吗？",QMessageBox.Yes|QMessageBox.No,QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
