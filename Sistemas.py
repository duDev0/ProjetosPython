import json
import bcrypt
import os


ARQUIVO_DB = 'usuario.json'

def carregar_usuarios():
    if not os.path.exists(ARQUIVO_DB):
        return{}
    with open(ARQUIVO_DB, 'r') as f:
        return json.load(f)


def salvar_usuarios(usuarios):
    with open(ARQUIVO_DB, 'w') as f:
        json.dump(usuarios, f, indent=4)


def registrar_usuario():
    usuarios = carregar_usuarios()
    username = input('Digite seu nome de Usuário: ').strip()

    if username in usuarios:
        print('Este usuário ja existe!')
        return

    senha = input('Digite sua senha: ').encode('utf-8')
    senha_hash = bcrypt.hashpw(senha, bcrypt.gensalt()).decode('utf-8')

    usuarios[username] = senha_hash
    salvar_usuarios(usuarios)
    print (f'Usuário {username}, registrado com sucesso! ')

def login():
    usuarios = carregar_usuarios()
    username = input('Usuário: ').strip()

    if username not in usuarios:
        print('Usuário não encontrado!')
        return

    senha = input('Senha: ').encode('utf-8')
    senha_hash = usuarios[username].encode("utf-8")
    if bcrypt.checkpw(senha, senha_hash):
        print(f'Login efetuado com sucesso, seja bem vindo {username}')
    else:
        print('Senha invalida!')

def main():
    while True:
        print('Seja bem vindo ao GerencieJá!')
        print('1- Login!')
        print('2- Registrar!')
        print('3- Sair!')
        op = input(': ')

        if op == '1':
            login()
            
        elif op == '2':
            registrar_usuario()

        elif op == '3':
            print('Encerrando sistema...')
            break

        else:
            print('Opção inválida, tente novamente!')
            

if __name__ == '__main__':
    main()
