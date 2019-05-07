import requests, random, bs4, openpyxl
aa = openpyxl.Workbook() #创建一个工作簿
sheet = aa.active #获取工作簿的活动表
sheet.title = '豆瓣电影top250' #工作表重命名

sheet['A1'] = '排名号'  #加表头，给A1单元格赋值
sheet['B1'] = '电影名'
sheet['C1'] = '评价'
sheet['D1'] = '推荐语'
sheet['E1'] = '链接'

for x in range(10):
    url = 'https://movie.douban.com/top250?start=' + str(x*25) + '&filter='
    res = requests.get(url)
    bs = bs4.BeautifulSoup(res.text, 'html.parser')
    bs = bs.find('ol', class_="grid_view")
    for titles in bs.find_all('li'):
        num = titles.find('em',class_="").text
        title = titles.find('span', class_="title").text
        comment = titles.find('span',class_="rating_num").text
        url_movie = titles.find('a')['href']

        if titles.find('span',class_="inq") != None:
            tes = titles.find('span',class_="inq").text
            sheet.append([num,title,comment,tes,url_movie])
            print(num + '.' + title + '——' + comment + '\n' + '推荐语：' + tes +'\n' + url_movie)
        else:
            sheet.append([num,title,comment,'',url_movie])
            print(num + '.' + title + '——' + comment + '\n' +'\n' + url_movie)
aa.save('doubiantop250.xlsx')