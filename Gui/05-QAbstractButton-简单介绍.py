# -*- coding: utf-8 -*- 
"""
项目: PyQt5
作者: 张强
创建时间: 2019-11-20 11:13
IDE: PyCharm
介绍:
"""
import sys
from PyQt5.Qt import *
import qdarkgraystyle
class Btn(QAbstractButton):
    def paintEvent(self, evt):
        print("绘制按钮")

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("QAbstractButton")
window.resize(500,500)

btn =Btn(window)
btn.setText("xxx")

window.setStyleSheet(qdarkgraystyle.load_stylesheet())
window.show()

sys.exit(app.exec_())