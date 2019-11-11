# -*- coding: utf-8 -*-
"""
Project: PyQt5
Creator: zhangqiang
Create time: 2019-11-04 15:11
IDE: PyCharm
Introduction:
"""

import sys
from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("事件消息学习")
        self.resize(500, 500)
        self.setui()

    def setui(self):
        pass

    def showEvent(self, QShowEvent):
        print("窗口显示")

    def closeEvent(self, QCloseEvent):
        print("窗口关闭")

    def moveEvent(self, QMoveEvent):
        print("窗口移动了")

    def resizeEvent(self, QResizeEvent):
        print("窗口调整大小了")

    def enterEvent(self, QEvent):
        print("鼠标进入了")

    def leaveEvent(self, QEvent):
        print("鼠标离开了")

    def mousePressEvent(self, QMouseEvent):
        print("鼠标被按下")

    def mouseReleaseEvent(self, QMouseEvent):
        print("鼠标被释放了")

    def mouseDoubleClickEvent(self, QMouseEvent):
        print("鼠标双击")

    def mouseMoveEvent(self, QMouseEvent):
        print("鼠标移动")

    def keyPressEvent(self, QKeyEvent):
        print("键盘上某个按键被按下")
    def keyReleaseEvent(self, QKeyEvent):
        print("键盘上某个按键被释放")

    def focusInEvent(self, QFocusEvent):
        print("焦点获取了")
    def focusOutEvent(self, QFocusEvent):
        print("失去焦点了")



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
