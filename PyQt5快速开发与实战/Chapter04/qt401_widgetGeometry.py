#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2019/12/3 8:27 下午
@Author:  zhangqiang
@File: qt401_widgetGeometry.py
@Software: PyCharm
@Title:
"""
import sys
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton

app = QApplication(sys.argv)
widget =QWidget()
btn = QPushButton(widget)
btn.setText("按钮")
btn.move(20,20)
widget.resize(300,200)
widget.move(250,200)
widget.setWindowTitle("PyQt5坐标系统例子")
widget.show()
sys.exit(app.exec_())