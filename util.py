# Importar pacotes
import imp
from random import randint
from os import system,name

# Gerar um número aleatório
def num_aleatorio(ini,final):
    return randint(ini,final+1)

def clear():
    if name == 'nt':
        system('cls')
    else:
        system('clear')