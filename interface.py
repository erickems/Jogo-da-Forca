from login import logar
from cadastro import cadastrarUsuario
import os, time

def entrarSistema():
    while(True):
        interface()
        opcao = input('\n** Digite sua opção: ')
        switcher = {
            0: logar,
            1: cadastrarUsuario
        }
        if int(opcao) == 1 or int(opcao) == 2:
            time.sleep(0.5)
            os.system('cls' if os.name == 'nt' else 'clear')
            interface()
            if switcher[int(opcao)-1](): break
        else: print('Entrada inválida!'); time.sleep(0.5); os.system('cls' if os.name == 'nt' else 'clear')

def jogarNovamente():
    res = input('Deseja jogar novamente? (1)Jogar novamente, (2)Sair: ')

    try:
        if int(res) == 1 or int(res) == 2:
            return res
    except:
        print('Entrada inválida')


def interface():
    print(' -----------------------------------')
    print('"                                   "')
    print('"     BEM VINDO AO JOGO DA FORCA    "')
    print('"                                   "')
    print('"   DIGITE 1 para FAZER LOGIN       "')
    print('"   DIGITE 2 para FAZER CADASTRO    "')
    print('"                                   "')
    print('" --------------------------------- "')

    return 
