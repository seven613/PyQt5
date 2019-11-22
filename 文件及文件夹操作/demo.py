# -*- coding: utf-8 -*- 
"""
Project: PyQt5
Creator: zhangqiang
Create time: 2019-11-06 09:49
IDE: PyCharm
Introduction:
"""
import os
input_folder ='路径名'
# 1.判断指定目录是否存在
os.path.exists(input_folder)
# 2.判断指定目录是不是文件夹
os.path.isdir(input_folder)
# 3.判断指定目录是不是文件
os.path.isfile(input_folder)
# 4.判断指定文件是不是图片(判断给定文件是何种图片类型)
import imghdr
input_filename ='文件名'
img_list ={'jpg','bmp','png','jpeg','rgb','gif','pbm','ppm','tiff','xbm'}
if imghdr.what(input_filename) not in img_list:
    print('不是图片')

# 5.判断指定txt(文件)是否为空
if os.path.getsize('test.txt') is 0:
    print('文件为空')
# 6.按行读取txt文件内容
f = open('test.txt','r')
lines = f.readlines()
for line in lines:
    print(line)
    line = line.strip('\n')
    print(line)
# 7.遍历指定目录文件夹下所有文件
import glob
for file in sorted(glob.glob(os.path.join(input_folder,"*.*"))):
    print(file)



