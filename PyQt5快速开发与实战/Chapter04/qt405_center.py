#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2019/12/3 7:59 下午
@Author:  zhangqiang
@File: qt405_center.py
@Software: PyCharm
@Title:把窗口放在屏幕中间
"""
#1.创建一个窗口，设置标题和大小
#2.创建一个放置窗口中间函数
#2.1得到屏幕的大小
#2.2得到当前窗口的大小
#2.3将窗口的中间点移动到窗口中间点
#3.启动程序、
import sys
from PyQt5.QtWidgets import QApplication,QDesktopWidget,QMainWindow

class WinForm(QMainWindow):
    def __init__(self,parent = None):
        super(WinForm, self).__init__(parent)
        self.setWindowTitle("窗口放在屏幕中间")
        self.resize(300,200)
        self.center()
    def center(self):
        screen = QDesktopWidget().screenGeometry()
        print(screen)
        size = self.size()
        print(size)
        self.move((screen.width() - size.width())/2,(screen.height() - size.height())/2)
        print(self.geometry())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    winForm = WinForm()
    winForm.show()
    sys.exit(app.exec_())