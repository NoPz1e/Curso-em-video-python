## Desafio 24
'''
Crie um programa que leia o nome de uma cidade 
e diga se ela começa ou não com o nome "Santo"
'''

# Pergunta uam cidade ao utilizador 
# também retira os espacos desnecessarios
cid = str(input('Digite o nome de uma cidade: ')).strip()

# verifica se o nome da cidade começa com Santo
san = bool(cid[:5].upper() == 'SANTO')

#   apresenta se nome começa por santo ou não
print(f'A sua cidade começa com Santo ---> {san}')