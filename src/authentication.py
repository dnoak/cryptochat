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
    # π = private key
    # π = public key
    # π = token 


    # criando Sπ, Sπ, Sπ  
    # address = address
    priKey_B = PKCS1_OAEP.new(priKey)
    address_B = address.export_key()
    token_B = os.urandom(10).hex()
    print(f'\n\n{colors.GREY} Token: {token_B}{colors.END}')


    # recebendo Cπ
    print(f'\n\n{colors.GREEN}Recebeu - Cπ:{colors.END}')
    address_A = RSA.import_key(connection.server.recv(2048))
    print(address_A.export_key())


    # enviando Sπ, Cπ(Sπ)
    print(f'\n\n{colors.BLUE}Enviou - Sπ, Cπ(Sπ):{colors.END}')
    encryptor = PKCS1_OAEP.new(address_A)
    cryptoken_B = encryptor.encrypt(token_B.encode())
    connection.client.send(address_B)
    connection.client.send(cryptoken_B)
    print(address_B,'\n')
    print(cryptoken_B)


    # recebendo Sπ(Cπ, Sπ)
    print(f'\n\n{colors.GREEN}Recebeu - Sπ(Cπ, Sπ):{colors.END}')
    cryptoken_A_B = connection.server.recv(2048)
    print(cryptoken_A_B)
    
    decryptoken_A_B = priKey_B.decrypt(cryptoken_A_B)
    decryptoken_A_B = decryptoken_A_B.decode().split(',')
    decryptoken_A = decryptoken_A_B[0]
    decryptoken_B = decryptoken_A_B[1]


    # enviando Cπ(Cπ)
    encryptor = PKCS1_OAEP.new(address_A)
    cryptoken_A = encryptor.encrypt(decryptoken_A.encode())

    connection.client.send(cryptoken_A)
    print(f'\n\n{colors.BLUE}Enviou - Cπ(Cπ):{colors.END}')
    print(cryptoken_A)
    

    # AutenticaΓ§Γ£o
    if decryptoken_B == token_B:
        print(f'\n\n{colors.GREY}UsuΓ‘rio autenticado.{colors.END}\n')
        return True, ''.join(sorted([token_B, decryptoken_A])), address_A

    print(f'\n\n{colors.RED}UsuΓ‘rio NΓO autenticado.{colors.END}\n')
    connection.client.close()
    return False



def authenticate_A(address, priKey):
    # C = client
    # S = server
    # π = private key
    # π = public key
    # π = token 


    # criando Cπ, Cπ, Cπ  
    # address = address
    priKey_A = PKCS1_OAEP.new(priKey)
    address_A = address
    token_A = os.urandom(10).hex()
    print(f'\n\n{colors.GREY} Token: {token_A}')


    # enviando Cπ
    print(f'\n\n{colors.BLUE}Enviou - Cπ:{colors.END}')
    connection.client.send(address_A.exportKey())
    print(address_A.exportKey())
    

    # recebendo Sπ, Cπ(Sπ)
    print(f'\n\n{colors.GREEN}Recebeu - Sπ, Cπ(Sπ):{colors.END}')
    address_B = RSA.import_key(connection.server.recv(2048))
    cryptoken_B = connection.server.recv(2048)

    print(address_B.export_key(), '\n')
    print(cryptoken_B)
    
    
    # enviando Sπ(Cπ , Sπ)
    print(f'\n\n{colors.BLUE}Enviou - Sπ(Cπ , Sπ):{colors.END}')

    decryptoken_B = priKey_A.decrypt(cryptoken_B).decode()
    token_string = f'{token_A},{decryptoken_B}'

    encryptor = PKCS1_OAEP.new(address_B)
    cryptoken_A_B = encryptor.encrypt(token_string.encode())
    connection.client.send(cryptoken_A_B)
    
    print(cryptoken_A_B)



    # recebendo Cπ(Cπ)
    print(f'\n\n{colors.GREEN}Recebeu - Cπ(Cπ):{colors.END}')
    cryptoken_A = connection.server.recv(2048)
    decryptoken_A = priKey_A.decrypt(cryptoken_A).decode()
    print(cryptoken_A)


    # AutenticaΓ§Γ£o
    if decryptoken_A == token_A:
        print(f'\n\n{colors.GREY}UsuΓ‘rio autenticado.{colors.END}\n')
        return True, ''.join(sorted([token_A, decryptoken_B])), address_B
    else:
        print(f'\n\n{colors.RED}UsuΓ‘rio NΓO autenticado.{colors.END}\n')
        connection.client.close()
        return False


