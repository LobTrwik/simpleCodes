vdc = float(input('Qual o valor da CASA? R$'))
salario = float(input('Qual seu sálario mensal? R$'))
anos = int(input('Por quantos anos você pretende pagar o imprestimo? '))
prestacao = vdc / (anos * 12)
minimo = salario * 30 / 100
print(f'Para pagar uma casa de {vdc} reais em {anos} anos.\nA prestação será de {prestacao:.2f}')
if prestacao <= minimo:
    print('O emprestimo pode ser CONCEDIDO')
else:
    print('Emprestimo NEGADO!')

