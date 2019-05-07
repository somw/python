import csv
#引用csv模块
csv_file = open('demo.csv','w',newline='',encoding='gbk')
#调用open()函数打开csv文件，传入参数：文件名“demo.csv”、写入模式“w”、newline=''、encoding='utf-8'
writer = csv.writer(csv_file)
#用csv.writer()函数创建一个writer对象
writer.writerow(['电影1','电影2'])
#调用writer对象的writerow()方法，可以在csv文件里写入一行文字“电影1”和“电影2”
writer.writerow(['电影3','电影4'])
#csv文件里写入一行文字“电影3”和“电影4”
writer.writerow(['电影5','电影6'])
#csv文件里写入一行文字“电影5”和“电影6”
csv_file.close()
#写入完成后，关闭文件就大功告成啦