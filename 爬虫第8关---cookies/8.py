from tkinter import *

# 创建窗口对象的背景色
root = Tk()
# 创建两个列表
li = ['a','b','c','d']
movie = ['mp4','avi','rm']
# 创建两个列表组件
listb = Listbox(root)
listb1 = Listbox(root)
# 第一个小部件插入数据
for item in li:
    listb.insert(0,item)
# 第二个小部件插入数据
for item in movie:
    listb1.insert(0,item)

# 将小部件放置到主窗口中
listb.pack()
listb1.pack()

# 进入消息循环
root.mainloop()