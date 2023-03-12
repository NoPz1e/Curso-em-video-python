####Operadores aritemeticos####
# Os operadores aritemeticos são (+ - * / // ** %), e eles seguem uma ordem de precedencia que deriva de matatematicas base, #### 1º () 2º** 3º + / // % 4º + - ####

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))

s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
rd = n1 % n2
e = n1 ** n2

print(f'A soma é {s},\nA multiplicação é {m},\nA divisão é {d},\nA divisão inteira {di},\nO resto da divisão é {rd},\nA potencia {e}')