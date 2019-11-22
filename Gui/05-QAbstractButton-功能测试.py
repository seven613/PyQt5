# -*- coding: utf-8 -*- 
"""
项目: PyQt5
作者: 张强
创建时间: 2019-11-20 13:50
IDE: PyCharm
介绍:
"""
import sys
from PyQt5.Qt import *

import qdarkgraystyle

class Button(QPushButton):
    def hitButton(self, *args, **kwargs):
        pass


app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("按钮功能测试--抽象类")
window.resize(500, 500)


# *********************文本操作*****************开始
def plus_one():
    num = int(btn.text())
    num += 1
    btn.setText(str(num))


btn = QPushButton(window)
btn.setText("1")
btn.pressed.connect(plus_one)
btn.adjustSize()

# *********************文本操作*****************结束

# *********************图标操作*****************开始
icon = QIcon(r'E:\Codes\Python\PyQt\PyQt5\Gui\resource\p1.jpg')
btn.setIcon(icon)#设置按钮图标

size = QSize(50, 50)
btn.setIconSize(size)#设置按钮图标大小
# 
# print(btn.icon())
# print(btn.iconSize())
# *********************图标操作*****************结束

# *********************快捷键*****************开始
# btn.setText('&abc')
# btn.setShortcut('Alt+G')
# *********************快捷键*****************结束

# *********************自动重复*****************开始
#print(btn.autoRepeat())
btn.setAutoRepeat(True)#设置自动重复，按住按钮不放时，自动执行按钮的功能
btn.setAutoRepeatDelay(3000)#延迟3秒后自动重复执行，第一次点击之后的延迟
btn.setAutoRepeatInterval(1000)#每隔1秒就执行一次，开始重复后，间隔时间后才执行
# *********************自动重复*****************结束

# *********************按钮状态*****************开始
push_button =QPushButton(window)
push_button.setText("按钮")
push_button.move(100,100)
radio_button = QRadioButton(window)
radio_button.setText("单选")
radio_button.move(100,150)
checkbox = QCheckBox(window)
checkbox.setText("复选")
checkbox.move(100,200)

push_button.setStyleSheet("QPushButton:pressed {background-color:red;}")
# 把三个按钮都置为按下状态
# push_button.setDown(True)
# radio_button.setDown(True)
# checkbox.setDown(True)
push_button.setCheckable(True)
print(push_button.isCheckable())
print(radio_button.isCheckable())
print(checkbox.isCheckable())

radio_button.setChecked(True)
push_button.setChecked(True)
checkbox.setChecked(True)

print(push_button.isChecked())
print(radio_button.isChecked())
print(checkbox.isChecked())

def cao():
    print("cao")
    push_button.toggle()
    radio_button.toggle()
    checkbox.toggle()

    push_button.setChecked(not push_button.isChecked())
    radio_button.setChecked(not radio_button.isChecked())
    checkbox.setChecked(not checkbox.isChecked())

btn.pressed.connect(cao)
# *********************按钮状态*****************结束


# *********************排他性*****************开始
for i in range(0,3):
    btn_c = QPushButton(window)
    btn_c.setText("btn_"+str(i))
    btn_c.move(50*i,50)
    btn_c.setAutoExclusive(True)

    print(btn_c.autoExclusive())
    print(btn_c.isCheckable())

# *********************排他性*****************结束


# *********************按钮模拟点击*****************开始
btn_a = QPushButton(window)
btn_a.setText("模拟点击")
btn_a.move(200,200)
btn_a.pressed.connect(lambda :print("模拟点击这个按钮"))
#btn_a.click()
#btn_a.animateClick(2000)
# *********************按钮模拟点击*****************结束
# *********************设置有效点击区域*****************开始

btn_b = Btn(window)
btn_b.setText("有效点击")
btn_b.move(250,250)
btn_b.pressed.connect(lambda :print("按钮被点击了"))
# *********************设置有效点击区域*****************结束



window.setStyleSheet(qdarkgraystyle.load_stylesheet())
window.show()

sys.exit(app.exec_())
