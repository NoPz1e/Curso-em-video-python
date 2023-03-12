## Manipulando Texto

frase = ('Curso em video Python')

# apresenta o comprimento da frase
print(f'A frase tem {len(frase)} caracteres')

# apresenta quantas vezes aparece uma letra, palavra, etc
print(frase.count('o'))

# encontra algo no texto
print(frase.find('deo'))

# apresenta se tem ou não algo na frase
print('Curso' in frase)

# troca algo na frase
print(frase.replace('Python', 'Android'))

# troca a frase para maiusculas
print(frase.upper())

# troca a frase para minosculas
print(frase.lower())

# troca a frase para minusculas mas a primeira letra em maiusculas
print(frase.capitalize())

# troca a primeira letra de cada palavra para maiuscula
print(frase.title())

frase2 = '   Aprenda Python  '
print(frase2)

# retira todos os espaços inuteis no inicio e no final
print(frase2.strip())

frase2 = '   Aprenda Python  '

# retira os espaços inuteis no lado direito
print(frase2.rstrip())

# retira os espaços inuteis no lado esquerdo
print(frase2.lstrip())

# divide a frase com forme os espaços
frase3 = frase.split()
print(frase3)


# Junta a frase que estao na lista
print('-'.join(frase3))