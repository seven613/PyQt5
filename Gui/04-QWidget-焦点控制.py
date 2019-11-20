# -*- coding: utf-8 -*- 
"""
项目: PyQt5
作者: 张强
创建时间: 2019-11-19 16:20
IDE: PyCharm
介绍:
"""
import sys
from PyQt5.Qt import *
import qdarkgraystyle
app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("焦点控制")
window.resize(500,500)

lineEdit = QLineEdit(window)
lineEdit.move(50,50)

lineEdit2 = QLineEdit(window)
lineEdit2.move(50,100)

lineEdit3 = QLineEdit(window)
lineEdit3.move(50,150)

lineEdit3.setFocus()

window.setStyleSheet(qdarkgraystyle.load_stylesheet())
window.show()

sys.exit(app.exec_())