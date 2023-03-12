## Desafio 22
'''
Crie um programa quer leia o name completo
de uma pessoa e mostra:

>>>O nome com todas as letras maiúsculas
>>>O nome com todas minúsculas
>>>Quantas letras ao todo(sem considerar espaços)
>>>Quantas letras tem o primeiro nome
'''

# pede o nome completo do utilizador
nome = str(input('Escreva o seu nome completo: '))

# tira os espaços inuteis
nome = nome.strip()

# mostra o nome com todas as letras maiúsculas
print(f'O seu nome com todas as letras maiúsculas: {nome.upper()}.')

# mostra o nome com todas as letras maiúsculas
print(f'O seu nome com todas as letras minúsculas: {nome.lower()}.')

# conta os caracteres que o nome ocupa incluindo os espaços
con = len(nome)

# conta os caracteres que tem espaços
esp = nome.count(' ')

# apresenta quantas letra tem o nome so utilizador
print(f'O seu nome tem {con - esp} letras.')

# divide o nome para um lista
nolis = nome.split()

# Conta as letra do primeiro nome
prino = len(nolis[0])

# apresenta quantas letra tem o primeiro nome
print(f'O seu primeiro nome {nolis[0]} tem {prino} letras.')