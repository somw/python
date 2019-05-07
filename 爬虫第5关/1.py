import requests

url = "https://c.y.qq.com/soso/fcgi-bin/client_search_cp"
for x in range(1,5):
    params = {
        'ct': '24',
        'qqmusic_ver': '1298',
        'remoteplace': 'txt.yqq.lyric',
        'searchid': '101993666451794734',
        'aggr': '0',
        'catZhida': '1',
        'lossless': '0',
        'sem': '1',
        't': '7',
        'p': str(x),
        'n': '5',
        'w': '周杰伦',
        'g_tk': '5381',
        'loginUin': '0',
        'hostUin': '0',
        'format': 'json',
        'inCharset': 'utf8',
        'outCharset': 'utf-8',
        'notice': '0',
        'platform': 'yqq.json',
        'needNewCode': '0',
	}
    #将参数封装为字典
res_music = requests.get(url,params=params)
#调用get方法，下载这个字典
json_music = res_music.json()
#调用json方法，将response对象，转为列表/字典
list_music = json_music['data']['lyric']['list']
#一层一层地取字典，获取歌单列表
for music in list_music:
#list_music是一个列表，music是它里面的元素
    print(music['content'].replace('<em>','').replace('</em>','').replace('\\n','\r\n'))
    #以content为键，查找歌词