'''
把原字典键值对颠掉重新生成字典
'''

dict ={'A':'a','B':'b','C':'c',"D":"d"}
dict2 = {y:x for x,y in dict.items()}
print(dict2)