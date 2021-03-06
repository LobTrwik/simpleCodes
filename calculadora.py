print('\033[33mOlá, tudo bom? Eu sou sua calculadora virtual. \nMas primeiro a gente vai fazer seu cadrasto pra você ter total suposte do nosso site.')
nome = input('\n\033[37mQual seu nome: ')
print(f'Ola, {nome}! Prazer em conhecelo-lo!.')
data = input('Voce poderia nos falar sua data de nacimento: ')
print('Uau. tudo bem, voce nasceu em',data,'agora siga o seu cadastro...')
enderecodeemail = input('Agora voce poderia digitar seu endereço de email? ')
print('Ok, seu endereço de email',enderecodeemail,'foi salvo em nosso sistema')
print('\n\033[33magora é so entrar no seu email, confirmar seu cadastro e pegar sua senha. Muito obrigado por encolher a gente!')


input('\n\n\033[35mProntinho! \nAgora é só teclar ENTER que a gente já vai te redirecionar para nossa calculadora...')

n1 = float(input('\n\033[36mDigite um número: '))
n2 = float(input('Digite outro número que será calculado pelo de cima: '))
import math
print(f'\nA porção inteira de {n1}: é {math.trunc(n1)}')
print(f'A porção inteira de {n2} é {math.trunc(n2)}')
rq1 = n1 ** (1/2)
rq2 = n2 ** (1/2)
print(f'\nA raiz quadrada do némero {n1} é: {rq1}')
print(f'A raiz quadrada do número {n2} é: {rq2}')
s = n1 + n2
s1 = n1 - n2
d = n1
m = n1*n2
d = n1/n2
di = n1//n2
p = n1**n2
print(f'{n1}+{n2} = {s}')
print(f'{n1}-{n2}={s1}')
print(f'A divisão de {n1} com {n2} é: {d}\nA multiplicacão é {m}')
print(f'A divisão Inteira é {di}.\nA potencia é igual à {p}.\n\n')


input('Muito bem! Ainda temos um conversor de dolár. Você quer testalo? Digite ENTER...')

real = float(input(f'{nome}, Digite um valor em real que vocé quer converter em dolar: R$'))
dolar = real / 5.60
print(f'\n{real:.2f} reais é igual a {dolar:.2f} doláres.')


input(f'\n\n{nome}, tecle ENTER se quiser entrar em nosso calculador de área para pintura.')

ap = float(input('Digite a autura da parede: mm '))
lp = float(input('Digite a largura da parede: mm '))
mq = ap * lp
print(f'A sua parede tem {mq}m²')
litros = float(input('Você gasta quantos litros de tinta por metro quadrado? L'))
lt = mq / litros
print(f'\nVocê irá gastar {lt} litros para pintar sua parede.')


print(f'\n\n{nome}, Você quer calcular o valor de descontos de produtos? Se sim, digite ENTER...')

preco = float(input('\nQual o preço do produto? R$'))
desconto = int(input('Qual o desconto do produto? %'))
vdcd = preco - (preco * desconto / 100)
print(f'\nO valor do produto com desconto é igual a {vdcd} R$')


input(f'\n\n{nome}, tecle ENTER se você quiser somar 2 médias para chegar em um resultado... \nLembre-se de colocar ponto no lugar da virgula.')

m1 = float(input('\nDigite a PRIMEIRA média; '))
m2 = float(input('Digite a SEGUNDA média; '))
media = (m1 + m2) / 2
print(f'A sua média foi:{media}')
if media >= 7.0:
    print(f'PARABÉNS {nome}, sua média está boa!')
else:
    print(f'{nome}, sua média precisa ser melhorada.')


input(f'\n\n{nome}, nós também temos  nosso leitor de número impar ou par. Tecle ENTER se você quiser testalo...')

numero = int(input('Bom, para saber-se se o número INTEIRO é impar ou par. bastao digita-lo abaixo: \n'))
resultado = numero % 2
if resultado == 1:
    print(f'\nO número {numero} é ÍMAPAR.')
else:
    print(f'O número {numero} é PAR.')


input(f'\n\n{nome}, tecle ENTER para verificar anos BISSEXTOS e NÃO BISSEXTOS...')

from datetime import date
anob = int(input('\nDigite um ano para sabermos se é BISSEXTO ou NÃO. E digite 0 se for o ano ataual: \n'))
if anob == 0:
    ano = date.today().year
if anob % 4 == 0 and anob % 100 != 0 or anob % 400 == 0:
    print(f'O ano {anob} É BISSEXTO.')
else:
    print(f'O ano {anob} NÃO É BISSEXTO.')
