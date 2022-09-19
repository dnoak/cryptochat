# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainQT.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(308, 396)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("font: 12pt \"FreeMono\"; ")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("font: 13pt \"FreeMono\";\n"
"background-color: rgb(0, 0, 0);\n"
"color: rgb(78, 154, 6);\n"
"border-color: rgb(92, 53, 102);\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("FreeMono")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("FreeMono")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_2.setLineWidth(1)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.host_input = QtWidgets.QLineEdit(self.frame)
        self.host_input.setEnabled(True)
        self.host_input.setAutoFillBackground(False)
        self.host_input.setStyleSheet("background-color: rgb(78, 154, 6);\n"
"color: rgb(0, 0, 0);")
        self.host_input.setObjectName("host_input")
        self.verticalLayout_2.addWidget(self.host_input)
        self.label_3 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("FreeMono")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.port2_input = QtWidgets.QLineEdit(self.frame)
        self.port2_input.setStyleSheet("background-color: rgb(78, 154, 6);\n"
"color: rgb(0, 0, 0);")
        self.port2_input.setObjectName("port2_input")
        self.verticalLayout_2.addWidget(self.port2_input)
        self.label_4 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("FreeMono")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.port1_input = QtWidgets.QLineEdit(self.frame)
        self.port1_input.setStyleSheet("background-color: rgb(78, 154, 6);\n"
"color: rgb(0, 0, 0);")
        self.port1_input.setObjectName("port1_input")
        self.verticalLayout_2.addWidget(self.port1_input)
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.login_input = QtWidgets.QLineEdit(self.frame)
        font = QtGui.QFont()
        font.setFamily("FreeMono")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.login_input.setFont(font)
        self.login_input.setStyleSheet("background-color: rgb(78, 154, 6);\n"
"color: rgb(0, 0, 0);")
        self.login_input.setDragEnabled(False)
        self.login_input.setClearButtonEnabled(False)
        self.login_input.setObjectName("login_input")
        self.verticalLayout_2.addWidget(self.login_input)
        self.login_button = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setFamily("FreeMono")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.login_button.setFont(font)
        self.login_button.setObjectName("login_button")
        self.verticalLayout_2.addWidget(self.login_button)
        self.create_user_button = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setFamily("FreeMono")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.create_user_button.setFont(font)
        self.create_user_button.setObjectName("create_user_button")
        self.verticalLayout_2.addWidget(self.create_user_button)
        self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 308, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#4e9a06;\">CryptoChat</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#4e9a06;\">Host</span></p></body></html>"))
        self.host_input.setText(_translate("MainWindow", "localhost"))
        self.label_3.setText(_translate("MainWindow", "Porta Client"))
        self.port2_input.setText(_translate("MainWindow", "5050"))
        self.label_4.setText(_translate("MainWindow", "Porta Server"))
        self.port1_input.setText(_translate("MainWindow", "5051"))
        self.label_5.setText(_translate("MainWindow", "Usuário"))
        self.login_input.setText(_translate("MainWindow", "daniel"))
        self.login_button.setText(_translate("MainWindow", "Login"))
        self.create_user_button.setText(_translate("MainWindow", "Criar usuário"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
