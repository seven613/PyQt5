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

window.move(100, 100)  # 往下走，改y；往右走 改x 正直；
# window.resize(500,500)#可以调整大小
window.setFixedSize(500, 500)  # 固定大小

# window.setGeometry(0,0,150,150)#用户区域距离桌面原点的x,y值， 不包括窗口的标题栏，
label = QLabel(window)  # 在窗口内添加一个标签
label.setText("测试得分")  # 设置标签内容
label.move(100, 100)  # 标签放到固定位置
label.setStyleSheet("background-color:red;")  # 设置标签样式，背景色红色


def changeCao():  # 定义槽函数
    new_content = label.text() + "测试得分"
    label.setText(new_content)
    label.adjustSize()  # 自适应大小


btn = QPushButton(window)  # 窗口内放置一个按钮
btn.setText("点击")  # 设置按钮内容
btn.move(100, 300)  # 移动到固定位置
btn.clicked.connect(changeCao)  # 点击事件连接到槽函数

window.show()
# window.setGeometry(0,0,150,150) 放在这里执行的结果就是看不到标题栏，因为它是设置用户区域的位置


sys.exit(app.exec_())
