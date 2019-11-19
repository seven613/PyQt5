# -*- coding: utf-8 -*- 
"""
项目: PyQt5
作者: 张强
创建时间: 2019-11-19 09:02
IDE: PyCharm
介绍:
"""
import sys
from PyQt5.Qt import *
import qdarkgraystyle
app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("交互状态")
window.resize(500,500)

btn = QPushButton(window)
btn.setText("按钮")
btn.setEnabled(False)#设置按钮不可用
btn.pressed.connect(lambda :print("按钮被点击了"))


window.setStyleSheet(qdarkgraystyle.load_stylesheet())
window.show()

sys.exit(app.exec_())