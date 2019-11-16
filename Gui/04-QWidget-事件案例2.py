# -*- coding: utf-8 -*- 
"""
Project: PyQt5
Creator: zhangqiang
Create time: 2019-11-05 09:54
IDE: PyCharm
Introduction:
"""
import sys
from PyQt5.Qt import *


class MyLabel(QLabel):
    def keyReleaseEvent(self, *args, **kwargs):  # 按键释放事件重写
        pass

    def keyPressEvent(self, evt):  # 按键按下事件重写

        # print("sssss")
        # QKeyEvent
        # 普通键位
        if evt.key() == Qt.Key_Tab:  #获得按下键是否为tab键，Qt.Key_所有键
            print("是Tab键")
        # 修饰键为Ctrl 并且 普通键位s
        if evt.modifiers() == Qt.ControlModifier and evt.key() == Qt.Key_S:  # 监听Ctrl+S，组合键中ctrl alt shift都是修饰键
            print("Ctrl+S被按下了")

        if evt.modifiers() == Qt.ControlModifier | Qt.ShiftModifier and evt.key() == Qt.Key_A:  # 按位或 监听修饰键
            print("Ctrl+Shift+A被按下了")


app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("事件案例2")
window.resize(500, 500)

label = MyLabel(window)
label.resize(200, 200)
label.move(100, 100)
label.setStyleSheet('background-color:cyan;')

label.grabKeyboard()  # 监听键盘输入，否则无法知道谁在获取键盘输入

window.show()

sys.exit(app.exec_())
