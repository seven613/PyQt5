# -*- coding: utf-8 -*- 
"""
项目: PyQt5
作者: 张强
创建时间: 2019-11-19 16:20
IDE: PyCharm
介绍:
"""
import sys
from PyQt5.Qt import *
import qdarkgraystyle

class Window(QWidget):
    def mousePressEvent(self, QMouseEvent):
        # print(self.focusWidget())
        self.focusNextChild()#下一个
        self.focusPreviousChild()#上一个
        self.focusNextPrevChild(True)#True：下一个;False 上一个


app = QApplication(sys.argv)
window = Window()
window.setWindowTitle("焦点控制")
window.resize(500,500)

lineEdit = QLineEdit(window)
lineEdit.move(50,50)

lineEdit2 = QLineEdit(window)
lineEdit2.move(50,100)

lineEdit3 = QLineEdit(window)
lineEdit3.move(50,150)

QWidget.setTabOrder(lineEdit,lineEdit3)
QWidget.setTabOrder(lineEdit3,lineEdit2)
#lineEdit3.setFocus()

#获取当前窗口内部所有子控件当中获得焦点的控件
#print(window.focusWidget())

window.setStyleSheet(qdarkgraystyle.load_stylesheet())
window.show()

sys.exit(app.exec_())