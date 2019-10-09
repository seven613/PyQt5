#-*-coding:utf-8 -*-
"""..."""
__author__ = '张强'

from PyQt5.Qt import *  # 主要包含了我们常用的一些类，汇总到了一块

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("类")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        label = QLabel(self)
        label.setText("XXX")

if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    window = Window()
    window.show
    sys.exit(app.exec_())
