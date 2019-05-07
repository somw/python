import requests
res_abc = requests.get('https://www.shanbay.com/api/v1/vocabtest/category/')
#调用get()方法，下载这个字典
json_abc = res_abc.json()
#使用json()方法，将response对象转为字典/列表
# bianhao = int(input('''请输入你选择的词库编号，按Enter确认
# 1，GMAT  2，考研  3，高考  4，四级  5，六级
# 6，英专  7，托福  8，GRE  9，雅思  10，任意
# >'''))
# abc_list = json_abc['data'][ bianhao-1][0]
# print(abc_list)
abc_list = json_abc['data']

for i in range(1,11):
    print(str(i) + '，' + abc_list[i-1][1])

aa = int(input('请输入你选择的词库编号，按Enter确认:'))
word = abc_list[aa-1][0]
res_word = requests.get('https://www.shanbay.com/api/v1/vocabtest/vocabularies/?category='+str(word))
#调用get()方法，并且网址后面加str(word),下载这个字典
json_word = res_word.json()
#使用json()方法，将response对象转为字典/列表
danci = []    #新增一个list，用于统计用户认识的单词
words_konws = []  #创建一个空的列表，用于记录用户认识的单词。
not_knows = []    #创建一个空的列表，用于记录用户不认识的单词。
print('测试现在开始，如果你认识这个单词，请输入Y，否则直接敲Endter:')
n = 0
for x in json_word['data']:  #启动一个循环，循环的次数等于单词的数量。
    n = n+1
    print('\n第'+str(n)+'个：'+ x['content'])   #记得加一个\n，用于换行。
    answer = input('认识请敲Y，否则敲Enter:')    #让用户输入自己是否认识。
    if answer.upper() == 'Y':    #如果用户认识：
        danci.append(x['content'])
        words_konws.append(x)   #就把这个单词，追加进列表words_knows。
        #print(words_konws)
    else:
        not_knows.append(x)    #就把这个单词，追加进列表not_knows。 

#打印一个统计数据：这么多单词，认识几个，认识的有哪些？
print('\n一共有' + str(len(json_word['data'])) + '个单词，你认识单词有' + str(len(danci)) +'个，你认识的有哪些？')
print(danci)

print('现在我们来检测一下，你有没有真正掌握它们')
wrong_word = [] #创建一个空的列表，用于记录用户错误的单词
right_num = 0
for r in words_konws:
    print('A.' + r['definition_choices'][0]['definition'])
    print('B.' + r['definition_choices'][1]['definition'])
    print('C.' + r['definition_choices'][2]['definition'])
    print('D.' + r['definition_choices'][3]['definition'])
    xuanze = input('请选择单词\"'+r['content']+'\"的正确翻译（填写数字即可）：')
    dic = { 'A': r['definition_choices'][0]['rank'], 'B': r['definition_choices'][1]['rank'], 'C': r['definition_choices'][2]['rank'], 'D': r['definition_choices'][3]['rank'] }
    #我们创建一个字典，搭建起A、B、C、D和四个rank值的映射关系。
    #print(dic[xuanze])
    if dic[xuanze] == r['rank']:
        right_num += 1
    else:
        wrong_word.append(r)
print('现在，到了公布成绩的时刻：')
bbb = abc_list[aa-1][1]
print('在'+ str(len(json_word['data'])) + '个' + str(bbb) + '词汇当中，你认识其中' + str(len(danci)) + '个，实际掌握' + str(right_num) + '个，错误' + str(len(wrong_word)) + '个。')


save = input ('是否打印并保存你的错词集？填入Y或N： ')
#询问用户，是否要打印并保存错题集。
if save.upper() == 'Y':
#如果用户说是：
    f = open('错题集.txt', 'a+')
    #在当前目录下，创建一个错题集.txt的文档。        
    print ('你记错的单词有：')
    f.write('你记错的单词有：\n')    #写入"你记错的单词有：\n"
    m=0
    for z in wrong_word:
    #启动一个循环，循环的次数等于，用户的错词数：
        m=m+1
        print (z['content'])
        #打印每一个错词。
        f.write(str(m) +'. '+ z['content']+'\n')   #写入序号，写入错词。           
    print ('你不认识的单词有：')
    f.write('你没记住的单词有：\n')    #写入"你没记住的单词有：\n"
    s=0
    for i in not_knows:
    #启动一个循环，循环的次数等于，用户不认识的单词数。
        s=s+1
        print (i['content'])
        #打印每一个不认识的单词。
        f.write(str(s) +'. '+ i['content']+'\n')   #写入序号，写入用户不认识的词汇。 
    print ('错词和没记住的词已保存至当前文件目录下，下次见！')
    #告诉用户，文件已经保存好。
    #在网页版终端运行时，文件会被写在课程的服务器上，你看不到，但它的确已经存在。
else:
#如果用户不想保存：
    print('下次见！')