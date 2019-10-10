'''
列出当前目录下的所有文件盒目录名
'''
import os
print([d for d in os.listdir('.')])