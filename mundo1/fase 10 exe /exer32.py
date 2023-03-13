## Desafio 32
'''
Faça um programa que leia
um ano qualquer e mostre
se ele é bissexto
'''

# pergunta um ano para verificar
ano = int(input('Digite um ano para saber se é bissexto: '))

# faz calculo para verificar se o ano é bissexto
biss = bool(ano % 4)

# verifica se é bissexto para apresentar
if biss == True:

    # apresenta ao utilizador o resultado
    print(f'O ano {ano} não é um bissexto!!')

else:
    
    #apresenta ao atilizador o resultado
    print(f'O ano {ano} é um ano bissexto!!')