# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/postboy_ui_v1.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_postboy(object):
    def setupUi(self, postboy):
        postboy.setObjectName("postboy")
        postboy.resize(745, 444)
        self.horizontalLayout_main = QtWidgets.QHBoxLayout(postboy)
        self.horizontalLayout_main.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_main.setSpacing(5)
        self.horizontalLayout_main.setObjectName("horizontalLayout_main")
        self.frame_response = QtWidgets.QFrame(postboy)
        self.frame_response.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_response.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_response.setObjectName("frame_response")
        self.verticalLayout_response = QtWidgets.QVBoxLayout(self.frame_response)
        self.verticalLayout_response.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_response.setSpacing(5)
        self.verticalLayout_response.setObjectName("verticalLayout_response")
        self.label_method = QtWidgets.QLabel(self.frame_response)
        self.label_method.setAlignment(QtCore.Qt.AlignCenter)
        self.label_method.setObjectName("label_method")
        self.verticalLayout_response.addWidget(self.label_method)
        self.textEdit_response = QtWidgets.QTextEdit(self.frame_response)
        self.textEdit_response.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.textEdit_response.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.textEdit_response.setObjectName("textEdit_response")
        self.verticalLayout_response.addWidget(self.textEdit_response)
        self.horizontalLayout_main.addWidget(self.frame_response)
        self.frame_input = QtWidgets.QFrame(postboy)
        self.frame_input.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_input.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_input.setObjectName("frame_input")
        self.verticalLayout_input = QtWidgets.QVBoxLayout(self.frame_input)
        self.verticalLayout_input.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_input.setSpacing(5)
        self.verticalLayout_input.setObjectName("verticalLayout_input")
        self.frame_url = QtWidgets.QFrame(self.frame_input)
        self.frame_url.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_url.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_url.setObjectName("frame_url")
        self.horizontalLayout_domain = QtWidgets.QHBoxLayout(self.frame_url)
        self.horizontalLayout_domain.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_domain.setSpacing(5)
        self.horizontalLayout_domain.setObjectName("horizontalLayout_domain")
        self.label_domain = QtWidgets.QLabel(self.frame_url)
        self.label_domain.setObjectName("label_domain")
        self.horizontalLayout_domain.addWidget(self.label_domain)
        self.lineEdit_url = QtWidgets.QLineEdit(self.frame_url)
        self.lineEdit_url.setText("")
        self.lineEdit_url.setObjectName("lineEdit_url")
        self.horizontalLayout_domain.addWidget(self.lineEdit_url)
        self.verticalLayout_input.addWidget(self.frame_url)
        self.frame_params = QtWidgets.QFrame(self.frame_input)
        self.frame_params.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_params.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_params.setObjectName("frame_params")
        self.horizontalLayout_route = QtWidgets.QHBoxLayout(self.frame_params)
        self.horizontalLayout_route.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_route.setSpacing(5)
        self.horizontalLayout_route.setObjectName("horizontalLayout_route")
        self.label_route = QtWidgets.QLabel(self.frame_params)
        self.label_route.setObjectName("label_route")
        self.horizontalLayout_route.addWidget(self.label_route)
        self.lineEdit_params = QtWidgets.QLineEdit(self.frame_params)
        self.lineEdit_params.setObjectName("lineEdit_params")
        self.horizontalLayout_route.addWidget(self.lineEdit_params)
        self.verticalLayout_input.addWidget(self.frame_params)
        self.frame_token = QtWidgets.QFrame(self.frame_input)
        self.frame_token.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_token.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_token.setObjectName("frame_token")
        self.horizontalLayout_token = QtWidgets.QHBoxLayout(self.frame_token)
        self.horizontalLayout_token.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_token.setSpacing(5)
        self.horizontalLayout_token.setObjectName("horizontalLayout_token")
        self.label_token = QtWidgets.QLabel(self.frame_token)
        self.label_token.setObjectName("label_token")
        self.horizontalLayout_token.addWidget(self.label_token)
        self.lineEdit_token = QtWidgets.QLineEdit(self.frame_token)
        self.lineEdit_token.setObjectName("lineEdit_token")
        self.horizontalLayout_token.addWidget(self.lineEdit_token)
        self.verticalLayout_input.addWidget(self.frame_token)
        self.label_payload = QtWidgets.QLabel(self.frame_input)
        self.label_payload.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_payload.setAlignment(QtCore.Qt.AlignCenter)
        self.label_payload.setObjectName("label_payload")
        self.verticalLayout_input.addWidget(self.label_payload)
        self.textEdit_payload = QtWidgets.QTextEdit(self.frame_input)
        self.textEdit_payload.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.textEdit_payload.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.textEdit_payload.setObjectName("textEdit_payload")
        self.verticalLayout_input.addWidget(self.textEdit_payload)
        self.frame_button = QtWidgets.QFrame(self.frame_input)
        self.frame_button.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_button.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_button.setObjectName("frame_button")
        self.gridLayout_button = QtWidgets.QGridLayout(self.frame_button)
        self.gridLayout_button.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_button.setSpacing(5)
        self.gridLayout_button.setObjectName("gridLayout_button")
        self.pushButton_post = QtWidgets.QPushButton(self.frame_button)
        self.pushButton_post.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_post.setObjectName("pushButton_post")
        self.gridLayout_button.addWidget(self.pushButton_post, 0, 1, 1, 1)
        self.pushButton_get = QtWidgets.QPushButton(self.frame_button)
        self.pushButton_get.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_get.setObjectName("pushButton_get")
        self.gridLayout_button.addWidget(self.pushButton_get, 0, 0, 1, 1)
        self.pushButton_put = QtWidgets.QPushButton(self.frame_button)
        self.pushButton_put.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_put.setObjectName("pushButton_put")
        self.gridLayout_button.addWidget(self.pushButton_put, 1, 0, 1, 1)
        self.pushButton_delete = QtWidgets.QPushButton(self.frame_button)
        self.pushButton_delete.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_delete.setObjectName("pushButton_delete")
        self.gridLayout_button.addWidget(self.pushButton_delete, 1, 1, 1, 1)
        self.verticalLayout_input.addWidget(self.frame_button)
        self.horizontalLayout_main.addWidget(self.frame_input)

        self.retranslateUi(postboy)
        QtCore.QMetaObject.connectSlotsByName(postboy)

    def retranslateUi(self, postboy):
        _translate = QtCore.QCoreApplication.translate
        postboy.setWindowTitle(_translate("postboy", "POSTBOY"))
        self.label_method.setText(_translate("postboy", "METHOD"))
        self.label_domain.setText(_translate("postboy", "URL"))
        self.label_route.setText(_translate("postboy", "PARAMS"))
        self.label_token.setText(_translate("postboy", "TOKEN"))
        self.label_payload.setText(_translate("postboy", "PAYLOAD"))
        self.pushButton_post.setText(_translate("postboy", "POST"))
        self.pushButton_get.setText(_translate("postboy", "GET"))
        self.pushButton_put.setText(_translate("postboy", "PUT"))
        self.pushButton_delete.setText(_translate("postboy", "DELETE"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    postboy = QtWidgets.QWidget()
    ui = Ui_postboy()
    ui.setupUi(postboy)
    postboy.show()
    sys.exit(app.exec_())
