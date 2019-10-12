import requests
import json

url = "http://222.222.40.2:8098/api/do"#url
parms

headers =json.dumps(
    {
        "method": "getPersonInfo",
        "headSign": "893e64e8499d4ae0b466168ae26f6904",
        "bodySign": "f10cd9f4dcf23d98a1980210f95a3001",
        "orgCode": "5a679bf2129541cf84596fa11835608c",
        "version": "V1.0.6",
        "appId": "bb9077b5bed64924a36e9e4eee515c9a",
        "nonceStr": "122685614345641657",
        "timestamp": "60C90F3B796B41878B8D9C393E2B6329",
        "signMode": "MD5",
        "encryptMode": "DESede/ECB/ZeroBytePadding",
        "signature": "304502201368C6FF4A228EBFBE22741EBBE71D27D32DBA9E79291E99D03B42E2BC3553FD022100EBF0559D4C40D05651D015C7EE04756C1E999D2727DD86757C3775FFB5762912",
        "body": {
            "erhcCardNo": "3D06CB522786C96739459300C8DED9AB14805A17ABD46B79",
            "appMode": "2"
        }
    }

)

response = requests.post(url,headers)

print(response.text)
