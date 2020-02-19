# Conversor de dolar em real

real = float(input('Digite quantos reais você tem: '))
dolar = real / 4.28

print('Você tem R${:.2f} reais, e convertendo será U${:.2f} dólares'.format(real,dolar))