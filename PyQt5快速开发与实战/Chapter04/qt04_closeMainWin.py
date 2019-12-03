#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2019/12/3 8:14 下午
@Author:  zhangqiang
@File: qt04_closeMainWin.py
@Software: PyCharm
@Title:
"""
import sys
from PyQt5.QtWidgets import QApplication,QWidget,QMainWindow,QPushButton,QHBoxLayout,qApp

class WinForm(QMainWindow):
    def __init__(self,parent = None):
        super(WinForm, self).__init__(parent)
        self.setWindowTitle("关闭主窗口")
        self.resize(500,300)

        self.pushButton = QPushButton("关闭主窗口")
        self.pushButton.clicked.connect(self.onButtonClick)

        layout = QHBoxLayout()
        layout.addWidget(self.pushButton)

        main_frame = QWidget()
        main_frame.setLayout(layout)
        self.setCentralWidget(main_frame)

    def onButtonClick(self):
        sender = self.sender()
        print(sender.text()+" 被按下了")
        qApp = QApplication.instance()
        qApp.quit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    winForm = WinForm()
    winForm.show()
    sys.exit(app.exec_())
