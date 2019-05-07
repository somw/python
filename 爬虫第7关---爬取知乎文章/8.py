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
    if answer == 'Y':    #如果用户认识：
        danci.append(x['content'])
        words_konws.append(x)   #就把这个单词，追加进列表words_knows。
        print(words_konws)
    else:
        not_knows.append(x)    #就把这个单词，追加进列表not_knows。 

#打印一个统计数据：这么多单词，认识几个，认识的有哪些？
print('\n一共有' + str(len(json_word['data'])) + '个单词')
print('你认识单词有'+ str(len(danci)) +'个，你认识的有哪些？')
print(danci)