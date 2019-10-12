'''
加密函数
'''

import requests
import json
url = "http://222.222.40.2:8098/api/encrypt"

payload=json.dumps(
    {
        'key':'893E64E8499D4AE0B466168AE26F6904',
        'params':'132930198111173014'
    }
)
headers = {
    'Content-Type': "application/json"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)