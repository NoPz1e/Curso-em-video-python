## Desafio 20
'''
O mesmo professor do desafio 
anterior quer sortear a ordem de apresentação de
trabalhos dos alunos. Faça um programa que leia o 
nomes dos quatro alunos e mostre a ordem sorteada
'''

# importa a biblioteca random
from random import shuffle

# pergunta o nome dos alunos
a1 = input('Primeiro aluno: ')
a2 = input('Segundo aluno: ')
a3 = input('Terceiro aluno: ')
a4 = input('Quarto aluno: ')

# criar uma lista comos nomes dos alunos
lista = [a1, a2 , a3, a4]

# criar uma ordem aleatoria
shuffle(lista)

# apresenta a ordem aleatoria
print(f'A ordem será: {lista}')