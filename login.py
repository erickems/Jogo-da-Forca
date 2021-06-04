from cadastro import lerUsuarios

def logar():
    dir_usuarios = lerUsuarios()
    chaves_usuarios = dir_usuarios.keys()
    flag = True
    flag2 = True

    while(flag):
        login = input('Digite seu login: ')

        if login in chaves_usuarios:

            flag = False
            while(flag2):
                senha = input('Digite sua senha: ')

                if dir_usuarios[login]['senha'] == int(senha): 
                    print('Acesso autorizado')
                    flag2 = False
                else: 
                    print('Senha incorreta')
                    flag2 = True

        else: print('Usuario inexistente'); flag = True            