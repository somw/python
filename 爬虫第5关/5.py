import requests,openpyxl
wb = openpyxl.Workbook() #创建工作簿
sheet = wb.active #获取工作簿的活动表
sheet.title = 'mm' #工作表重命名

sheet['A1'] = '歌曲名' #加表头，给A1单元格赋值
sheet['B1'] = '所属专辑' #加表头，给B1单元格赋值
sheet['C1'] = '播放时长' #加表头，给C1单元格赋值
sheet['D1'] = '播放链接' #加表头，给D1单元格赋值


url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp'
for x in range(5):

    params = {
        'ct': '24',
        'qqmusic_ver': '1298',
        'new_json': '1',
        'remoteplace': 'sizer.yqq.song_next',
        'searchid': '64405487069162918',
        't': '0',
        'aggr': '1',
        'cr': '1',
        'catZhida': '1',
        'lossless': '0',
        'flag_qc': '0',
        'p': str(x + 1),
        'n': '20',
        'w': '周杰伦',
        'g_tk': '5381',
        'loginUin': '0',
        'hostUin': '0',
        'format': 'json',
        'inCharset': 'utf8',
        'outCharset': 'utf-8',
        'notice': '0',
        'platform': 'yqq.json',
        'needNewCode': '0'
    }

    res_music = requests.get(url, params=params)
    json_music = res_music.json()
    list_music = json_music['data']['song']['list']
    for music in list_music:
        name = music['name']
        album = music['album']['name']
        time = music['interval']
        link = 'https://y.qq.com/n/yqq/song/' + music['file']['media_mid'] + '.html\n\n'
        sheet.append([name,album,time,link]) #把name,album,time和link写成列表，用append函数多行写入Excel
        print('歌曲名：' + name + '\n' + '所属专辑：' + album + '\n' + '播放时长：' + str(time) + '\n' + '播放链接：' + link)
wb.save('Jay.xlsx')