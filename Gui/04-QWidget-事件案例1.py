# -*- coding: utf-8 -*- 
"""
Project: PyQt5
Creator: zhangqiang
Create time: 2019-11-05 09:43
IDE: PyCharm
Introduction:
"""
import sys
from PyQt5.Qt import *


class MyLabel(QLabel):

    def enterEvent(self, *args, **kwargs):  # 鼠标进入控件事件重写
        print("鼠标进入")
        self.setText("欢迎光临")

    def leaveEvent(self, *args, **kwargs):  # 鼠标离开控件事件重写
        print("鼠标离开了")
        self.setText("谢谢惠顾")


app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("鼠标操作案例1")
window.resize(500, 500)

label = MyLabel(window)  # 继承控件父类

label.resize(200, 200)
label.move(100, 100)
label.setStyleSheet('background-color:cyan;')

window.show()

sys.exit(app.exec_())
