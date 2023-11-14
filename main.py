import random
from os import system, name

#fução para limpar a tela a cada execução

def limpa_tela():

    if name =='nt':
        _=system('cls')

#função
def game():

    limpa_tela()

    print("\nBem-Vindo(a) ao jogo da forca!")
    print("Advinhe a palavra abaixo:\n")

    #lista de palavras para o jogo
    palavras = ['banana', 'abacate', 'uva', 'morango', 'laranja']

    #escolhe randomicamente uma palavra
    palavra = random.choice(palavras)

    #list comprehension
    letras_descobertas = ['_' for letra in palavra]

    #Número de chances
    chances = 6

    #Lista para as letras erradas
    letras_erradas = []

    #loop enquanto número de chanches for maior do que zero

    while chances > 0:

        #print
        print("".join(letras_descobertas))
        print("\nChances restantes:", chances)
        print("Letras erradas:", " ".join(letras_erradas))


        #tentativa
        tentativa = input("\nDigite uma letra: ").lower()

        #condicional
        if tentativa in palavra:
            index = 0

            for letra in palavra:
                if tentativa == letra:
                    letras_descobertas[index] = letra
                index += 1

        else:
            chances -= 1
            letras_erradas.append(tentativa)
        
        #Condicional
        if "_" not in letras_descobertas:
            print("\nVocê venceu, a palavra era: ", palavra)
            break

    # Condicional
    if "_" in letras_descobertas:
        print("\nVocê perdeu, a palavra era: ", palavra)

#bloco main

if __name__ == "__main__":
    game()
    print("\nParabéns. Você está aprendendo programação em Python. :)\n")