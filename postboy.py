import os
import json
import time
import requests
import datetime
from PyQt5 import QtWidgets, QtCore
from postboy_ui import Ui_postboy

class Postboy_window(QtWidgets.QWidget,Ui_postboy):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        self.url = str()

        # buttons event
        self.pushButton_post.clicked.connect(self.post)
        self.pushButton_get.clicked.connect(self.get)
        self.pushButton_put.clicked.connect(self.put)
        self.pushButton_delete.clicked.connect(self.delete)

        # 設定快捷鍵
        self.pushButton_post.setShortcut('Ctrl+Return')  # Mac Command + retrun
        self.pushButton_get.setShortcut('Meta+Return')  # Mac retrun
        self.pushButton_put.setShortcut('Ctrl+R')  # Mac Command + r
        self.pushButton_delete.setShortcut('Ctrl+D')  # Mac fn + delete

    def _get_params(self):
        params = self.lineEdit_params.text()
        if params.startswith('{') and params.endswith('}'):
            return json.loads(params)
        if params.startswith('?'):
            param_list = params.lstrip('?').split('&')
            results = dict()
            for param in param_list:
                attr = param.split('=')
                if len(attr) != 2:
                    continue
                results.update({attr[0]: attr[1]})
            if 'token' not in results:
                results.update({'token': self.lineEdit_token.text() or None})
            return results
        return dict()

    def _get_url(self):
        url = self.lineEdit_url.text()
        if not url:
            return url
        return url if url.startswith('https://') else f'https://{url}'

    def _display_response(self, response):
        if not response.text:
            return None
        try:
            data = json.loads(response.text)
            result = json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False)
        except Exception as e:
            result = str(e)
        self.textEdit_response.setText(result)

    # user interact
    def get(self):
        self.label_method.setText('[GET]')
        url = self._get_url()
        if not url:
            return None
        params = self._get_params()
        response = requests.get(url, params=params)
        if response.status_code != requests.codes.ok:
            return None
        self._display_response(response)

    def post(self):
        self.label_method.setText('[POST]')
        url = self._get_url()
        if not url:
            return None
        params = self._get_params()
        payload = self.textEdit_payload.toPlainText()
        if not payload:
            response = requests.post(url, params=params)
        else:
            try:
                data = json.loads(payload)
            except Exception as e:
                print(f'{e}, {payload}')
                data = None
            response = requests.post(url, params=params, data=data)
        if response.status_code != requests.codes.ok:
            return None
        self._display_response(response)

    def put(self):
        self.label_method.setText('[PUT]')

    def delete(self):
        choice = QtWidgets.QMessageBox.question(
                    self, 'DELETE', 'DELETE',
                    QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)

        if choice == QtWidgets.QMessageBox.Yes:
            self.label_method.setText('[DELETE]')

