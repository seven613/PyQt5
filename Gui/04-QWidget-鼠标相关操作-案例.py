# -*- coding: utf-8 -*- 
"""
Project: PyQt5
Creator: zhangqiang
Create time: 2019-11-04 14:51
IDE: PyCharm
Introduction:
"""
import sys
from PyQt5.Qt import *


class MyWindow(QWidget):
    def mouseMoveEvent(self, mv):
        print("鼠标移动了", mv.localPos())
        label = self.findChild(QLabel)
        label.move(mv.localPos().x(), mv.localPos().y())


app = QApplication(sys.argv)
window = MyWindow()
window.setWindowTitle("鼠标操作案例")
window.resize(500, 500)
window.setMouseTracking(True)

label = QLabel(window)
label.setText("鼠标操作案例")
label.move(100, 100)
label.setStyleSheet('background-color:cyan;')

window.show()

sys.exit(app.exec_())
