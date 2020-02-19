# Verifica se o carro está acima da velocidade determinada

vel = float(input('Qual a velocidade do carro: '))
multa = int(vel-80) * 7

if vel > 80:
    print('Você está multado e pagará R${:.2f} reais de multa'.format(multa))
else:
    print('Você não está multado, boa viagem') 