# -*- coding: utf-8 -*- 
"""
项目: PyQt5
作者: 张强
创建时间: 2019-11-08 16:12
IDE: PyCharm
介绍:
"""
import sys
from PyQt5.Qt import *
import qdarkgraystyle
app = QApplication(sys.argv)
window = QWidget()

window.resize(500,500)

# window.setWindowIcon(QIcon('E:\Codes\Python\PyQt\PyQt5\Gui\PyQt5界面美化素材\p1.jpg'))#设置窗口图标
# window.setWindowOpacity(0.9) #设置窗口透明

print(window.windowState() == Qt.WindowNoState)
# Qt.WindowNoState#无状态
# Qt.WindowMinimized#最小化
# Qt.WindowMaximized#最大化
# Qt.WindowFullScreen#全屏无标题栏
# Qt.WindowActive#活动窗口
window.setWindowState(Qt.WindowMinimized)

w2 =QWidget()
w2.setWindowTitle('窗口2')
w2.show()

window.setStyleSheet(qdarkgraystyle.load_stylesheet())
window.show()
window.setWindowState(Qt.WindowActive)

sys.exit(app.exec_())