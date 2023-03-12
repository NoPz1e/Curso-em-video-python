## Desafio 19
'''
Um professor quer sortear um dos 
seus quatro alunos para apagar
o quadro. Faça um programa que ajude
ele, lendo o nome deles e escrevendo 
o nome do escolhido.
'''

# importa a biblioteca random
import random

# pergunta o nome dos alunos
a1 = input('Primeiro aluno: ')
a2 = input('Segundo aluno: ')
a3 = input('Terceiro aluno: ')
a4 = input('Quarto aluno: ')

# criar uma lista comos nomes dos alunos
lista = [a1, a2 , a3, a4]

# escolhe aliatoriamente um dos quatro alunos
esc = random.choice(lista)

# apresenta o aluno escolhido
print(f'O aluno escolhido foi:{esc}')