# -*- coding: utf-8 -*- 
"""
Project: PyQt5
Creator: zhangqiang
Create time: 2019-10-25 15:04
IDE: PyCharm
Introduction:
"""
import sys
from PyQt5.Qt import *

app = QApplication(sys.argv)

window = QWidget()

window.move(100,100) #往下走，改y；往右走 改x 正直；
#window.resize(500,500)#可以调整大小
window.setFixedSize(500,500)#固定大小

#window.setGeometry(0,0,150,150)#用户区域距离桌面原点的x,y值， 不包括窗口的标题栏，
label = QLabel(window)
label.setText("测试得分")
label.move(100,100)
label.setStyleSheet("background-color:red;")

def changeCao():
    new_content = label.text()+"测试得分"
    label.setText(new_content)
    label.adjustSize()#自适应大小

btn = QPushButton(window)
btn.setText("点击")
btn.move(100,300)
btn.clicked.connect(changeCao)

window.show()
#window.setGeometry(0,0,150,150) 放在这里执行的结果就是看不到标题栏，因为它是设置用户区域的位置



sys.exit(app.exec_())