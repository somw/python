import requests,  random, bs4, csv
#引用csv模块。
csv_file=open('movieTop250.csv', 'w', newline='')
#调用open()函数打开csv文件，传入参数：文件名“movieTop250.csv”、写入模式“w”、newline=''。
writer = csv.writer(csv_file)
# 用csv.writer()函数创建一个writer对象。
writer.writerow(['序号', '电影名', '评分', '推荐语', '链接'])
#调用writer对象的writerow()方法，可以在csv文件里写入title:'序号', '电影名', '评分', '推荐语', '链接'

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
            # 把num, title, comment, tes和url_movie写成列表，用append函数多行写入Excel
            writer.writerow([num + '.' + title + '——' + comment + '\n' + '推荐语：' + tes +'\n' + url_movie])
        else:
            writer.writerow([num + '.' + title + '——' + comment + '\n' +'\n' + url_movie])
        
csv_file.close()