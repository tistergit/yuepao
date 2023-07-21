import hashlib
import requests
import config

def checkSignature(data):
    TOKEN = "tisteryu"
    signature = data.get('signature')
    timestamp = data.get('timestamp')
    nonce = data.get("nonce")
    if not signature or not timestamp or not nonce:
        return False
    tmp_str = "".join(sorted([TOKEN, timestamp, nonce]))
    tmp_str = hashlib.sha1(tmp_str.encode('UTF-8')).hexdigest()
    if tmp_str == signature:
        return True
    else:
        return False
    

def get_openid(code):
    appid = config.WX_APP_ID
    secret = config.WX_APP_SECRET
    url = 'https://api.weixin.qq.com/sns/jscode2session?appid=%s&secret=%s&js_code=%s&grant_type=%s'%(appid,secret,code,'authorization_code')
    res = requests.get(url)
    if res.status_code == 200 or res.status_code == 206:
        return res.text


def get_wx_token():
    APPID = config.WX_APP_ID
    APPSECRET = config.WX_APP_SECRET
    url = f'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={APPID}&secret={APPSECRET}'
    response = requests.get(url)
    data = response.json()
    access_token = data.get('access_token')
    return access_token
