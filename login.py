from cadastro import lerUsuarios
import os, time

def logar():
    dir_usuarios = lerUsuarios()
    chaves_usuarios = dir_usuarios.keys()

    login = input('\nDigite seu login: ')
    
    if login in chaves_usuarios:
        senha = input('Digite sua senha: ')

        if dir_usuarios[login]['senha'] == senha or dir_usuarios[login]['senha'] == int(senha): print('Acesso autorizado!'); time.sleep(0.5); return True
        
        else: print('Senha incorreta!'); time.sleep(0.7); os.system('cls' if os.name == 'nt' else 'clear'); return False

    else: print('Usuario inexistente!'); time.sleep(0.7); os.system('cls' if os.name == 'nt' else 'clear'); return False         