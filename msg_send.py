import requests
import json
from utils.wx_util import get_wx_token


wx_token = get_wx_token()

print(wx_token)

# json数据格式请求参数
data = {
  "touser": "oqUIZ0UjuMlhxsICr5qGULkGzLCQ", # 接收用户的openid
  "template_id": "GQ5WOJGSQrS9XqRKpu0iOnSLGFfWaquJCyGqPhX0N-8", # 模板id
  "page": "pages/index/index",
  "miniprogram_state":"formal",
  "lang":"zh_CN",
  "data": {
      "time1": {
          "value": "2021-08-01"
      },
      "thing2": {
          "value": "Python推送小程序订阅消息"
      },
      "thing3": {
          "value": "作为雅思写作考官我将根据您"
      }
  }
}

# 设置请求头
header = {'Content-Type': 'application/json'}
# 请求地址
url = f"https://api.weixin.qq.com/cgi-bin/message/subscribe/send?access_token={wx_token}"
# 请求体
response = requests.post(url, headers=header, data = json.dumps(data))
# 打印请求结果
print(response.text)
