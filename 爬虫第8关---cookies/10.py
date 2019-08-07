import requests,json

userid = str(1)

apikey = str('fbf0e27020b44c4ba5f56b621b4e8aaa')

def robot(content):
    api = r'http://openapi.tuling123.com/openapi/api/v2'
    data = {
        "perception": {
            "inputText": {
                "text": content
                            }
                        },
        "userInfo": {
                    "apiKey": apikey,
                    "userId": userid,
                    }
    }

    # 转化为json格式
    datajson = json.dumps(data)
    # 发起POST请求
    response = requests.post(api,data=datajson)
    # 将返回的json数据解码
    res = json.loads(response.content)
    print(res['results'][0]['values']['text'])

# for x in range(10):
#     content = input('talk:')
#     robot(content)
#     if x == 10:
#         break


while True:
    content = input('talk:')
    robot(content)
    if content == 'bye':
        break