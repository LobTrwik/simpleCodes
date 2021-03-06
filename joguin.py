from random import randint
from time import sleep

print('\033[032mOlá, player!')
nick = input('Qual seu nick? ')

print(f'\n\033[035mOlá {nick}, Eu sou o Robô! \nVou pensar em um número de 0 a 10. Tente adivinhar...')
computador = randint (0, 10)

palpites = 0
acertou = False
while not acertou:
    jogador = int(input('Qual Número você que eu pensei? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('MAIS...')
        else:
            print('MENOS...')

print('\nPROCESSANDO...')
sleep (3)

print(f'\n\033[038mParabéns. Você acertou com {palpites} Palpites')

