# -*- coding: utf-8 -*- 
"""
项目: PyQt5
作者: 张强
创建时间: 2019-11-19 15:44
IDE: PyCharm
介绍:
"""
import sys
from PyQt5.Qt import *
import qdarkgraystyle
app = QApplication(sys.argv)
#window = QWidget()
window = QMainWindow()
#懒加载
#用到的时候才会创建
window.statusBar()

window.setWindowTitle("信息提示")
window.resize(500,500)
window.setWindowFlags(Qt.WindowContextHelpButtonHint)

#当鼠标停留在窗口控件身上之后，在状态栏提示一段文本
window.setStatusTip("这是窗口")

label = QLabel(window)
label.setText("标签控件")
label.setStatusTip("这是标签")
label.setToolTip("这是一个提示标签")

label.setToolTipDuration(2000)

label.setWhatsThis("这是啥？这是标签")



window.setStyleSheet(qdarkgraystyle.load_stylesheet())
window.show()

sys.exit(app.exec_())