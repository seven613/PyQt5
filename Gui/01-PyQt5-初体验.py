#-*-coding:utf-8 -*-
"""..."""
__author__ = '张强'

from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("社会我顺哥，人很话不多")
window.resize(500,500)
window.move(400,200)

label = QLabel(window)
label.setText("Hello World!")
label.move(200,50)

window.show()

sys.exit(app.exec_())