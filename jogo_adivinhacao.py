'''

Jogo de adivinhação de número entre 1 e 100.

'''

import random
import os
import time

def limpa_tela():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def resposta(r):
    while True:
        if r in "sS":
            return True
        elif r in "nN":
            return False
        else:
            r = input ("\nInsira uma opção válida: ")

def compara(n, p):
    return n == p

def dica(n, p):
    if n > p:
        m = "maior"
    else:
        m = "menor"
    return print ("\nPalpite incorreto. Dica: tente um palpite %s." %m)

def main():
    palpite = 0
    i = 0
    r = "s"
    lista_de_palpites = []

    while resposta(r):
        limpa_tela()
        try:
            print ("JOGO DA ADIVINHAÇÃO\n")
            print ("Adivinhe o número escolhido.\nBoa sorte!")
            if palpite == 0:
                numero = random.randint(1, 100)
                print ("\nDica: tente um palpite entre 1 e 100")
            else:
                dica(numero, palpite)
            print ("\nSeus palpites válidos até o momento:")
            print (lista_de_palpites)
            i += 1
            palpite = int (input ("\nTentativa %d: " %i))
            lista_de_palpites.append(palpite)
            if compara(numero, palpite):
                print ("\nParabéns! Você acertou!")
                print ("Tentativas necessárias: %d." %i)
                palpite = i = 0
                lista_de_palpites.clear()
                r = input ("\nJogar novamente (S/N)? ")
                if r in "nN":
                    print ("\nObrigado por jogar! Até a próxima!")
                    time.sleep(2)
        except:
            print ("\nValor inserido é inválido.") 
            time.sleep(1)

if __name__ == "__main__":
    main()
