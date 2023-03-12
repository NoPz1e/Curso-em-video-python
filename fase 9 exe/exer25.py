## Desafio 25
'''
Crie um programa que leia o nome de uma 
pessoa e diga se ela tem "silva" no nome!
'''

# pergunta um nome e elimina espaços inuteis
nome = str(input('Qual é o seu nome completo? ')).strip().lower()

# verifica se tem silva no nome
sil = bool('silva' in nome)

# Apresenta se o nome tem silva ou não
print(f'Seu nome tem Silva? {sil}')