# -*- coding: utf-8 -*- 
"""
Project: PyQt5
Creator: zhangqiang
Create time: 2019-10-14 10:48
IDE: PyCharm
Introduction:
"""


class Person1(object):
    country = 'china'  # 类属性
    __language = "Chinese"  # 私有类属性也不能直接外部调用

    def __init__(self, name, age):
        self.name = name
        self.__age = age  # 使用__下划线表示私有属性，对象不能直接调用，要通过方法调调用

    def getAge(self):
        return self.__age

    def setAge(self, age):
        if age > 100 or age < 0:
            print("age is not true")
        else:
            self.__age = age

    def __str__(self):
        info = "name :" + self.name + ",age(保密):" + str(self.__age)  # 注意这里不是self.age
        return info


# ------创建对象,调用方法，属性测试-------------------------------------------------------
stu1 = Person1("tom", 18)
print("修改前的结果：", stu1.__str__())
stu1.name = "tom_2"  # 修改stu1的name属性
print("修改name后的结果：", stu1.__str__())
# print(stu1.__age)  #直接调用私有属性__age报错，'Person1' object has no attribute '__age'

print("打印私有age内存地址：", id(stu1.getAge()))
stu1.__age = 19  # 如果这样赋值的话，不会报错，因为系统找不到这个变量，直接新建了一个。但是实际没有修改对象的属性值
print(stu1.__age)  # 有值，但是没有 实际修改stu1对象的age属性值
print("打印stu1.__age的内存地：", id(stu1.__age))  # 两个内存地址值不一样。
print("错误修改age后的值", stu1.__str__())  # 实际值没有变

stu1.setAge(22)  # 只有调用才可以修改age的值
print("正确修改age后的值", stu1.__str__())
