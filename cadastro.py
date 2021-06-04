import os
import json

def cadastrarUsuario(login, senha):
    d1 = lerUsuarios()

    if exists(login, d1): return False
    else: 
        d1[login] = {
            'login': login,
            'senha': senha
            }
        with open('usuarios.json', 'w+') as file:
            json.dump(d1, file)

def lerUsuarios():
    usuarios = {}

    if os.path.exists('usuarios.json'):
        with open('usuarios.json', 'r') as file:
            usuarios = json.load(file)

    return usuarios

def exists(login, dicionario):
    chaves = dicionario.keys()
    if login in chaves:
        return True