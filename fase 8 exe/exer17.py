## Desafio 17
'''
Faça um programa que leia o comprimento
do cateto aposto e do cateto adjacente de um triãngulo
retãngulo, calcule e mostre o comprimento da hipotenusa
'''

# pergunta ao utilizador o comprimento do cateto oposto
op = float(input('Digite o comprimento do cateto oposto: '))

# pergunta ao utilizador o comprimento do cateto adjacente
ad = float(input('Digite o comprimento do cateto adjacente: '))

## calculo sem o biblioteca math

# Calcula a hipotebusa
hi = (op ** 2 + ad ** 2) ** (1/2)

# apresenta o comprimento da hipotenusa
print(f'A hipotenusa vai medir {hi:.2f}')

## calculo com a bibliteca math

# importa a função da biblioteca math
from math import hypot

# apresenta o comprimento da hipotenusa
print(f'A hipotenusa mede {hypot(op, ad):.2f}')