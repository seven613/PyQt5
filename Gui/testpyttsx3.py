#-*-coding:utf-8 -*-
"""文字转语音"""
__author__ = '张强'


import pyttsx3

with open('/Users/zhangqiang/PycharmProjects/PyQt5/Gui/read.txt','r',encoding='utf-8') as f:
    line = f.read()#文件不大，一次性读取
    engine = pyttsx3.init()
    #调整频率
    rate = engine.getProperty('rate')
    engine.setProperty('rate',rate -50 ) #调整语速快慢
    #调整音量
    volume = engine.getProperty('volume')
    engine.setProperty('volume',volume + 0.25)
    engine.say(line)
    engine.runAndWait()