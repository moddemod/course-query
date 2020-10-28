#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： moddemod
# datetime： 2020/10/28 0028 下午 9:49 
# ide： PyCharm

import requests
from urllib.parse import quote, unquote

token = 'PqOxtkakjXDHWlCk'
url = 'http://cx.icodef.com/wyn-nb'
headers = {
    'Content-type': 'application/x-www-form-urlencoded',
    'Authorization': token,
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome'
                  '/85.0.4183.83Safari/537.36'
}

question = '【多选题】中国古建筑中墙转角的石柱作用是()。'
data = 'question=' + quote(question)
response = requests.post(url=url, headers=headers, data=data)
print(response.text)
#  {"code":1,"data":"石雕龙柱"}
#  {"code":1,"data":"装饰#实用保护"}
