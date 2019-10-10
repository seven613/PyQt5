'''
替换列表字符
'''
num =['harden','lampard',3,34,45,76,87,45,3,3,3,67862,98,75]

for i in range(num.count(3)):#取出3出现的次数
    ele_index =num.index(3)#获取首次3出现的坐标
    num[ele_index]='3a'#修改3为3a
    print(num)