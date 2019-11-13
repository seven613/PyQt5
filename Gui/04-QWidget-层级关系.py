# -*- coding: utf-8 -*- 
"""
Project: PyQt5
Creator: zhangqiang
Create time: 2019-11-08 15:51
IDE: PyCharm
Introduction:
"""
import sys
from PyQt5.Qt import *
import qdarkgraystyle


class Label(QLabel):
    def mousePressEvent(self, QMouseEvent):
        self.raise_()

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("控件层级关系")
window.resize(500,500)

label = Label(window)
label.setText('标签1')
label.resize(200,200)
label.setStyleSheet('background-color:red;')

label2 = Label(window)
label2.setText('标签2')
label2.resize(200,200)
label2.setStyleSheet('background-color:green;')

label2.move(100,100)

label2.lower()#降低标签2显示图层
label.raise_()#提上标签1的显示图层

label2.stackUnder(label)#标签2放在标签1下面
window.setStyleSheet(qdarkgraystyle.load_stylesheet())
window.show()

sys.exit(app.exec_())