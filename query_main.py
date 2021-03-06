#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： Administrator
# datetime： 2020/5/7 0007 上午 10:36 
# ide： PyCharm

from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import QtCore
from PyQt5.QtGui import QIcon
import sys
from query import Ui_Form
import requests
import json
import query_ico_rc
from urllib.parse import quote
from pyquery import PyQuery


class Window(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.set_window()
        self.question = ''


    def set_window(self):
        self.setWindowTitle('查题助手 v3.0.1')
        self.setMaximumSize(600, 300)
        self.setMinimumWidth(300)
        self.adjustSize()
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowIcon(QIcon(':/tou.ico'))
        self.addClipbordListener()

    def addClipbordListener(self):
        clipboard = QApplication.clipboard()
        clipboard.dataChanged.connect(self.shortcut_query)

    def onClipboradChanged(self):
        clipboard = QApplication.clipboard()
        text = clipboard.text()
        print(text)

    def click_query(self):
        text = self.lineEdit.text()
        self.question = text
        self.query()

    def shortcut_query(self):
        clipboard = QApplication.clipboard()
        self.question = clipboard.text()
        self.lineEdit.setText(self.question)
        self.query()

    def query(self):
        if self.question.strip() == '':
            self.textBrowser.setText('请输入问题哦！')
            return
        result = self.req(self.question)
        d_result = {}
        try:
            r_list = result.split('正确答案：')
            d_result = {
                'question': self.question,
                'answer': r_list[1].replace('\n', '')
            }
        except:
            d_result = {
                'question': 'error！ 无法查询哦，请重试',
                'answer': 'error！'
            }
        question = d_result['question']
        answer = d_result['answer']
        text = '问题:<h4>{}</h4>答案:<p style="color:red"><b>{}</b><p>'.format(question, answer)
        self.textBrowser.setText(text)

    @staticmethod
    def req(question='java'):
        url = 'http://www.yxykw.com/questions_my.jsp?user=null'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome'
                          '/85.0.4183.83Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        data = {
            'question': question.strip()
        }
        try:
            response = requests.post(url=url, data=data, headers=headers)
            pq = PyQuery(response.text)
            result = pq('.result_list div#answerNone0').text()
            return result.replace('解析： 暂无解析', '')
        except:
            return '{"tm": "请检查网络环境！", "da": "请检查网络环境！"}'


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())
