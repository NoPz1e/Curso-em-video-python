## condições

nome = input('Qual é o seu nome? ')

if nome == 'Cristiano':
    print('Que nome lindo você tem!')
else:
    print('O seu nome é tao normal!')
print(f'Bom dia, {nome}!')

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2

print(f'A sua média foi {media:.1f}')

if media >= 10.0:
    print('Sua media foi boa! PARABÉNS')
else:
    print('Sua média foi uma porcaria! Estude mais!')