## Desafio 26
'''
Faça um programa que leia uma frase pelo 
teclado e mostre:
>Quantas vezes aparece a letra "a"
>Em que posição ela aparece a primeira vez.
>Em que posição ela aparece na ultima vez.
'''

# pede uma frase ao utilizador
frase = str(input('Digite uma frase: ')).upper().strip()

# conta as vezes que aparece a letra A na frase
a = frase.count('A')

# apresenta quantas vezes aparece a letra A
print(f'A letra A aparece {a} vezes na frase')

# encontra a primeira letra A
a1 = frase.find('A')+1

# apesenta onde esta a primeira letra A
print(f'A primeira letra A aparece na posição {a1}')

# encontra a ultima letra A
a2 = frase.rfind('A')+1

# apresenta onde esta a ultima letra A
print(f'A ultima letra A pareceu na posição {a2}')