import requests
from bs4 import BeautifulSoup

url = 'https://www.zhihu.com/api/v4/members/zhang-jia-wei/articles?'
headers = { 'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36' }
params = {
	'include': 'data[*].comment_count,suggest_edit,is_normal,thumbnail_extra_info,thumbnail,can_comment,comment_permission,admin_closed_comment,content,voteup_count,created,updated,upvoted_followees,voting,review_info,is_labeled,label_info;data[*].author.badge[?(type=best_answerer)].topics',
    'offset': '10',
    'limit': '20',
    'sort_by': 'voteups',
}
res = requests.get(url,headers=headers, params=params)
#发起请求，将响应的结果赋值给变量res
print(res.status_code)
#print(res.text)