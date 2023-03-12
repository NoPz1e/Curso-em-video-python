## Utilizando Módulos ##

#### forma basica de importar(importa todas as funcionalidades do módulo)
#import bebida

#### forma de importar uma coisa especifica(importa as funcinalidades escolhidas por mim)
#from doce import pudim

from math import sqrt, floor

num = int(input('Digite um número: '))
raiz = sqrt(num)

print(f'A raiz de {num} é igual a {floor(raiz)}')

# utilizar o biblioteca random
import random

num = random.randint(1,10)

print(num)

import emoji

print(emoji.emojize('Olá, Mundo :earth_americas:', language='alias'))