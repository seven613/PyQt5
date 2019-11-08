'''
解密函数
样例：
{
"key":"F2D8D966CD3D47788449C19D5EF2081B",
"params":"8DAD69F1A99DC5FD79FE9CB8D8FFD022499DDD6FCAEC433D690FACF545D8E49A"
}
{
"code": 0,
"message": "请求成功",
"result": "450422199206240849"
}
说明：key用之前下发给各个医院的秘钥
'''
import requests
import json

url = 'http://222.222.40.2:8098/api/deciphering'
payload=json.dumps(
    {
        'key':'893E64E8499D4AE0B466168AE26F6904',#给医院的密钥
        'params':'7450B4ACD7A767CF0E587FE9C641F62E528B6A3E30197713C1ABB7F7F542CA5E'#加密后的身份证号
    }
)
headers = {
    'Content-Type': "application/json"
    }

response = requests.request("POST", url, data=payload, headers=headers)
print(response.text)
msg = response.json()
if msg['code'] != 0:
    print(msg['message'])
else:
    print(msg['result'])