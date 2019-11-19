# -*- coding: utf-8 -*- 
"""
项目: PyQt5
作者: 张强
创建时间: 2019-11-18 11:26
IDE: PyCharm
介绍:
"""
import sys
from PyQt5.Qt import *
import qdarkgraystyle

class Window(QWidget):
    def __init__(self,*args,**kwargs):
        super(Window, self).__init__(*args,**kwargs)
        self.setWindowFlags(Qt.FramelessWindowHint)  # 窗口无标题栏
        self.setWindowOpacity(1)  # 窗口半透明 0 完全透明，1 不透明
        self.setWindowTitle("顶层窗口操作-案例")
        self.resize(500, 500)

        self.top_margin = 10
        self.btn_width = 80
        self.btn_height = 40

        self.setup_ui()
    def setup_ui(self):
        #公共数据

        close_btn = QPushButton(self)
        self.close_btn = close_btn
        close_btn.setText("关闭")
        close_btn.resize(self.btn_width, self.btn_height)


        max_btn = QPushButton(self)
        self.max_btn = max_btn
        max_btn.setText("最大化")
        max_btn.resize(self.btn_width, self.btn_height)


        min_btn = QPushButton(self)
        self.min_btn = min_btn
        min_btn.setText("最小化")
        min_btn.resize(self.btn_width, self.btn_height)


        def max_normal():
            if self.isMaximized():
                self.showNormal()
                max_btn.setText("最大化")
            else:
                self.showMaximized()
                max_btn.setText("恢复")

        close_btn.pressed.connect(self.close)
        max_btn.pressed.connect(max_normal)
        min_btn.pressed.connect(self.showMinimized)

    def resizeEvent(self, QResizeEvent):#窗口尺寸变化事件

        window_w = self.width()
        close_btn_x = window_w - self.btn_width
        close_btn_y = self.top_margin
        self.close_btn.move(close_btn_x, close_btn_y)

        max_btn_x = close_btn_x - self.btn_width
        max_btn_y = self.top_margin
        self.max_btn.move(max_btn_x, max_btn_y)

        min_btn_x = max_btn_x - self.btn_width
        min_btn_y = self.top_margin
        self.min_btn.move(min_btn_x, min_btn_y)

    def mousePressEvent(self, QMouseEvent):
        #定义一个状态，监听是不是已经按下了鼠标
        #判断按下的是不是鼠标左键
        #记录窗口当前的坐标
        #记录鼠标点击的当前坐标
        #计算出差值
        pass
    def mouseMoveEvent(self, QMouseEvent):
        #判定鼠标状态是不是为真，如果是则执行
        #记录鼠标移动后的坐标
        #用鼠标移动后的坐标 - 移动前的坐标 = 移动向量
        #窗口移动到窗口原始坐标+移动向量

        pass
    def mouseReleaseEvent(self, QMouseEvent):
        #鼠标状态设置为甲
        pass


app = QApplication(sys.argv)
# window = QWidget(flags=Qt.FramelessWindowHint)#窗口无标题栏
window = Window()
# window.setWindowFlags(Qt.FramelessWindowHint)  # 窗口无标题栏
#
# window.setWindowOpacity(1)  # 窗口半透明 0 完全透明，1 不透明
#
# window.setWindowTitle("顶层窗口操作-案例")
# window.resize(500, 500)
#
# top_margin = 10
# btn_width = 80
# btn_height = 40
# # 添加3个子控件-窗口右上角
# close_btn = QPushButton(window)
# close_btn.setText("关闭")
# close_btn.resize(btn_width,btn_height)
# window_w = window.width()
# close_btn_x =  window_w - btn_width
# close_btn_y = top_margin
# close_btn.move(close_btn_x,close_btn_y)
#
# max_btn = QPushButton(window)
# max_btn.setText("最大化")
# max_btn.resize(btn_width,btn_height)
# max_btn_x = close_btn_x - btn_width
# max_btn_y = top_margin
# max_btn.move(max_btn_x,max_btn_y)
#
# min_btn = QPushButton(window)
# min_btn.setText("最小化")
# min_btn.resize(btn_width,btn_height)
# min_btn_x = max_btn_x - btn_width
# min_btn_y = top_margin
# min_btn.move(min_btn_x,min_btn_y)
#
# # def close():
# #     window.close()
# # close_btn.pressed.connect(close)
#
# def max_normal():
#     if window.isMaximized():
#         window.showNormal()
#         max_btn.setText("最大化")
#     else:
#         window.showMaximized()
#         max_btn.setText("恢复")
#
# close_btn.pressed.connect(window.close)
# max_btn.pressed.connect(max_normal)
# min_btn.pressed.connect(window.showMinimized)




#window.setStyleSheet(qdarkgraystyle.load_stylesheet())
window.show()

sys.exit(app.exec_())
