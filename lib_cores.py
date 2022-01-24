class colors:
    fim = '\033[0m'
    negrito = '\033[1m'
    sublinhado = '\033[4m'
    vermelho = '\033[91m'
    verde = '\033[92m'
    laranja = '\033[93m'
    azul = '\033[94m'
    magenta = '\033[95m'
    ciano = '\033[96m'
    
def testes():
    print(f'{colors.magenta}Teste Magenta{colors.fim}')
    print(f'{colors.azul}Teste Azul{colors.fim}')
    print(f'{colors.ciano}Teste Ciano{colors.fim}')
    print(f'{colors.verde}Teste Verde{colors.fim}')
    print(f'{colors.laranja}Teste Laranja{colors.fim}')
    print(f'{colors.vermelho}Teste Vermelho{colors.fim}')
    print(f'{colors.negrito}Teste Negrito{colors.fim}')
    print(f'{colors.sublinhado}Teste Sublinhado{colors.fim}')