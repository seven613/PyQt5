# -*- coding: utf-8 -*- 
"""
Project: PyQt5
Creator: zhangqiang
Create time: 2019-11-04 13:57
IDE: PyCharm
Introduction:
"""
import sys
from PyQt5.Qt import *

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("鼠标相关操作")
window.resize(500,500)

window.setCursor(Qt.BusyCursor)

window.show()

sys.exit(app.exec_())