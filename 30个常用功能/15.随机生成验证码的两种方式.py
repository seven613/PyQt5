'''
随机生成验证码的两种方式
'''
import random
list1 =[]
for i in range(65,91):
    list1.append(chr(i))#通过循环遍历asii追加到空列表中
for j in range(97,123):
    list1.append(chr(j))
for k in range(48,58):
    list1.append(chr(k))

ma = random.sample(list1,6)
ma=''.join(ma)
print(ma)

