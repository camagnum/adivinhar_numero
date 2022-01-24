from lib_cores import colors
from util import *

def inicio_jogo():    
    clear()
    print('========================')
    print(f'{colors.verde}          Olá!      ')
    print(f'   Bem-vindo ao jogo! {colors.fim}')
    print('========================')
    print()

    while True:
        inicio = input(f'{colors.vermelho}Aperte ENTER para iniciar\n{colors.fim}')
        if inicio == '':
            break

def principal():
    clear()
    
    numero = num_aleatorio(1,100)
    chute = int(input('Vamos começar. Já pensei em um número. Qual foi? '))
    tentativas = 0
    while True:
        if chute == numero:
            print(f'{colors.verde}Parabéns! Você acertou em {tentativas} tentativas! Eu pensei no número {numero}.{colors.fim}')
            break
        elif chute > numero:
            chute = int(input(f'O número que eu pensei é {colors.ciano}menor{colors.fim} que {colors.ciano}{chute}{colors.fim}: '))
            tentativas += 1
        elif chute < numero:
            chute = int(input(f'O número que eu pensei é {colors.ciano}maior{colors.fim} que {colors.ciano}{chute}{colors.fim}: '))
            tentativas += 1

def recomeco():
    while True:
        recomecar = input(f'{colors.laranja}Quer jogar novamente? (S/N)\n{colors.fim}')

        if recomecar[0].lower() == 's':
            return True
        elif recomecar[0].lower() == 'n':
            return False
        else:
            print('Insira uma resposta válida')

def encerrar():
    print(f'{colors.vermelho}Obrigado por jogar conosco.{colors.fim}')

def jogo():
    while True:
        principal()
        continuar = recomeco()
        if not continuar:
            encerrar()
            break

inicio_jogo()
jogo()