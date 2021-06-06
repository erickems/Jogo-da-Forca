# encoding: utf-8
# encoding: iso-8859-1
# encoding: win-1252

import os, json

def cadastrarUsuario():
    d1 = lerUsuarios()

    login = input('Digite o login: ')
    senha = input('Defina uma senha: ')

    if exists(login, d1): print('Usuário já cadastrado'); return False
    else: 
        d1[login] = {
            'login': login,
            'senha': senha
            }
        with open('usuarios.json', 'w+') as file:
            json.dump(d1, file)
            
        print('Cadastro realizado com sucesso!')

def lerUsuarios():
    usuarios = {}

    if os.path.exists('usuarios.json'):
        with open('usuarios.json', 'r') as file:
            usuarios = json.load(file)

    return usuarios

def cadastrarPalavra(palavra, dica):
    d1 = lerPalavras()

    if exists(palavra, d1): return False
    else: 
        d1[palavra] = {
            'nome': palavra,
            'dica': dica
            }
        with open('palavras.json', 'w+', encoding='utf8') as file:
            json.dump(d1, file, ensure_ascii=False)

def lerPalavras():
    palavras = {}

    if os.path.exists('palavras.json'):
        with open('palavras.json', 'r', encoding='utf8') as file:
            palavras = json.load(file)

    return palavras

def exists(chave, dicionario):
    chaves = dicionario.keys()
    if chave in chaves:
        return True

# def main():
#     while(True):
#         print(lerPalavras())
#         palavra = input('Palavra: ')
#         if palavra == 'exit': break
#         dica = input('Dica: ') 
#         cadastrarPalavra(palavra, dica)

# if __name__ == '__main__':
#     main()