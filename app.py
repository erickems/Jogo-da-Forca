import random

def main():
    jogar()

def jogar():
    minha_palavra = recuperaPalavra()
    meu_palpite = escondePalavra(minha_palavra)
    palpites = []

    while(True):
        print(meu_palpite)
        letra = input('\nUma letra: ') 
        palpites.append(letra)
        print('Palpites dados: ', end='')
        print(palpites)
        meu_palpite = palpite(letra, minha_palavra, meu_palpite)

        if acertou(meu_palpite) == 'exit':
            print(meu_palpite)
            break
    print('Parabéns, você acertou!!')

    return

def recuperaPalavra():    
    lista_palavras = ['mesa']
    randomico = random.randint(0, len(lista_palavras)-1) 

    return lista_palavras[randomico]

def escondePalavra(palavra):
    palavra_escondida = ''

    for i in range(len(palavra)):
        palavra_escondida += "_ "
    palavra_escondida = palavra_escondida[:-1]

    return palavra_escondida

def palpite(letra, palavra, palavra_escondida):
    indexes = []
    index = -1
    ocorrencias = palavra.count(letra)
    palavra_atual = palavra_escondida

    if ocorrencias > 0:
        for i in range(ocorrencias):
            index = palavra.find(letra, index + 1)
            indexes.append(index)
        palavra_atual = descobrePalavra(indexes, letra, palavra_escondida)
    
    return palavra_atual
    
def descobrePalavra(indexes, letra, palavra_escondida):
    for i in indexes:
        palavra_escondida = palavra_escondida[:i*2] + letra + palavra_escondida[(i*2) + 1:] 

    return palavra_escondida

def acertou(palavra):
    if palavra.find('_') == -1: return 'exit'

if __name__ == "__main__":
    main()