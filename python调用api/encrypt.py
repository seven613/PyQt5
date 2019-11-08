'''
加密函数
样例：
{
"key":"F2D8D966CD3D47788449C19D5EF2081B",
"params":"450422199206240849"
}
{
"code": 0,
"message": "请求成功",
"result": "8DAD69F1A99DC5FD79FE9CB8D8FFD022499DDD6FCAEC433D690FACF545D8E49A"
}
说明：key用之前下发给各个医院的秘钥
'''

import requests
import json
url = "http://222.222.40.2:8098/api/encrypt"

payload=json.dumps(
    {
        'key':'893E64E8499D4AE0B466168AE26F6904',#给医院的密钥
        'params':'132930198111173014'#加密后的身份证号
    }
)
headers = {
    'Content-Type': "application/json"#请求的头信息必须标明是json格式
    }

response = requests.request("POST", url, data=payload, headers=headers)#一定要调用POST方法，否则无法获取数据
print(response.text)
msg = response.json()
if msg['code'] != 0:
    print(msg['message'])
else:
    print(msg['result'])