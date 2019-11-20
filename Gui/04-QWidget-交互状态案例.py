# -*- coding: utf-8 -*- 
"""
项目: PyQt5
作者: 张强
创建时间: 2019-11-19 15:07
IDE: PyCharm
介绍:
"""

import sys
from PyQt5.Qt import *
import qdarkgraystyle


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("交互状态案例")
        self.resize(500, 500)
        self.setui()

    def setui(self):
        # 添加三个子控件
        label = QLabel(self)
        label.setText("标签")
        label.hide()  # 隐藏

        lineEdit = QLineEdit(self)
        lineEdit.setText("文本框")

        def text_cao(text):
            # if len(text) > 0:
            #     btn.setEnabled(True)
            # else:
            #     btn.setEnabled(False)
            #
            btn.setEnabled(len(text) > 0)

        lineEdit.textChanged.connect(text_cao)

        def check():
            content = lineEdit.text()
            if content == "Sz":
                label.setText("登录成功")
            else:
                label.setText("登录失败")

            label.setVisible(True)
            label.adjustSize()#自适应

        btn = QPushButton(self)
        btn.setText("登陆")
        btn.setEnabled(False)  # 设置为不可用

        btn.pressed.connect(check)

        label.move(10, 10)
        lineEdit.move(10, 50)
        btn.move(10, 100)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.setStyleSheet(qdarkgraystyle.load_stylesheet())
    window.show()
    sys.exit(app.exec_())
