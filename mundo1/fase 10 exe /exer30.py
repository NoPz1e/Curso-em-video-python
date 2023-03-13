## Desafio 30
'''
Crie um programa que leia um número
inteiro e mostre na tela se ele é PAR ou IMPAR.
'''

# pergunta ao utilizador um número
num = int(input('Digite um número inteiro que deseja saber se é PAR ou impar: '))

# calcula se o número é par ou impar
parimp = bool(num % 2)

# verifica se o número é par ou ímpar
if parimp == True:
    print(f'O número {num} é ímpar!!!')
else: 
    print(f'O número {num} é par!!!') 
