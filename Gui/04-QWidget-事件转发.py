# -*- coding: utf-8 -*- 
"""
Project: PyQt5
Creator: zhangqiang
Create time: 2019-11-05 08:56
IDE: PyCharm
Introduction:
"""
import sys
from PyQt5.Qt import *

class Window(QWidget):
    def mousePressEvent(self, QMouseEvent):
        print("顶层窗口鼠标按下")

class MidWindow(QWidget):
    pass

    #不处理这个事件，点击时时间将被转移到父控件对应的事件，Window的mousePressEvent
    # def mousePressEvent(self, QMouseEvent):
    #     print("中间控件被按下")

class Label(QLabel):
    pass
    #QLabel本身并没有处理这个事件，所以才会传入父控件。
    #不处理这个事件，点击时时间将被转移到父控件对应的事件，MidWindow的mousePressEvent
    # def mousePressEvent(self, QMouseEvent):
    #     print("标签控件被按下")

class Button(QPushButton):
    def mousePressEvent(self, *args, **kwargs):
        print("按钮被按下")

app = QApplication(sys.argv)
window = Window()
window.setWindowTitle("事件转发")
window.resize(500,500)

mid_window = MidWindow(window)
mid_window.resize(300,300)
mid_window.setAttribute(Qt.WA_StyledBackground,True)
mid_window.setStyleSheet('background-color:yellow;')

#label = Label(mid_window)
label = QLabel(mid_window)
label.setText("控件")
label.move(100,100)
label.setStyleSheet("background-color:red;")

btn = QPushButton(mid_window)
btn.setText("我是按钮")
btn.move(50,100)


window.show()

sys.exit(app.exec_())