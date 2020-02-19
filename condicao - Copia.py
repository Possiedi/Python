# Verifica a média tirada de duas notas, e se a pessoa foi aprovada ou reprovada.

nota1 = float(input('Digite qual foi sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
m = (nota1+nota2)/2

print('Sua média foi de {} pontos'.format(m))

if m>=6:
    print('Você foi aprovado')
else:
    print('Você foi reprovado')