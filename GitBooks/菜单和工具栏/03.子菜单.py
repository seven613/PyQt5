
#!/usr/bin/python3
#-*- coding:utf-8 -*-
"""
PyQt5 教程

子菜单

by 张强 2019.9.26
"""
import sys
from PyQt5.QtWidgets import QMainWindow,QAction,QMenu,QApplication

class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('File')

        impMenu = QMenu('Import',self)
        impAct = QAction('Import mail',self)
        impMenu.addAction(impAct)

        newAct = QAction('New',self)

        fileMenu.addAction(newAct)
        fileMenu.addMenu(impMenu)

        self.setGeometry(300,300,300,200)
        self.setWindowTitle('子菜单')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())