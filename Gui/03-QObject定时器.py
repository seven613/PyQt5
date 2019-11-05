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
        print(evt,1)


class MyLable(QLabel):

    def __init__(self,*args,**kwargs):
        super(MyLable, self).__init__(*args,**kwargs)
        self.setText('10')
        self.move(100, 100)
        self.setStyleSheet('font-size:22px;')
        self.timer_id = self.startTimer(1000)

    def timerEvent(self, *args, **kwargs):
        #1.获取当前标签的内容
        current_sec = int(self.text())
        current_sec -= 1
        self.setText(str(current_sec))
        if current_sec == 0:
            self.killTimer(self.timer_id)

class MyWidget(QWidget):
    def timerEvent(self, *args, **kwargs):

        self.resize(self.width()+10,self.height()+10)

app = QApplication(sys.argv)
window = MyWidget()
window.setWindowTitle("定时器的学习")
window.resize(500,500)

# obj =MyObj()
# timer_id =obj.startTimer(1000)
#
# obj.killTimer(timer_id)
#label = MyLable(window)
window.startTimer(100)
window.show()

sys.exit(app.exec_())