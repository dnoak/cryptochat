import os
import socket
import connection
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


class colors:
    GREEN = '\033[1;30;42m'
    BLUE = '\033[1;37;44m'
    GREY = '\033[0;30;47m'
    RED = '\033[0;37;41m'
    YELL = '\033[1;30;43m'
    END = '\033[0m'

def authenticate_B(address, priKey):
    # C = client
    # S = server
    # 🔑 = private key
    # 🔒 = public key
    # 📜 = token 


    # criando S🔑, S🔒, S📜  
    # address = address
    priKey_B = PKCS1_OAEP.new(priKey)
    address_B = address.export_key()
    token_B = os.urandom(10).hex()
    print(f'\n\n{colors.GREY} Token: {token_B}{colors.END}')


    # recebendo C🔒
    print(f'\n\n{colors.GREEN}Recebeu - C🔒:{colors.END}')
    address_A = RSA.import_key(connection.server.recv(2048))
    print(address_A.export_key())


    # enviando S🔒, C🔒(S📜)
    print(f'\n\n{colors.BLUE}Enviou - S🔒, C🔒(S📜):{colors.END}')
    encryptor = PKCS1_OAEP.new(address_A)
    cryptoken_B = encryptor.encrypt(token_B.encode())
    connection.client.send(address_B)
    connection.client.send(cryptoken_B)
    print(address_B,'\n')
    print(cryptoken_B)


    # recebendo S🔒(C📜, S📜)
    print(f'\n\n{colors.GREEN}Recebeu - S🔒(C📜, S📜):{colors.END}')
    cryptoken_A_B = connection.server.recv(2048)
    print(cryptoken_A_B)
    
    decryptoken_A_B = priKey_B.decrypt(cryptoken_A_B)
    decryptoken_A_B = decryptoken_A_B.decode().split(',')
    decryptoken_A = decryptoken_A_B[0]
    decryptoken_B = decryptoken_A_B[1]


    # enviando C🔒(C📜)
    encryptor = PKCS1_OAEP.new(address_A)
    cryptoken_A = encryptor.encrypt(decryptoken_A.encode())

    connection.client.send(cryptoken_A)
    print(f'\n\n{colors.BLUE}Enviou - C🔒(C📜):{colors.END}')
    print(cryptoken_A)
    

    # Autenticação
    if decryptoken_B == token_B:
        print(f'\n\n{colors.GREY}Usuário autenticado.{colors.END}\n')
        return True, ''.join(sorted([token_B, decryptoken_A])), address_A

    print(f'\n\n{colors.RED}Usuário NÃO autenticado.{colors.END}\n')
    connection.client.close()
    return False



def authenticate_A(address, priKey):
    # C = client
    # S = server
    # 🔑 = private key
    # 🔒 = public key
    # 📜 = token 


    # criando C🔑, C🔒, C📜  
    # address = address
    priKey_A = PKCS1_OAEP.new(priKey)
    address_A = address
    token_A = os.urandom(10).hex()
    print(f'\n\n{colors.GREY} Token: {token_A}')


    # enviando C🔒
    print(f'\n\n{colors.BLUE}Enviou - C🔒:{colors.END}')
    connection.client.send(address_A.exportKey())
    print(address_A.exportKey())
    

    # recebendo S🔒, C🔒(S📜)
    print(f'\n\n{colors.GREEN}Recebeu - S🔒, C🔒(S📜):{colors.END}')
    address_B = RSA.import_key(connection.server.recv(2048))
    cryptoken_B = connection.server.recv(2048)

    print(address_B.export_key(), '\n')
    print(cryptoken_B)
    
    
    # enviando S🔒(C📜 , S📜)
    print(f'\n\n{colors.BLUE}Enviou - S🔒(C📜 , S📜):{colors.END}')

    decryptoken_B = priKey_A.decrypt(cryptoken_B).decode()
    token_string = f'{token_A},{decryptoken_B}'

    encryptor = PKCS1_OAEP.new(address_B)
    cryptoken_A_B = encryptor.encrypt(token_string.encode())
    connection.client.send(cryptoken_A_B)
    
    print(cryptoken_A_B)



    # recebendo C🔒(C📜)
    print(f'\n\n{colors.GREEN}Recebeu - C🔒(C📜):{colors.END}')
    cryptoken_A = connection.server.recv(2048)
    decryptoken_A = priKey_A.decrypt(cryptoken_A).decode()
    print(cryptoken_A)


    # Autenticação
    if decryptoken_A == token_A:
        print(f'\n\n{colors.GREY}Usuário autenticado.{colors.END}\n')
        return True, ''.join(sorted([token_A, decryptoken_B])), address_B
    else:
        print(f'\n\n{colors.RED}Usuário NÃO autenticado.{colors.END}\n')
        connection.client.close()
        return False


