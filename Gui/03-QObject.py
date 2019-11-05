# -*- coding: utf-8 -*- 
"""
Project: PyQt5
Creator: zhangqiang
Create time: 2019-10-17 16:49
IDE: PyCharm
Introduction:
"""

import sys
from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("QObject的学习")
        self.resize(500,500)
        self.setui()

    def setui(self):
        #self.QObject继承结构测试()
        #self.QOject对象名称和属性的操作()
        #self.QObject对象的父子关系操作()
        #self.QObject信号的操作()
        #self.QObject类型判定()
        self.QObject对象删除()


    def QObject继承结构测试(self):
        #QObject.__subclasses__()
        mros = QObject.mro()
        for mro in mros:
            print(mro)

    def QOject对象名称和属性的操作(self):
        # ************************测试API******************开始
        # obj = QObject()
        # obj.setObjectName("notice")#设置对项名
        # print(obj.objectName())
        #
        # obj.setProperty("notice_level","error")#设置属性
        # obj.setProperty("notice_level2", "warning")#设置属性
        #
        # print(obj.property('notice_level'))#获取其中一个属性
        # print(obj.dynamicPropertyNames()) #获取所有属性

        # ************************测试API******************结束

        # ************************案例演示******************开始
        with open('QObject.css','r') as f:
            qApp.setStyleSheet(f.read())

        label = QLabel(self)
        label.setText("第一个label标签")
        label.move(100,0)
        label.setObjectName('notice')
        label.setProperty('notice_level','normal')


        label2 = QLabel(self)
        label2.move(100,100)
        label2.setText("第二个label标签")
        label2.setObjectName('notice')
        label2.setProperty('notice_level','warning')

        label3 = QLabel(self)
        label3.setText('第三个label标签')
        label3.move(100,200)
        label3.setObjectName('notice')
        label3.setProperty('notice_level','error')



        btn = QPushButton(self)
        btn.setText("提交")
        btn.move(300,300)

        # ************************案例演示******************结束

    def QObject对象的父子关系操作(self):
        #***************测试API*****************开始
        # obj1 = QObject()
        # obj2 = QObject()
        # print("obj1",obj1)
        # print("obj2",obj2)
        #
        # obj1.setParent(obj2)
        # print(obj1.parent())
        # ***************测试API*****************结束
        # ***************父子关系图*****************开始
        # obj0 = QObject()
        # obj1 = QObject()
        # obj2 = QObject()
        # obj2.setObjectName('2')
        # obj3 = QObject()
        # obj4 = QObject()
        # obj5 = QObject()
        # print('obj0',obj0)
        # print('obj1', obj1)
        # print('obj2', obj2)
        # print('obj3', obj3)
        # print('obj4', obj4)
        # print('obj5', obj5)
        #
        # obj1.setParent(obj0)
        # obj2.setParent(obj0)
        # obj3.setParent(obj1)
        # obj4.setParent(obj2)
        # obj5.setParent(obj2)
        # print('---------------------')
        # print(obj4.parent())
        # print(obj2.children())
        # print('---------------------')
        # print(obj0.findChild(QObject, '2', Qt.FindChildrenRecursively))
        # ***************父子关系图*****************开始
        # ***************内存管理机制*****************开始
        obj1 = QObject()
        obj2 = QObject()

        obj2.setParent(obj1)

        #监听obj2对象被释放

        obj2.destroyed.connect(lambda :print('obj2对象被释放了'))

        # ***************内存管理机制*****************开始

        win1 = QWidget()
        win1.resize(500, 500)
        win1.setStyleSheet('background-color:red;')

        win2 = QWidget()
        win2.setStyleSheet('background-color:green;')
        win2.resize(1000, 100)  # win2大小受win1窗口大小限制
        win2.setParent(win1)  # 设置父子关系，win2窗口就在win1窗口里了

        label = QLabel()
        label.setText("标签")
        label.move(20, 20)
        label.setStyleSheet('background-color:cyan;')
        label.setParent(win2)
        # 循环窗口所有子对象，可以更改统一样式

        win1.show()
        win2.show()
    def QObject信号的操作(self):
        #**************信号与槽案例*****************开始
        btn = QPushButton(self)
        btn.setText("点我")
        btn.move(100,100)
        def cao():
            print("点我干涉吗")
        btn.clicked.connect(cao)

        def windotitlecao(name):
            print('窗口标题改变了','撩开'+name)
            self.blockSignals(True)
            self.setWindowTitle('撩开'+name)
            self.blockSignals(False)

        self.windowTitleChanged.connect(windotitlecao)
        # **************信号与槽案例*****************结束

        #self.obj = QObject()
        # def destroy_cao(obj):
        #     print("对象被释放了",obj)
        #
        # self.obj.destroyed.connect(destroy_cao)
        # del self.obj
        #
        # def obj_name_cao(name):#定义槽函数
        #     print('对象名称发生了改变',name)
        # self.obj.objectNameChanged.connect(obj_name_cao)#对象名称更改信号连接槽函数
        #
        # print('当前对象这个信号正在连接的槽的数量：',self.obj.receivers(self.obj.objectNameChanged))#当前对象objectNameChanged信号正在连接的槽的数量
        # self.obj.setObjectName('xxxx')#对象改变名称
        # #self.obj.objectNameChanged.disconnect()#断开信号与槽函数的连接，但是信号还是被执行了
        # print(self.obj.signalsBlocked(),'1')#查看信号是否被阻断
        # self.obj.blockSignals(True)#临时阻断一下信号与槽函数，导致下面一句不执行槽函数
        # print(self.obj.signalsBlocked(),'2')
        # self.obj.setObjectName('ooo')#改变对象名称，但是没有执行槽函数，因为已经断开连接了
        # #self.obj.objectNameChanged.connect(obj_name_cao)  # 对象名称更改信号再次连接槽函数
        # self.obj.blockSignals(False)#开启信号与槽的连接
        # print(self.obj.signalsBlocked(),'3')
        # self.obj.setObjectName('xxoo')  # 改变对象名称，但是没有执行槽函数，因为已经断开连接了

    def QObject类型判定(self):
        # *********************API*****************开始
        # obj = QObject()
        # w = QWidget()
        # btn = QPushButton()
        # label =QLabel()
        # objs =[obj,w,btn,label]
        # for o in objs:
        #     print(o.isWidgetType())
        # *********************API*****************结束
        # *********************案例*****************开始
        label1  = QLabel(self)
        label1.setText("第一个标签")
        label1.move(100,100)

        label2 = QLabel(self)
        label2.setText("第一个标签")
        label2.move(100,150)

        btn = QPushButton(self)
        btn.setText("点我")
        btn.move(100,200)
        for widget in self.children():#循环self的所有子控件
            print(widget)
            if widget.inherits("QLabel"):#判定widget这个控件是否是继承自QLabel
                print("是")
                widget.setStyleSheet('background-color:cyan')

        # for obj in [label1,label2,btn]:
        #     obj.setStyleSheet('background-color:cyan')

        # *********************案例*****************结束

    def QObject对象删除(self):
        obj1 = QObject()
        self.obj1 =obj1
        obj2 = QObject()
        obj3 = QObject()

        obj2.setParent(obj1)
        obj3.setParent(obj2)

        obj1.destroyed.connect(lambda: print('obj1被释放了'))
        obj2.destroyed.connect(lambda: print('obj2被释放了'))
        obj3.destroyed.connect(lambda: print('obj3被释放了'))

        #del obj2
        obj2.deleteLater()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.setWindowTitle("窗口标题1")

    window.setWindowTitle("窗口标题2")
    window.show()

    sys.exit(app.exec_())