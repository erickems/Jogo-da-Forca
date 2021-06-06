from cadastro import lerUsuarios

def logar():
    dir_usuarios = lerUsuarios()
    chaves_usuarios = dir_usuarios.keys()

    login = input('Digite seu login: ')
    
    if login in chaves_usuarios:
        senha = input('Digite sua senha: ')

        if dir_usuarios[login]['senha'] == int(senha) or dir_usuarios[login]['senha'] == senha: print('Acesso autorizado'); return True
        
        else: print('Senha incorreta'); return False

    else: print('Usuario inexistente'); return False         