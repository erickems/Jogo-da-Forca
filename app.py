import random, time, os
from cadastro import lerPalavras
from interface import entrarSistema, jogarNovamente

def main():
    entrarSistema()
    os.system('cls' if os.name == 'nt' else 'clear')
    entrada = 1
    while (int(entrada) != 2):
        jogar()
        time.sleep(0.7)
        entrada = jogarNovamente()

def jogar():
    minha_palavra, minha_dica = recuperaPalavra()
    meu_palpite = escondePalavra(minha_palavra)
    palpites = []

    while(True):
        print('A dica é: ' + minha_dica)
        print(meu_palpite)
        letra = input('\nUma letra: ') 
        palpites.append(letra)
        print('Palpites dados: ', end='')
        print(palpites)
        meu_palpite = palpite(letra, minha_palavra, meu_palpite)

        if lancar_contagem(meu_palpite):
            if palpite_palavra(meu_palpite) == minha_palavra:
                print('Parabéns, você acertou!!')
                return
            else:
                print(f'Você errou! A palavra correta era {minha_palavra}')
                return

def recuperaPalavra():   
    dict_palavras = lerPalavras()
    lista_numeros_sorteados = []
    i = -1
    
    while(i != len(list(dict_palavras))):
        numero_aleatorio = random.randint(0, len(list(dict_palavras))-1)

        if numero_aleatorio not in lista_numeros_sorteados: 
            i += 1
            lista_numeros_sorteados.append(numero_aleatorio)
            minha_chave = list(dict_palavras)[numero_aleatorio]
            palavra_e_dica = (dict_palavras[minha_chave]['nome'], dict_palavras[minha_chave]['dica']) 
            return (palavra_e_dica)

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

def lancar_contagem(palavra):
    if palavra.count('_') <= 3:
        return True

def palpite_palavra(palavra_palpite):
    if palavra_palpite.count('_') <= 3:
        print(palavra_palpite)
        sec = 5

        while(sec != 0):
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f'\nTempo: {sec}s')
            sec -= 1
            time.sleep(1)

        os.system('cls' if os.name == 'nt' else 'clear')
        print(palavra_palpite)
        resposta = input('A palavra misteriosa é: ')

        return resposta

if __name__ == "__main__":
    main()