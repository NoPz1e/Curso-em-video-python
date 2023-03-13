## Desafio 29
'''
Escreva um programa que leia a
velocidade de um carro.
Se ele ultrapassar 80km/h,
mostra uma mensagem dizendo
que ele foi multado.
A multa vai custar 7,00€ por cada km
acima do limite
'''

# lê a velocidade do carro
velo = int(input('Qual a velocidade do carro: '))

# verifica se está acima do limite de velocidade
if velo > 80:
    # calcula o preço da multa
    multa = (velo - 80) * 7

    # apresenta a multa
    print(f'Voçê altopasou a velocidade permitida da via e foi multado numa fatura de {multa}€')
else:
    print('O carro pasou sem problemas.')