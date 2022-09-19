import os
import global_variables as gvar
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


def login(login):
    path = f'users{gvar.bar}{login}{gvar.bar}{login}.pem'
    adress_keys = RSA.import_key(open(path).read())
    adress, priKey = adress_keys.publickey(), adress_keys
    return adress, priKey


def create(new_user):
    #new_user = input('Novo usuário: ')
    path = f'users{gvar.bar}{new_user}'
    if not os.path.exists(path) and new_user.isalpha():
        os.mkdir(path)
        os.mkdir(f'{path}{gvar.bar}friends')
        with open(f'{path}{gvar.bar}{new_user}.pem', 'xb') as p:
            key = RSA.generate(1024, os.urandom)
            p.write(key.export_key())
            p.close()
        print(f'Usuário {new_user} criado com sucesso!\nEndereço:')
        print(key.publickey().export_key().decode())
        input()
    else:
        print('Usuário inválido.')


def add_friend(login, friend, address):
    path = f'users{gvar.bar}{login}'
    if os.path.exists(path) and friend.isalpha():
        with open(f'{path}{gvar.bar}{login}_friends_addresses.txt', 'r+') as f:
            # [ line.rstrip('\n') for line in f.readlines() ]
            friends_addresses = f.readlines()
            # f.close()
            for friend_address in friends_addresses:
                if address == friend_address.split(',')[0]:
                    print('Amigo já existente.')
                    f.close()
                    return
            print('Amigo adicionado.')
            f.write(f'{address}, {friend}\n')
            f.close()
    else:
        print('Usuário ou amigo inválido.')

def save_chat(login, friend_name, current_chat):
    if friend_name is None or current_chat == []:
        return
    print(current_chat)
    chat_path = f'users{gvar.bar}{login}{gvar.bar}friends{gvar.bar}{friend_name}.txt'
    with open(chat_path, 'a+') as friend_chat:
        for msg in current_chat:
            #append_string = repr(f'{username}:{msg}')+'\n'
            friend_chat.write(msg)
        friend_chat.close()

def print_chat(login, friend_name):
    chat_path = f'users{gvar.bar}{login}{gvar.bar}friends{gvar.bar}{friend_name}.txt'
    if os.path.exists(chat_path):
        with open(chat_path, 'r') as friend_chat:
            return friend_chat.readlines()
    return None


def is_friend(login, received_address):
    friend_name = None
    for friend in os.scandir(f'users{gvar.bar}{login}{gvar.bar}friends'):
        if friend.is_file() and os.path.splitext(friend)[1].lower() == '.pem':
            with open(friend.path) as friend_pem:
                friend_address = RSA.import_key(friend_pem.read())
                friend_pem.close()
            if friend_address == received_address:
                friend_name = friend.path.split(gvar.bar)[-1].split('.')[0]
    return friend_name



def get_priKey(login):
    with open(f'users{gvar.bar}{login}{gvar.bar}{login}.pem') as privateKey:
        priKey = RSA.import_key(privateKey.read())
        privateKey.close()
    return priKey




'''chat_append = [['daniel', 'hehehe\nbarra ene'],
               ['gigi', 'blablabla2\n\n\n\'\"']]
save_chat('daniel', chat_append, 'gigi')
get_chat('daniel','gigi')
'''
# user_create()
#user_add_friend('jose', 'B', 'key0')
