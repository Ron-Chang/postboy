import os
import time
import datetime
from PyQt5 import QtWidgets,QtCore
from postboy_ui import Ui_postboy

class Postboy_window(QtWidgets.QWidget,Ui_postboy):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        # connect buttons
        self.pushButton_post.clicked.connect(self.post)
        self.pushButton_get.clicked.connect(self.get)
        self.pushButton_put.clicked.connect(self.put)
        self.pushButton_delete.clicked.connect(self.delete)

        # 設定快捷鍵
        # Mac Command + retrun
        self.pushButton_post.setShortcut("Ctrl+Return")
        # Mac retrun
        self.pushButton_get.setShortcut("Meta+Return")
        # Mac Command + r
        self.pushButton_put.setShortcut("Ctrl+R")
        # Mac fn + delete
        self.pushButton_delete.setShortcut("Ctrl+D")

    def get_timestamp():
        return int(time.mktime(datetime.datetime.now().timetuple()))

    def execute(self, request):

        cmd = ["curl","-X"]+request
        cmd = " ".join([i for i in cmd])
        response = os.popen(cmd).read()
        self.textEdit_response.setText(response)

    # user interact
    def post(self):
        #METHOD
        self.label_method.setText("[POST]")
        method = ["POST"]

        # URI
        if self.lineEdit_domain.text():
            uri = [f"{self.lineEdit_domain.text()}{self.lineEdit_route.text()}"]
        else:
            uri = []
            print("ERROR: Invalid URI") # 插入ERROR CODE

        # HEADER
        if self.lineEdit_token.text():
            header = ["-H Content-Type:application/json"]
            header += [f"-H Authorization:{self.lineEdit_token.text()}"]
        else:
            header = []

        #BODY
        if self.textEdit_body.toPlainText():
            body = [f"-d '{self.textEdit_body.toPlainText()}'"]
            request = method+uri+header+body
            self.execute(request)
        else:
            body = []
            print("ERROR")


    def get(self):
        #METHOD
        self.label_method.setText("[GET]")
        method = ["GET"]

        # URI
        if self.lineEdit_domain.text():
            uri = [f"{self.lineEdit_domain.text()}{self.lineEdit_route.text()}"]
        else:
            uri = []
            print("ERROR: Invalid URI") # 插入ERROR CODE

        # HEADER
        if self.lineEdit_token.text():
            header = ["-H Content-Type:application/json"]
            header += [f"-H Authorization:{self.lineEdit_token.text()}"]
        else:
            header = []

        request = method+uri+header
        self.execute(request)

    def put(self):
        #METHOD
        self.label_method.setText("[PUT]")
        method = ["PUT"]

        # URI
        if self.lineEdit_domain.text():
            uri = [f"{self.lineEdit_domain.text()}{self.lineEdit_route.text()}"]
        else:
            uri = []
            print("ERROR: Invalid URI") # 插入ERROR CODE

        # HEADER
        if self.lineEdit_token.text():
            header = ["-H Content-Type:application/json"]
            header += [f"-H Authorization:{self.lineEdit_token.text()}"]
        else:
            header = []

        #BODY
        if self.textEdit_body.toPlainText():
            body = [f"-d '{self.textEdit_body.toPlainText()}'"]
            request = method+uri+header+body
            self.execute(request)
        else:
            body = []
            print("ERROR")

    def delete(self):
        choice = QtWidgets.QMessageBox.question(
                    self, "DELETE",
                    "DELETE",
                    QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)

        if choice == QtWidgets.QMessageBox.Yes:
            #METHOD
            self.label_method.setText("[DELETE]")
            method = ["DELETE"]

            # URI
            if self.lineEdit_domain.text():
                uri = [f"{self.lineEdit_domain.text()}{self.lineEdit_route.text()}"]
            else:
                uri = []
                print("ERROR: Invalid URI") # 插入ERROR CODE

            # HEADER
            if self.lineEdit_token.text():
                header = ["-H Content-Type:application/json"]
                header += [f"-H Authorization:{self.lineEdit_token.text()}"]
            else:
                header = []

            #BODY
            if self.textEdit_body.toPlainText():
                body = [f"-d '{self.textEdit_body.toPlainText()}'"]
                request = method+uri+header+body
                self.execute(request)
            else:
                body = []
                print("ERROR")


# if __name__ == "__main__":
#     import main
#     main.app()
