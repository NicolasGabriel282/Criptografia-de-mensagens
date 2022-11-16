#pip install cryptocode

import cryptocode as cripto
import os
from pprint import pprint

def menu():
    pergunta=input('''Digite o número do que voce deseja realizar:
            1 - Criptografar uma frase
            2 - Ler o arquivo com as frases criptografadas
            3 - Ler o arquivo com as frases descriptografadas\n ''')
    if pergunta == "1":
        opcao_1()
    elif pergunta == '2':
        opcao_2()
    elif pergunta == '3':
        opcao_3()
    else:
        menu()


def opcao_1():
    mensagem=input("Qual mensagem voce deseja esconder?\n")
    arquivo_chave=open("senha.txt","r")
    chave=arquivo_chave.readline()
    mens_cripto= cripto.encrypt(mensagem,chave)
    arquivo=open("dados.txt","a")
    arquivo.write(f'{mens_cripto}\n')
    arquivo.close()
    menu()

def opcao_2():
    arquivo=open('dados.txt','r')
    lista=arquivo.readlines()
    pprint(lista)
    menu()


def opcao_3():
    arquivo_chave=open("senha.txt","r")
    chave=arquivo_chave.readline()
    arquivo=open('dados.txt','r')
    lista=arquivo.readlines()
    contador=0
    while contador <=3:

        tent_chave=str(input("Digite a chave:\n"))
        if tent_chave == chave:
            for x in lista:
                decodificacao=cripto.decrypt(x,tent_chave)
                print(decodificacao.split('\n'))
                contador=4
        else:
            contador=contador + 1
            if contador == 3:
                arquivo.close()
                os.remove("dados.txt")
                break
    menu()


menu()