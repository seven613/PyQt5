'''
输出路径及其子目录下的所有文件路径
'''

import os
def show_dir(filepath):
    for i in os.listdir(filepath):
        path = (os.path.join(filepath,i))
        print(path)
        if os.path.isdir(path):
            show_dir(path)

filepath ="e:\codes\python\pyqt\pyqt5"
show_dir(filepath)