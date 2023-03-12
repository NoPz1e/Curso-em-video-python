## Desafio 27
'''
Faça um programa que leia o nome completo
de uma pessoa, mostrando em seguida o primeiro e o
último nome separadamente.
'''

# pergunta o nome completo ao utilizador
no = input('Escreva o seu nome completo: ').strip().title()

# divide o nome para uma lista
nome = no.split()

# apresenta o primeiro nome
print(f'O seu primeiro no é : {nome[0]}')

# apresenta o ultimo nome
print(f'O seu ultimo nome é : {nome[len(nome)-1]}')