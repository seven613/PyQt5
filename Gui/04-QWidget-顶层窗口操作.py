# -*- coding: utf-8 -*- 
"""
项目: PyQt5
作者: 张强
创建时间: 2019-11-11 15:51
IDE: PyCharm
介绍:
"""
import sys
from PyQt5.Qt import *
import qdarkgraystyle

app = QApplication(sys.argv)
window = QWidget(flags=Qt.FramelessWindowHint)  # 无标题栏
window.setWindowTitle("顶层窗口操作-案例")
window.setWindowOpacity(0.5)  # 窗口透明
window.resize(500, 500)

# 添加三个子控件-窗口右上角
top_margin = 10
btn_w = 80
btn_h = 40

close_btn = QPushButton(window)
close_btn.setText('关闭')
close_btn.resize(btn_w, btn_h)

window_w = window.width()
close_btn_x = window_w - btn_w
close_btn_y = top_margin
close_btn.move(close_btn_x, close_btn_y)

max_btn = QPushButton(window)
max_btn.setText('最大化')
max_btn.resize(btn_w, btn_h)

max_btn_x = close_btn_x - max_btn.width()
max_btn_y = top_margin
max_btn.move(max_btn_x, max_btn_y)

min_btn = QPushButton(window)
min_btn.setText('最小化')
min_btn.resize(btn_w, btn_h)

min_btn_x = max_btn_x - min_btn.width()
min_btn_y = top_margin
min_btn.move(min_btn_x, min_btn_y)

close_btn.pressed.connect(window.close)
max_btn.pressed.connect(window.showMaximized)
min_btn.pressed.connect(window.showMinimized)

window.setStyleSheet(qdarkgraystyle.load_stylesheet())
window.show()

sys.exit(app.exec_())
