# -*- coding: utf-8 -*- 
"""
Project: PyQt5
Creator: zhangqiang
Create time: 2019-11-08 15:41
IDE: PyCharm
Introduction:
"""
import sys
from PyQt5.Qt import *
import qdarkgraystyle
app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("父子关系")
window.resize(500,500)

label1 =QLabel(window)
label1.setText('标签1')

label2 =QLabel(window)
label2.setText('标签2')

label3 =QLabel(window)
label3.setText('标签3')


label2.move(50,50)
label3.move(100,100)

print(window.childAt(55, 55))#区间内的控件有谁
print(label2.parentWidget())#某个控件的父控件是谁
print(window.childrenRect())#子控件组成的区间


app.setStyleSheet(qdarkgraystyle.load_stylesheet())
window.show()

sys.exit(app.exec_())