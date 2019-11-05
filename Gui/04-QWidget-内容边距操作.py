# -*- coding: utf-8 -*- 
"""
Project: PyQt5
Creator: zhangqiang
Create time: 2019-10-31 10:42
IDE: PyCharm
Introduction:
"""
import sys
from PyQt5.Qt import *

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("内容边距的设定")
window.resize(500, 500)

label = QLabel(window)
label.setText("内容边距的设定")
label.resize(300, 300)
label.setStyleSheet('background-color:cyan;')

label.setContentsMargins(100,200,0,0)
print(label.contentsRect())
print(label.getContentsMargins())


window.show()

sys.exit(app.exec_())
