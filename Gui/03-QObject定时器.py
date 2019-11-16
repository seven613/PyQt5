# -*- coding: utf-8 -*- 
"""
Project: PyQt5
Creator: zhangqiang
Create time: 2019-10-24 16:47
IDE: PyCharm
Introduction:
"""

import sys
from PyQt5.Qt import *


class MyObj(QObject):
    def timerEvent(self, evt):
        print(evt, 1)


class MyLable(QLabel):

    def __init__(self, *args, **kwargs):
        super(MyLable, self).__init__(*args, **kwargs)#继承父类构造方法
        self.setText('10')#定义了一个标签
        self.move(100, 100)#移动到固定位置
        self.setStyleSheet('font-size:22px;')#设置标签样式
        self.timer_id = self.startTimer(1000)#启动一个定时器

    def timerEvent(self, *args, **kwargs):#实现定时器方法
        # 1.获取当前标签的内容
        current_sec = int(self.text())#获取标签当前文本，并且数字化
        current_sec -= 1#定时器主要任务 自动减1
        self.setText(str(current_sec))#显示到标签
        if current_sec == 0:#数字减到0时
            self.killTimer(self.timer_id)#停止定时器


class MyWidget(QWidget):

    def timerEvent(self, *args, **kwargs):  # 定时器启动任务事件
        self.resize(self.width() + 10, self.height() + 10)  # 窗口自动变大


app = QApplication(sys.argv)
window = MyWidget()
window.setWindowTitle("定时器的学习")
window.resize(500, 500)

# obj =MyObj()
# timer_id =obj.startTimer(1000)
#
# obj.killTimer(timer_id)
label = MyLable(window)
# window.startTimer(100)
window.show()

sys.exit(app.exec_())
