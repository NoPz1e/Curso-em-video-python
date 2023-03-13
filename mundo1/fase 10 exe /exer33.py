## Desafio 33
'''
Faça um programa que leia
três números e mostra qual é o maior
e qual é o menor
'''

# pergunta três números aos utilizadores
num1 = input('Digite um número: ')
num2 = input('Digite outro número: ')
num3 = input('Digite o terceiro número: ')

# verificar quem é menor
menor = num1
if num2 < num1 and num2 < num3:
    menor = num2

if num3 < num1 and num3 < num2:
    menor = num3

# verificar quem é maior
maior = num1
if num2 > num1 and num2 > num3:
    maior = num2

if num3 > num1 and num3 > num2:
    maior = num3

print(f'O menor valor digitado foi {menor}')
print(f'O maior valor digitado foi {maior}')