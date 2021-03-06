velocidade = float(input('Qaul a velocidade do veiculo? '))
if velocidade > 80:
        print('Por favor, dirija com mais CUIDADO! O limite da pista é de 80KM.')
        multa = (velocidade - 80) * 7
        print(f'Você deve pagar um multa de {multa:.2f} como penalidade.')
else:
    print('PARABÉNS, você está em uma velocidade ideal para pista!')
