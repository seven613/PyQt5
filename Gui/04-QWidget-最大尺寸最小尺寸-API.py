# -*- coding: utf-8 -*- 
"""
Project: PyQt5
Creator: zhangqiang
Create time: 2019-10-31 09:04
IDE: PyCharm
Introduction:
"""
import sys
from PyQt5.Qt import *

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("窗口最大尺寸最小尺寸修改")
# window.resize(500,500)#可以随意拖动大小
# window.setFixedSize(500,500)#就这么大，不能拖动大小
# window.setMinimumSize(200, 200)  # 可以往小拖动，但是只能到200,200,最大只能是屏幕大小，也可以单独限定宽、高
# window.setMaximumSize(800, 800)  # 可以往大拖动，但是只能到800,800，也可以单独限定宽、高

window.show()

sys.exit(app.exec_())
