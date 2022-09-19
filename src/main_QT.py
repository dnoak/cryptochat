import time
import threading
import sys
import connection
import chat
import user
import socket
import global_variables
from authentication import authenticate_A, authenticate_B
from PyQt5 import QtCore, QtGui, QtWidgets
import qt.mainQT as mainQT
import qt.chatQT as chatQT

class ChatWindow(QtWidgets.QMainWindow):
    def __init__(self, login, address, priKey, chat_address, token):
        super().__init__()
        self.ui = chatQT.Ui_ChatWindow()
        self.ui.setupUi(self)

        self.login = login
        self.address = address
        self.priKey = priKey
        self.chat_address = chat_address
        self.token = token

        self.ui.sendmessage_button.released.connect(self.send_message)
        self.ui.message_input.returnPressed.connect(self.send_message)

        self.friend_name = user.is_friend(self.login, self.chat_address)

        self.friend_chat = user.print_chat(self.login, self.friend_name)
        #print(self.friend_chat)

        print(self.friend_name, self.friend_chat)

        if self.friend_name is not None and self.friend_chat is not None:
            self.ui.chat_history.insertPlainText(''.join(self.friend_chat))
            self.ui.chat_history.moveCursor(QtGui.QTextCursor.End)

        self.end_chat = False
        self.time_0 = 0
        self.time_limit = 20

        self.current_chat = []

        threading.Thread(target = self.receive_message).start()
        threading.Thread(target = self.timeout_msg).start()
        
        self.end_chat = False

    def send_message(self):
        if not self.end_chat:
            text = self.ui.message_input.text()
            self.ui.message_input.clear()
            message = chat.send_msg(self.login, self.chat_address, self.token, text)
            self.time_0 = 0
            self.current_chat.append(message)
            self.ui.chat_history.insertPlainText(message)
            self.ui.chat_history.moveCursor(QtGui.QTextCursor.End)

    def receive_message(self):
        while not self.end_chat:
            message = chat.receive_msg(self.friend_name, self.token, self.priKey)
            if message is not None:
                self.time_0 = 0
                self.current_chat.append(message)
                self.ui.chat_history.insertPlainText(message)
                self.ui.chat_history.moveCursor(QtGui.QTextCursor.End)

    def timeout_msg(self):
        while not self.end_chat:
            time.sleep(1)
            print(f'{self.end_chat = }, {self.time_0}')
            if self.time_0 > self.time_limit:
                self.end_chat = True
                connection.client.shutdown(socket.SHUT_WR)
                connection.server.shutdown(socket.SHUT_WR)
                connection.client.close()
                connection.server.close()
                
                print('Chat encerrado.')
                user.save_chat(self.login, self.friend_name, self.current_chat)
                self.close()
            else:
                self.time_0 += 1

    def closeEvent(self, a0: QtGui.QCloseEvent):
        self.time_0 = self.time_limit + 1

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = mainQT.Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.login_button.released.connect(self.main_chat)
        self.ui.login_input.returnPressed.connect(self.main_chat)

        self.ui.create_user_button.released.connect(self.create_user)
    
    def main_chat(self):

        host = self.ui.host_input.text()
        port = int(self.ui.port2_input.text()), int(self.ui.port1_input.text())
        login = self.ui.login_input.text()
        #create_new_user = self.ui.create_user_box.checkState()
        
        address, priKey = user.login(login)
        threading.Thread(target=connection.start_server, args=('localhost', port[0])).start()
        init_authentication = connection.connect_client(host, port[1])

        if init_authentication:
            authentic, token, chat_address = authenticate_A(address, priKey)
        else:
            authentic, token, chat_address = authenticate_B(address, priKey)
        
        if authentic:
            self.chat_window = ChatWindow(login, address, priKey, chat_address, token)
            self.chat_window.show()
            self.hide()
        else:
            print('Chat não autenticado.')
    
    def create_user(self):
        login = self.ui.login_input.text()
        user.create(login)



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec())
