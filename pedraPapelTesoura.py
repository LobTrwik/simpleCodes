from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print('''Suas opções:
0 - Pedra
1 - Papel
2 - Tesoura''')
jogador = int(input('Escolha sua Jogada:'))
print('JO')
sleep (1)
print('KEN')
sleep(1)
print('PO!!!')
print('\033[35m=-=' * 9)
print(f'\033[36mO computador jogou \033[35m{itens[computador]}')
print(f'\033[36mE o jogador jogou \033[35m{itens[jogador]}')
print('\033[35m=-=' * 9)
if computador == 0: #PEDRA
    if jogador == 0:
        print('\033[36mEMAPTE!')
    elif jogador == 1:
        print('\033[36mVOCÊ VENCEU. PARABENS!')
    elif jogador == 2:
        print('\033[36mVOCÊ PERDEU. :(')
    else:
        print('\033[36mJOGADA INVÁLIDA!')
elif computador == 1: #PAPEL
    if jogador == 0:
        print('\033[36mVOCÊ PERDEU. :(')
    elif jogador == 1:
        print('\033[36mEMAPTE!')
    elif jogador == 2:
        print('\033[36mVOCÊ VENCEU. PARABENS!')
    else:
        print('\033[36mJOGADA INVÁLIDA!')
elif computador == 2: #TESOURA
    if jogador == 0:
        print('\033[36mVOCÊ VENCEU. PARABENS!')
    elif jogador == 1:
        print('\033[36mVOCÊ PERDEU. :(')
    elif jogador == 2:
        print('\033[36mEMAPTE!')
    else:
        print('\033[36mJOGADA INVÁLIDA!')


