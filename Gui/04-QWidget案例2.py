# -*- coding: utf-8 -*- 
"""
Project: PyQt5
Creator: zhangqiang
Create time: 2019-10-29 14:19
IDE: PyCharm
Introduction:
"""
import sys
from PyQt5.Qt import *

app = QApplication(sys.argv)

window = QWidget()

window.show()
window.resize(500,500)
window.move(300,300)

#总的控件个数
widget_count = 20
#一行有多少列
column_count = 3
#计算一个控件的宽度
widget_width = window.width() / column_count #放在这里是为了效率，只运行一次就可以了，放在循环里就太耗内存了
#总共有多少行
row_count = (widget_count - 1) // column_count + 1
#计算一个控件的高度
widget_height = window.height() / row_count

for i in range(0,widget_count):
    w = QWidget(window)
    w.resize(widget_width, widget_height)
    widget_x = i % column_count * widget_width
    widget_y = i // column_count * widget_height
    w.move(widget_x,widget_y)
    w.setStyleSheet("background-color:red;border:1px solid yellow;")
    w.show()  # 父控件已经显示出来了，子控件还需显示

# w = QWidget(window)
# w.resize(100,100)
# w.setStyleSheet("background-color:red;")
# w.show()#父控件已经显示出来了，子控件还需显示

sys.exit(app.exec_())