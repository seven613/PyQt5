#-*-coding:utf-8 -*-
"""..."""
__author__ = '张强'

import sys
from PyQt5.Qt import * #主要包含了我们常用的一些类，汇总到了一块
from Menu import Window
# class Window(QWidget):
#     def __init__(self):
#         super().__init__()
#
#         self.setWindowTitle("类")
#         self.resize(500,500)
#         self.setup_ui()
#
#     def setup_ui(self):
#         label = QLabel(self)
#         label.setText("XXX")

#1.创建一个应用对象
app = QApplication(sys.argv)

#2.控件的操作
#创建控件，设置大小、位置、样式，事件，信号的处理
#2.1创建控件
window = Window()

window.show()


#3.应用程序的执行，进入到消息循环
sys.exit(app.exec_())

