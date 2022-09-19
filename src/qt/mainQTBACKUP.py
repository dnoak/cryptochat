# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainQT.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import os
import time
import threading
from authentication import authenticate_A, authenticate_B
import global_variables as gvar
import connection
import chat
import user

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(600, 720)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.login_button = QtWidgets.QPushButton(self.centralwidget)
        self.login_button.setGeometry(QtCore.QRect(220, 510, 161, 31))
        font = QtGui.QFont()
        font.setFamily("FreeMono")
        self.login_button.setFont(font)
        self.login_button.setObjectName("login_button")
        self.login_input = QtWidgets.QLineEdit(self.centralwidget)
        self.login_input.setGeometry(QtCore.QRect(220, 440, 161, 31))
        font = QtGui.QFont()
        font.setFamily("FreeMono")
        font.setPointSize(14)
        self.login_input.setFont(font)
        self.login_input.setText("")
        self.login_input.setDragEnabled(False)
        self.login_input.setClearButtonEnabled(False)
        self.login_input.setObjectName("login_input")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(200, 130, 211, 81))
        font = QtGui.QFont()
        font.setFamily("FreeMono")
        font.setPointSize(25)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.create_user_box = QtWidgets.QCheckBox(self.centralwidget)
        self.create_user_box.setGeometry(QtCore.QRect(240, 480, 121, 23))
        self.create_user_box.setObjectName("create_user_box")
        self.host_input = QtWidgets.QLineEdit(self.centralwidget)
        self.host_input.setGeometry(QtCore.QRect(130, 330, 113, 25))
        self.host_input.setObjectName("host_input")
        self.port1_input = QtWidgets.QLineEdit(self.centralwidget)
        self.port1_input.setGeometry(QtCore.QRect(250, 330, 113, 25))
        self.port1_input.setObjectName("port1_input")
        self.port2_input = QtWidgets.QLineEdit(self.centralwidget)
        self.port2_input.setGeometry(QtCore.QRect(370, 330, 113, 25))
        self.port2_input.setObjectName("port2_input")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(170, 310, 31, 17))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(260, 310, 91, 17))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(380, 310, 91, 17))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(270, 420, 61, 17))
        self.label_5.setObjectName("label_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.login_button.released.connect(self.login)
        self.login_input.returnPressed.connect(self.login)
    
    def login(self):
        host = self.host_input.text()
        port = int(self.port2_input.text()), int(self.port1_input.text())
        user_login = self.login_input.text()
        create_new_user = self.create_user_box.checkState()
        
        
        address, priKey = user.login(user_login)
        threading.Thread(target=connection.start_server, args=(host, port[0])).start()
        connection.connect_client(host, port[1])

        if connection.init_authentication:
            authentic, token, chat_address = authenticate_A(address, priKey)
        else:
            authentic, token, chat_address = authenticate_B(address, priKey)

        if authentic:
            chat.start_chat(user_login, chat_address)
            self.chat_gui()
        else:
            print('Chat não autenticado.')
                
    
    def chat_gui(self):
        print('123232444')
        chat_screen = ChatScreen()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.login_button.setText(_translate("MainWindow", "Login"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">CryptoChat</p></body></html>"))
        self.create_user_box.setText(_translate("MainWindow", "Novo usuário"))
        self.host_input.setText(_translate("MainWindow", "localhost"))
        self.port1_input.setText(_translate("MainWindow", "5051"))
        self.port2_input.setText(_translate("MainWindow", "5050"))
        self.label_2.setText(_translate("MainWindow", "Host"))
        self.label_3.setText(_translate("MainWindow", "Porta Client"))
        self.label_4.setText(_translate("MainWindow", "Porta Server"))
        self.label_5.setText(_translate("MainWindow", "Usuário"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
