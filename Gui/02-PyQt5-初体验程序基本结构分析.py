#-*-coding:utf-8 -*-
"""..."""
__author__ = '张强'


#0.导入需要的包和模块
import sys
from PyQt5.Qt import * #主要包含了我们常用的一些类，汇总到了一块

#代码执行方式 右击执行；命令行python 代码名称
#1.创建一个应用对象
app = QApplication(sys.argv)

#2.控件的操作
#创建控件，设置大小、位置、样式，事件，信号的处理
#2.1创建控件
window = QWidget()
#2.2设置控件
window.setWindowTitle("sdlfajslflajflad")

label =QLabel(window)#增加label，并把它放到window控件上，组成了父子关系
label.setText("sdssss")#设置label标题
label.setWindowTitle("Label")#不起做了，因为label已经有了父控件window
label.show()#不起作用，因为window已经展示了。一般情况，父控件展示所有子控件
#2.3展示控件



window.show()


#3.应用程序的执行，进入到消息循环
#让整个程序开始执行，并且进入到消息循环(无限循环)
#监测整个程序所接收到的用户的交互信息
sys.exit(app.exec_())

