'''
签名函数
1）head签名样例：
{
	"key": "893e64e8499d4ae0b466168ae26f6904",
	"body": {
		"appId": "bb9077b5bed64924a36e9e4eee515c9a",
		"nonceStr": ".88357776802397576516672734238763958247",
		"orgCode": "LDWLYXGS",
		"timestamp": "1541816252.000000000000000000000000000004",
		"version": "V1.0.2"
	}
}
返回：
{
"code": 0,
"message": "请求成功",
"result": "c8eea95b423f3450c766270377616c5d"
}
2）body签名样例：
{
	"key": "893e64e8499d4ae0b466168ae26f6904",
 "body": {
        "qrCode": "3E3CD944076BBF60BD028DC26954B22B130FB3E42993016C2D205A5F31FB0B33:0:07EDF114B1651BA63D112011E74C1EC3",
        "medStepCode": "000000",
        "terminalCode": "hhqy001",
        "appMode": "2"
    }
}
返回
{
    "code": 0,
    "message": "请求成功",
    "result": "9489242505fd8fa36ad12efe9311f5b7"
}
说明：key用之前下发给各个医院的秘钥
'''

import requests
import json
import time
import random
def sign(params):

    url = 'http://222.222.40.2:8098/api/sign'
    payload=json.dumps(params)
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

def sortedDict(d):
    data={}
    for k in sorted(d):
        data[k]=d[k]
    return data



# data ={
#     "method":"getPersonInfo",# 方法名称	AN..50	Y 不签名例：getPersonInfo
#     "headSign":"3a0e580d9bc9f0c3cdd62f91fc3a075f",
#     "bodySign":"f10cd9f4dcf23d98a1980210f95a3001",
#     "orgCode":self.__orgcode,# 机构唯一识别码	AN..36	Y 由卡管系统分配
#     "version":"V1.0.6",# 接口版本号	AN..10	Y同文档版本号
#                 "appId":self.__appid,# 应用唯一识别码	AN..36	Y 由卡管系统分配
#                 "nonceStr":random.randint(0,99999999999999999),# 随机数	AN..32	Y小于16 位的整数
#                 "timestamp":time.time(),# 请求时间戳	AN..32	Y、加密当前秒数，与标准时间一致
#                 "signMode":"MD5",
#                 "encryptMode":"DESede/ECB/ZeroBytePadding",
#                 "signature": "",
#                 "body":{
#                     "idCardTypeCode":"01",
#                     "idCode":self.encrypt("132430198111173014"),
#                     "appMode":"2"
#                     }
#            }
headData ={
            "key": "893E64E8499D4AE0B466168AE26F6904",
            "body": {
                "appId": "bb9077b5bed64924a36e9e4eee515c9a",
                "nonceStr": random.randint(0,99999999),
                "orgCode": "5a679bf2129541cf84596fa11835608c",
                "timestamp": time.time(),
                "version": "V1.0.6"
            }
        }
print(sortedDict(headData))

#print(type(sorted(headData.items(),key=lambda headData:headData[1])))
#sign(headData)