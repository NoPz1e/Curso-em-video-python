## Desafio 31
'''
Desenvolva um programa que pergunte a distância
de uma viagem em km. Calcule o preço da passagem,
cobrando 0.50€ por km para viagens de até 200km
e 0.45€ para viagens mais longas
'''

# pergunta a distancia da viagem
dis = float(input('Qual a distancia da sua viagem? '))

# verifica qual a distancia da viagem
if dis > 200:
    
    # calcula o preço das passagens
    preço = dis * 0.45

    # apresenta o preço das passagem
    print(f'O preço das passagens é de 0.45€ por km,\no total das passgens da sua viagem é de {preço}€')

else:
     
     # calcula o preço das passagens
     preço = dis * 0.50

     # apresenta o preço das passagem
     print(f'O preço das passagens é de 0.50€ por km,\no total das passagens da sua viagem é de {preço}€')