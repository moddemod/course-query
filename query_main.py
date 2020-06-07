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
        r_json = json.loads(result)

        question = r_json['tm']
        try:
            question_select = r_json['xx']
        except:
            question_select = ''
        try:
            answer = r_json['da'].replace('关注公众号【花开校园】', '')
        except:
            answer = ''
        text = '问题:<h4>{}<br>{}</h4>答案:<p style="color:red"><b>{}</b><p>'.format(question, question_select, answer)
        self.textBrowser.setText(text)

    @staticmethod
    def req(question='java'):
        requests.get(url='https://xcx.fm210.cn/api/chunshuchati/api/ajax.php?type=qd&openid=ocgIw5TSj8f1JmALChj5N_mzDt3c')
        url = 'https://xcx.fm210.cn/api/chunshuchati/api/ajax.php?type=getda'
        data = 'openid=ocgIw5TSj8f1JmALChj5N_mzDt3c&w=' + quote(question.replace(" ", '').replace('\n', ''))
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8',
        }
        try:
            res = requests.post(url=url, data=data, headers=headers)
            return res.text
        except:
            return '{"tm": "请检查网络环境！", "da": "请检查网络环境！"}'


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())
