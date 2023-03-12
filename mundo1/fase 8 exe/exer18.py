## Desafio 18
''' 
Faça um programa que leia um ângulo qualquer e 
mostre na tela o valor de seno, 
cosseno e tangente desse ãngulo.
'''

# importa a biblioteca math
import math

# pergunta ao utilizador um angulo de um triagulo
ang = float(input('Digite um valor de uma angulo de um triagulo: '))

# corverte o angulo para radianos
rad = math.radians(ang)

# Apresenta os valores do seno, cosseno e tangente desse ângulo
print(f'O valor do seu ângulo é de {ang},\nque tem o seno de valor {math.sin(rad):.2f},\no cosseno de valor {math.cos(rad):.2f},\ne a tangente é {math.tan(rad):.2f}.')