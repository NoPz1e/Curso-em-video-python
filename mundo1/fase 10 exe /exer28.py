## Desafio 28
'''
Escreva um programa que faça o computador
"pensar" em um número inteiro entre 0 e 5
e peça para o utilizador tentar descobrir
qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o utilizador
veceu ou perdeu
'''

# importa a biblioteca random para gerar um número
import random

# apresenta o jogo ao utilizador
print('Vamos jogar a um jogo, em penso num número e voçê adivinha')

# gera um número aliatorio
num = random.randint(0,5)

# pede que ao utilizador para escolher um número
escolha = int(input('Tente acertar o número que eu pensei, digite um número entre 0 e 5: '))

# verifica se o número é igual ao gerado pelo computador
if escolha == num:
    # caso o utilzador acerte 
    print('Parabéns voçê acertou o número!!!')
else:
    # caso o utilizador erre
    print('Voçê errou, tente novamente!!!')