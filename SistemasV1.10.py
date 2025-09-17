import time
import getpass
import os
import json
import bcrypt
from datetime import datetime


ARQUIVO_DB = 'usuario110.json'

def carregar_usuarios():
    if not os.path.exists(ARQUIVO_DB):
        return {}
    with open(ARQUIVO_DB, 'r') as f:
        return json.load(f)
    
def salvar_usuarios(usuario):
    with open(ARQUIVO_DB, 'w') as f:
        json.dump(usuario, f, indent=4)

def registrar_usuario():
    usuarios = carregar_usuarios()
    username = input('Novo usuário: ').strip()

    if username in usuarios:
        print('Usuário já existe!')
        return
    
    senha = getpass.getpass('Nova Senha: ').encode('utf-8')
    senha_hash = bcrypt.hashpw(senha, bcrypt.gensalt()).decode('utf-8')

    usuarios[username] = senha_hash
    salvar_usuarios(usuarios)
    print(f'Usuario: {username}, REGISTRADO!')

def login():
    usuarios = carregar_usuarios()
    username = input('Usuário: ').strip()

    if username not in usuarios:
        print(f'Usuario: {username}, NÃO REGISTRADO!')
        return None
    
    senha = getpass.getpass('Senha: ').encode('utf-8')
    senha_hash = usuarios[username].encode('utf-8')

    if bcrypt.checkpw(senha, senha_hash):
        print('On-line')
        return username
    else:
        print('Senha ou usuario incorreto!')
        return None


def saudacao():
    hora_atual = datetime.now().hour

    if 5 <= hora_atual < 12:
        return 'Bom-Dia'
    
    elif 12 <= hora_atual < 18:
        return 'Boa-Tarde'
    
    else:
        return 'Boa-Noite'



def main():
    usuario_logado = None

    while True:
        
        print('C&O Manager')
        print('1- Login!')
        print('2- Cadastre-se!')
        print('3- sair!')

        op = input(': ')

        if op == '1':
            usuario_logado = login()
            if usuario_logado:
                print(f'{saudacao()}, {usuario_logado}!')
                break

        elif op == '2':
            registrar_usuario()

        elif op == '3':
            print('Logoff')

        else:
            print('Opção invalida, tente novamente!')


    print('1- Lava Rapido!')
    print('2- Restaurante!')
    print('3- Eletronicos!')
    print('4- Sair!')
    es = input(': ')
    if es == '1':
        print('Lava-Rapido')
        print('1- Clientes!')
        print('2- Produtos!')
        print('3- Funcionarios!')
        print('4- Funcionarios!')

    elif es == '2':
        print('Restaurante!')
        print('1- Faturamento!')
        print('2- Estoque!')
        print('3- Funcionarios!')
        
    elif es == '3':
        print('Eletronicos!')
        print('1- Faturamento!')
        print('2- Estoque!')
        print('3- Funcionarios!')

    elif es == '4':
        print('Logoff...')

    else:
        print('Opção invalida!')
        return




if __name__ == '__main__':
    main()
