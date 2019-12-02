#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2019/12/2 8:20 下午
@Author:  zhangqiang
@File: CallContainerswin.py
@Software: PyCharm
@Title:
"""
import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
from ContainersWin import Ui_MainWindow

class MyContainersWin(QMainWindow,Ui_MainWindow):
    def __init__(self,parent= None ):
        super(MyContainersWin, self).__init__(parent)
        self.setupUi(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myContainer = MyContainersWin()
    myContainer.show()
    sys.exit(app.exec_())