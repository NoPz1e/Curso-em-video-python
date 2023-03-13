## Desafios 34
'''
Escreve um programa que pergunte o salário
de um funcionário e calcule o valor do 
seu valor aumento
Para salários superios a 1.250,00€, calcule um aumento de 10%.
Para os inderiores ou iguais, o aumento é de 15%.
'''

# pergunta qual o salário do funcionário
sal = float(input('Digite o seu salário: '))

# verifica o valor do salário 
if sal > 1250:

    # faz o calculo do aumento
    aum = (sal * 10) / 100

    # apresenta o resultado do salário
    print(f'O seu salário sofrerá um aumento de 10%, e ira passar para {aum:.2f}€ por mês!!!')

else:
    
    # faz o calculo do aumento 
    aum = (sal * 15) / 100

    # apresenta o resultado do salário
    print(f'O seu salário sofrerá um aumento de 10%, e ira passar para {aum:.2f}€ por mês!!!') 