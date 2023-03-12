num = int(input('Digite um número: '))
numtest = 2
nprimo = bool(False)

for num in range(2,num):
    if (num // numtest == 0)  :
        nprimo = bool(True)
        print('aa')

print(f'O número não é primo ------> {nprimo}')
