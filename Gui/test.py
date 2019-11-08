
import sys
from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("sdfs")
        self.resize(500,500)
        self.setui()

    def setui(self):
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())