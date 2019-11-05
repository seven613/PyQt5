# -*- coding: utf-8 -*- 
"""
Project: PyQt5
Creator: zhangqiang
Create time: 2019-10-29 14:14
IDE: PyCharm
Introduction:
"""

import sys
from PyQt5.Qt import *

app = QApplication(sys.argv)

window = QWidget()

# window.resize(500,500)
# window.move(300,300)

window.setGeometry(300,300,500,500)

window.show()
sys.exit(app.exec_())