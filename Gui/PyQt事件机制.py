# -*- coding: utf-8 -*- 
"""
Project: PyQt5
Creator: zhangqiang
Create time: 2019-10-24 15:53
IDE: PyCharm
Introduction:
"""

import sys
from PyQt5.Qt import *

class App(QApplication):
    def notify(self, recevier, evt):
        if recevier.inherits("QPushButton") and evt.type() ==QEvent.MouseButtonPress:
            print(recevier,evt)
        else:
            return super().notify(recevier,evt)

class Btn(QPushButton):
    def event(self, evt):
        if evt.type() ==QEvent.MouseButtonPress:
            print(evt)

        return super().event(evt)



app = App(sys.argv)

window = QWidget()

btn = QPushButton(window)
btn.setText('按钮')
btn.move(100,100)
def cao():
    print("按钮被点击了")
btn.pressed.connect(cao)


window.show()

sys.exit(app.exec_())