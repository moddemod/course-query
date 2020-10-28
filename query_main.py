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


class Window(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.set_window()
        self.question = ''


    def set_window(self):
        self.setWindowTitle('查题助手--moddemod')
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
        print(result)
        try:
            r_json = json.loads(result)
            print(r_json)
        except:
            r_json = {
                'tm': '服务器有问题！'
            }

        question = self.question
        try:
            question_select = ''
        except:
            question_select = ''
        try:
            answer = r_json['data']
        except:
            answer = ''
        text = '问题:<h4>{}<br>{}</h4>答案:<p style="color:red"><b>{}</b><p>'.format(question, question_select, answer)
        self.textBrowser.setText(text)

    @staticmethod
    def req(question='java'):
        token = 'PqOxtkakjXDHWlCk'
        headers = {
            'Content-type': 'application/x-www-form-urlencoded',
            'Authorization': token,
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome'
                          '/85.0.4183.83Safari/537.36'
        }
        url = 'http://cx.icodef.com/wyn-nb'
        data = 'question=' + quote(question)
        try:
            res = requests.post(url=url, data=data, headers=headers)
            return res.text
        except:
            return '{"tm": "请检查网络环境！", "da": "请检查网络环境！"}'


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())
