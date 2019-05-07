import requests, random, bs4, csv
#引用csv模块
csv_file = open('doubiantop250.csv','w',newline='',encoding='utf-8')
#调用open()函数打开csv文件，传入参数
writer = csv.writer(csv_file)
#用csv.writer()函数创建一个writer对象
writer.writerow(['排行号','电影名','评分','推荐语','链接'])
#调用writer对象的wrtierow()方法，可以在csv文件里写入一行文字
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
            writer.writerow([str(num) , str(title) , str(comment) , str(tes) , str(url_movie)])
            #print(num + '.' + title + '——' + comment + '\n' + '推荐语：' + tes +'\n' + url_movie)
        else:
            writer.writerow([str(num) , str(title) , str(comment) , '' , str(url_movie)])
            #print(num + '.' + title + '——' + comment + '\n' +'\n' + url_movie)
csv_file.close()