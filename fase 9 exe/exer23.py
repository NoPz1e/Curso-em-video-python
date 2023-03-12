## Desafio 23
'''
Faça um programa que leia um número
de 0 a 9999 e mostre na tela cada um 
dos digitos separados.
'''

# pergunta um número entra 0 a 9999
num = int(input('Digite um número de 0 a 9999: '))

# calcula o número das unidades
u = num // 1 % 10

# calcula o número das dezenas
d = num // 10 % 10

# calcula o número das Centenas
c = num // 100 % 10

# calcula o número dos milhares
m = num // 1000 % 10

# apresenta o número das unidades
print(f'Unidades: {u}')

# apresenta o número das Dezenas
print(f'Dezena: {d}') 

# apresenta o número das Centenas
print(f'Centenas: {c}')

# apresenta o número dos milhares
print(f'Milhar: {m}')