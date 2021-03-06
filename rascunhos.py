n=int(input("Digite um número par ser covertido:")

print('Escolha como você quer que o número seja convertido:\n1 - BINÁRIO\n2 - HEXDECIMAL\n3 - OCTAL')
opcao=int('Sua opção:')
if opcao == 1:
    print(f'{n} em BINÁRIO é igual á:{bin(n)}')
