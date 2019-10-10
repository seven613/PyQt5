'''
合并去重
'''
list1 = [2,3,5,7,5,9,6]
list2 = [5,6,10,11,4,17,2]

list3 = list1 +list2

print(list3) #列表合并，不去重
print(set(list3))#去重，类型为set需要转换乘list
print(list(set(list3)))
