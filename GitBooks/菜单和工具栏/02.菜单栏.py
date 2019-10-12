#!/usr/bin/python3
#-*- coding:utf-8 -*-
"""
PyQt5 教程

菜单栏

by 张强 2019.10.1
"""
import sys,os
from PyQt5.QtWidgets import QMainWindow,QApplication,QAction,qApp
from PyQt5.QtGui import QIcon

print(os.getcwd())
class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        if sys.platform =='win32':
            exitAct = QAction(QIcon('exit.png'), '&Exit', self)
        else:
            exitAct = QAction(QIcon('/Users/zhangqiang/PycharmProjects/PyQt5/菜单和工具栏/exit.png'),'&Exit',self)

        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(qApp.quit)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAct)

        self.setGeometry(300,300,300,200)
        self.setWindowTitle('简单菜单')
        self.show()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    exe = Example()
    sys.exit(app.exec_())