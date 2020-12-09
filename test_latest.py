#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： moddemod
# datetime： 2020/10/28 0028 下午 9:49 
# ide： PyCharm

import requests
from urllib.parse import quote, unquote

# token = 'PqOxtkakjXDHWlCk'
# url = 'http://cx.icodef.com/wyn-nb'
# headers = {
#     'Content-type': 'application/x-www-form-urlencoded',
#     'Authorization': token,
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome'
#                   '/85.0.4183.83Safari/537.36'
# }

# question = '【多选题】中国古建筑中墙转角的石柱作用是()。'
# data = 'question=' + quote(question)
# response = requests.post(url=url, headers=headers, data=data)
# print(response.text)
#  {"code":1,"data":"石雕龙柱"}
#  {"code":1,"data":"装饰#实用保护"}


question = '《中共中央关于坚持和完善中国特色社会主义制度、推进国家治理体系和治理能力现代化若干重大问题的决定》指出，要构建区域协调发展新机制，形成（ ）明显、优势互补、高质量发展的区域经济布局。'
url = 'http://api.xmlm8.com/tp/tk.php?t=' + question
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome'
                  '/85.0.4183.83Safari/537.36'
}
response = requests.get(url=url, headers=headers)
print(response.text)
# {"title":"《中共中央关于坚持和完善中国特色社会主义制度、推进国家治理体系和治理能力现代化若干重大问题的决定》指出，要构建区域协调发展新机制，形成（ ）明显、优势互补、高质量发展的区域经济布局\n\n\n","answer":"主体功能\n\n","code":1}