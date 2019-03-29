import requests
# 引用requests库
from bs4 import BeautifulSoup
# 引用BeautifulSoup库

res_foods = requests.get('http://www.xiachufang.com/explore/')
# 获取数据
bs_foods = BeautifulSoup(res_foods.text,'html.parser')
# 解析数据
list_foods = bs_foods.find_all('div',class_='info pure-u')
# 查找最小父级标签
listfoods = []
for a in list_foods:
    tag_a = a.find('a')
    # 提取第0个父级标签中的<a>标签
    #print(len(tag_a.text)-13)
    aa = tag_a.text[17:-13]
    # 输出菜名，使用[17:-13]切掉了多余的信息
    bb= 'http://www.xiachufang.com'+tag_a['href']
    # 输出URL

    foods = a.find('p', class_='ing ellipsis')

    foodss = foods.text[1:-1]
    listfoods.append([aa,bb,foodss])
    #print(foods.text[1:-1])
    print(bb)

#print(listfoods)