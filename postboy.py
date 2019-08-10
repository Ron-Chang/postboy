import os
import time
from ast import literal_eval
import datetime
from errors import NotFoundError, ValidationError
from error_code import ErrorCodeDefine
from PyQt5 import QtWidgets,QtCore
from postboy_ui import Ui_postboy

class Postboy_window(QtWidgets.QWidget,Ui_postboy):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        # buttons event
        self.pushButton_post.clicked.connect(self.post)
        self.pushButton_get.clicked.connect(self.get)
        self.pushButton_put.clicked.connect(self.put)
        self.pushButton_delete.clicked.connect(self.delete)

        # 設定快捷鍵
        self.pushButton_post.setShortcut("Ctrl+Return")  # Mac Command + retrun
        self.pushButton_get.setShortcut("Meta+Return")  # Mac retrun
        self.pushButton_put.setShortcut("Ctrl+R")  # Mac Command + r
        self.pushButton_delete.setShortcut("Ctrl+D")  # Mac fn + delete

    # @staticmethod
    def _get_timestamp(self):
        return int(time.mktime(datetime.datetime.now().timetuple()))

    def _get_data(self, method):

        #METHOD
        self.method = f"-X {method}"
        # URI
        if self.lineEdit_domain.text():
            self.uri = f"{self.lineEdit_domain.text()}{self.lineEdit_route.text()}?t={str(self._get_timestamp())}"
        else:
            self.uri = ""
            print("INVALID DOMAIN!")
        # HEADER
        if self.lineEdit_token.text():
            self.header = "-H Content-Type:application/json "
            self.header += f"-H Authorization:{self.lineEdit_token.text()}"
        else:
            self.header = ""
            print("INVALID TOKEN!")
        #BODY
        if self.textEdit_body.toPlainText():
            self.body = f"-d '{self.textEdit_body.toPlainText()}'"
        else:
            self.body = ""

        data = {"method":self.method,
                "uri":self.uri,
                "header":self.header,
                "body":self.body,
                }

        self._exec(data)

    def _exec(self, data):

        if data["uri"]:
            data_list = [d for d in list(data.values()) if d != ""]
            requests = ["curl"]
            requests += data_list
            cmd = " ".join([request for request in requests])
            response = os.popen(cmd).read()
            self.textEdit_response.setText(response)
            if data["method"] == "-X POST" and "login" in data["uri"]:
                try:
                    token = literal_eval(response)["data"]["session"]
                    self.lineEdit_token.setText(token)
                except:
                    print("ERROR")
        else:
            print("NO DOMAIN")

    # user interact
    def post(self):
        #METHOD
        self.label_method.setText("[POST]")
        method = "POST"
        self._get_data(method)

    def get(self):
        #METHOD
        self.label_method.setText("[GET]")
        method = "GET"
        self._get_data(method)

    def put(self):
        #METHOD
        self.label_method.setText("[PUT]")
        method = "PUT"
        self._get_data(method)

    def delete(self):
        choice = QtWidgets.QMessageBox.question(
                    self, "DELETE",
                    "DELETE",
                    QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)

        if choice == QtWidgets.QMessageBox.Yes:
            #METHOD
            self.label_method.setText("[DELETE]")
            method = "DELETE"
            self._get_data(method)
