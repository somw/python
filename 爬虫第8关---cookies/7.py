from tkinter import Tk,Button,Text,Entry,Label,END


window = Tk()

window.title(u'我的翻译')

#设置窗口大小和位置
window.geometry('310x370+500+300')
window.minsize(320,370)
window.maxsize(320,370)


#创建一个文本框
text1 = Text(window,background = 'azure')
# 喜欢什么背景色就在这里面找哦，但是有色差，得多试试：http://www.science.smith.edu/dftwiki/index.php/Color_Charts_for_TKinter
text1.place(x = 10,y = 10,width = 300,height = 160)
text1.bind("<Key-Return>")

#创建一个按钮
#为按钮添加事件
submit1 = Button(window,text=u'翻译')
submit1.place(x=195,y=172,width=55,height=25)
submit2 = Button(window,text=u'清空')
submit2.place(x=255,y=172,width=55,height=25)

#翻译结果标题
title_label = Label(window,text=u'翻译结果:')
title_label.place(x=10,y=175)

#翻译结果
text2 = Text(window,background = 'light cyan')
text2.place(x = 10,y = 200,width = 300,height = 160)
window.mainloop()