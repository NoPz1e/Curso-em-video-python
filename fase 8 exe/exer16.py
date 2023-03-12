## Desafio 16
'''
Crie um programa que leia um 
número real qualquer pelo teclado
e mostre na tela a sua porção inteira
'''

# importa a função trunc da biblioteca math
from math import trunc

# Pergunta ao utilizador um número
num = float(input('Digite um número float:'))

# apresenta apenas a sua porção inteira
print(f'O número {num} tem a parte inteira {trunc(num)}')