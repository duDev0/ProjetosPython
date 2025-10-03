import bcrypt 
import sqlite3
from prompt_toolkit import prompt
from datetime import datetime

conn = sqlite3.connect('users120.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users120 (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT UNIQUE,
    senha BLOB,
    is_admin INTEGER DEFAULT 0
)
''')

conn.commit()

def cadastrar_usuario():
    print('Digite seu nome/usuário!')
    nome = input(': ').strip()
    print('Digite sua senha!')
    senha = prompt(': ', is_password=True)

    if not nome or not senha:
        print('error *username and password are empty')
        return

    senha_hash = bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt())
    
    print(f'O usuário {nome}, será ADMINISTRADOR? (s/*)')
    adm = input(':').strip().lower()
    is_admin = 1 if adm == 's' else 0

    try:
        cursor.execute('INSERT INTO users120 (nome, senha, is_admin) VALUES (?, ?, ?)',
                       (nome, senha_hash, is_admin))
        conn.commit()
        print(f'Usuário: {nome}, CADASTRADO COM SUCESSO!')
    except sqlite3.IntegrityError:
        print(f'Usuário: {nome}, já existe!')

def login_usuario():
    print('Usuário')
    nome = input(': ').strip()
    print('Senha')
    senha = prompt(': ',is_password=True)

    cursor.execute('SELECT senha, is_admin FROM users120 WHERE nome = ?', (nome,))
    registro = cursor.fetchone()

    if registro:
        senha_hash, is_admin = registro

        if bcrypt.checkpw(senha.encode('utf-8'), senha_hash):
            print('On-line')
            return nome, bool(is_admin)

        else:
            print('error *password')
            return None, False
    else:
        print('error *users')
        return None, False

def saudacao():
    hora_atual = datetime.now().hour

    if 5 <= hora_atual <12:
        return 'Ótimo-Dia!'
    
    elif 12 <= hora_atual <18:
        return 'Ótima-Tarde!'
    
    else:
        return 'Ótima-Noite'

def main():
    usuario_logado = None

    while True:

        print('C&O Manager')
        print('1- Login!')
        print('2- Criar Usuário!')
        print('3- Sair!')

        op = input(': ')

        if op == '1':
            usuario_logado, is_admin = login_usuario()
            if usuario_logado:
                if is_admin:
                    print(f'{saudacao()}, Sr. {usuario_logado}!')
                    print('Acesso TOTAL do sistema LIBERADO!')
                    
                    print('password is admin')
                else:
                    print(f'{saudacao()}, {usuario_logado}!')
                break

        elif op == '2':
            cadastrar_usuario()
            

        elif op == '3':
            print('Logoof...')
            break

        else:
            print('error *option invalid')

if __name__ == '__main__':
    main()
