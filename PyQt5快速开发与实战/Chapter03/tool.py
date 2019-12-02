#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2019/12/2 6:50 下午
@Author:  zhangqiang
@File: tool.py
@Software: PyCharm
@Title: 将当前目录下的ui文件编译为py文件
"""

import os
import os.path

# UI所在的文件路径
dir = './'


# 列出路径下所有的UI文件
def listUiFile():
    list = []
    files = os.listdir(dir)
    for filename in files:
        if os.path.splitext(filename)[1] == '.ui':
            list.append(filename)
    return list


# 把UI文件转换为py文件
def transPyFile(filename):
    return os.path.splitext(filename)[0] + '.py'


# 调用系统命令把UI转换为py文件
def runMain():
    list = listUiFile()
    for uifile in list:
        pyfile = transPyFile(uifile)
        cmd = 'pyuic5 -o {pyfile} {uifile}'.format(pyfile=pyfile, uifile=uifile)
        os.system(cmd)


if __name__ == '__main__':
    runMain()
