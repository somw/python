# 先导入模块
import math

# 方法1：条件判断
def abs_value1():
    a = float(input("请你输入一个数字："))
    if a >= 0:
        a = a
    else:
        a = -a
    print('绝对值为：%f' % a)


# 方法2：内置函数
def abs_value2():
    a = float(input("请你输入一个数字："))
    a = abs(a)
    print('绝对值为：%f' % a)

# 方法3：内置模块
def abs_value3():
    a = float(input("请你输入一个数字："))
    a = math.fabs(a)
    print('绝对值为：%f' % a)


# 运行函数，查验一下
abs_value1()
abs_value2()
abs_value3()