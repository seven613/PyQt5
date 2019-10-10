'''
冒泡算法
Python中range()函数的用法

1、函数原型：range（start， end， scan)：

参数含义：

start:计数从start开始。默认是从0开始。例如range（5）等价于range（0， 5）;

end:技术到end结束，但不包括end.例如：range（0， 5） 是[0, 1, 2, 3, 4]没有5

scan：每次跳跃的间距，默认为1。例如：range（0， 5） 等价于 range(0, 5, 1)
'''
#定义列表，len(lis) =15,index:0,1,2,3,4,5,6,7,8,9,10,11,12,13,14
lis =[56,12,1,8,354,10,100,34,56,7,23,23,456,234,-58]
#排序函数,数字越小越靠前
def sortport(lis):
    for i in range(len(lis)-1): #从左往右依次循环
        for j in range(len(lis) - 1 - i):
            if lis[j] > lis[j+1]:
                lis[j],lis[j+1]=lis[j+1],lis[j]

            #print('第%s次循环,lis[%s]是:%s,lis[%s+1]是%s,列表lis是:%s'%(j,j,lis[j],j,lis[j+1],lis))

    return lis

sortport(lis)
print(lis)