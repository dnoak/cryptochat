
import os
import socket
import time
import threading
import connection
import global_variables as gvar
import user
import main_QT
from timeit import default_timer as timer
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


def send_msg(login, received_address, token, sent_msg):
    #global time_0, msg_list
    encryptor = PKCS1_OAEP.new(received_address)
    
    #print(f'{token[0]},{token[1]}')
    if sent_msg.strip() == '':
        return #continue
    try:
        sent_msg_token = f'{token}:{sent_msg}'
        cryp_msg_friendKey = encryptor.encrypt(sent_msg_token.encode())
        connection.client.send(cryp_msg_friendKey)
        print('Enviou:', sent_msg, '\n')
        #time_0 = 0
        return f'{login}:{sent_msg}\n'
    except:
        return


def receive_msg(friend_name, token, priKey):
    decryptor = PKCS1_OAEP.new(priKey)
    try:
        received_crypt_msg = connection.server.recv(1024)
        decryp_msg = decryptor.decrypt(received_crypt_msg).decode()
        
        if decryp_msg.strip() != '':
            decryp_msg_token = decryp_msg.split(':',1)
            print('Certificado, autenticado e criptografado:', decryp_msg.split(':',1)[0] == token)
            print('Recebeu:', decryp_msg_token[1], '\n')

            if token == decryp_msg_token[0]:
                #time_0 = 0
                return f'{friend_name}: {decryp_msg_token[1]}\n'
    except:
        return

'''
def timeout_msg():
    global end_chat, time_0, msg_list
    msg_list = []
    end_chat = False
    time_0 = 0
    while not end_chat:
        time.sleep(1)
        print(time_0)
        if time_0 == 20:
            end_chat = True
            connection.client.close()
            connection.server.close()
            print('Chat encerrado')
            #print(msg_list)
        else:
            time_0 += 1

def start_chat(login, received_address):
    priKey = user.get_priKey(login)

    friend_name = user.is_friend(login, received_address)
    user.print_chat(login, friend_name)


    end_chat = threading.Thread(
        target = timeout_msg
        ).start()

    send_msg_thr = threading.Thread(
        target = send_msg, args=(login, received_address,)
        ).start()
    
    receive_msg_thr = threading.Thread(
        target = receive_msg, args=(friend_name, priKey,)
        ).start()
'''
    
    
    

