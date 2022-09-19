import os
import socket
import time
import timeit
import global_variables as gvar

def start_server(host, port):
    global server, server_is_online, init_authentication
    server_is_online = False
    
    server_sckt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_sckt.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_sckt.bind((host, port))
    server_sckt.listen()
    server, address = server_sckt.accept()

    init_authentication = False
    print(f'... Server iniciado na porta {port}.')

    server_is_online = True

def connect_client(host, port):
    global client, server_is_online, init_authentication
    time_limit = 20
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    for t in range(time_limit*2):
        time.sleep(0.5)
        try:
            client.connect((host, port))
            init_authentication = True
            print(f'... Cliente iniciado na porta {port}.')
            while not server_is_online:
                time.sleep(0.1)
            return init_authentication
        except:
            os.system(gvar.cleart) 
            dot_string = '.'*(t%3+1)
            print(f'({t//2}) Conectando {dot_string}')
    return

    print('\nTimeout.')
