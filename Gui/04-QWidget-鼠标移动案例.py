# -*- coding: utf-8 -*- 
"""
Project: PyQt5
Creator: zhangqiang
Create time: 2019-11-06 17:51
IDE: PyCharm
Introduction:
"""

import sys
from PyQt5.Qt import *
import qdarkgraystyle


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.move_flag =False #窗口移动标记,主要是判定鼠标是按下，还是一直在窗口内部移动,默认窗口不移动
        self.setWindowTitle("鼠标移动案例的学习")
        self.resize(500, 500)
        self.setui()

    def setui(self):
        btn = QPushButton(self)
        btn.setText('按钮')
        btn.move(200,200)

        label = QLabel(self)
        label.setText("标签")
        label.move(100,100)

    def mousePressEvent(self, evt):  # 鼠标按下事件
        #QMouseEvent
        if evt.button() == Qt.LeftButton:#只有鼠标左键才能移动，右键是不能移动的
            self.move_flag =True #设置为窗口移动状态
            self.mouse_x = evt.globalX() #鼠标在控件内第一次按下的x,相对于屏幕
            self.mouse_y = evt.globalY() #鼠标在控件内第一次按下的y,相对于屏幕
            print(self.mouse_x,self.mouse_y)
            self.origin_x = self.x()#窗口左上角标点在屏幕上的x位置
            self.origin_y = self.y()#窗口左上角标点在屏幕上的y位置

    def mouseMoveEvent(self, evt):  # 鼠标移动事件
        if self.move_flag:#窗口移动状态才能移动
            move_x = evt.globalX() - self.mouse_x #移动x距离，由当前的x值减去第一次按下鼠标的x值得到
            move_y = evt.globalY() - self.mouse_y #移动y距离，由当前的x值减去第一次按下鼠标的y值得到
            print(move_x,move_y)
            self.move(self.origin_x + move_x,self.origin_y + move_y) #窗口开始移动，由窗口的原始标点(x,y)+移动距离(move_x,move_y)


    def mouseReleaseEvent(self, QMouseEvent):  # 鼠标释放事件
        self.move_flag =False#释放窗口移动状态，否则鼠标释放后窗口仍然还要移动


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkgraystyle.load_stylesheet_pyqt5())
    window = Window()
    window.show()
    window.setMouseTracking(True)
    sys.exit(app.exec_())
