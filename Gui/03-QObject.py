#-*-coding:utf-8 -*-
"""..."""
__author__ = '张强'


from PyQt5.Qt import *  # 主要包含了我们常用的一些类，汇总到了一块

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QObject的学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        #self.QObject继承结构测试()
        self.QObject对象名称和属性的操作()

    def QObject继承结构测试(self):
        #QObject.__mro__
        mros = QObject.mro()
        for mro in mros:
            print(mro)

    def QObject对象名称和属性的操作(self):

        #**************************测试API***********************开始
        # obj= QObject()
        # obj.setObjectName("notice")
        # print(obj.objectName())
        # 
        # obj.setProperty("notice_level","error")
        # obj.setProperty("notice_level2","warning")
        # 
        # print(obj.property("notice_level"))
        # print(obj.dynamicPropertyNames())
        # **************************测试API***********************结束


        # **************************案例演示***********************开始
        with open("E:\\Codes\\Python\\PyQt\\PyQt5\\QObject.qss","r") as f:
            qApp.setStyleSheet(f.read())

        label = QLabel(self)
        label.setObjectName('notice')
        label.setProperty('notice_level',"normal")
        label.setText("案例演示")

        #label.setStyleSheet("font-szie:20px;color:red;")

        label2 = QLabel(self)
        label2.setObjectName('notice')
        label2.setProperty('notice_level',"warning")
        label2.move(100,100)
        label2.setText("测试样例")

        btn = QPushButton(self)
        btn.setText("BTN")
        btn.move(50,50)


        # **************************案例演示***********************结束

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())