# AVISO ||| TUDO QUE FOR ESCRITO FORA DAS ASPA NO PYTHON TERÁ DE SER MIN OU VAI DAR MERD@ OK ???? BOA

# Printar um texto na tela
print('Hello World!')

# Printar um calculo na tela
print(5+5)

# Printar na tela numeros
print('5' + '5')

#Usar tanto texto como números (neste caso, se usar o (+) em vez da (,)ele vai dar erro.
print('Olá', 5)

# Para representar um texto na tela é sempre necessário usar aspas simple, já para representação de calculo já não é necessario aspas.

# ---------------------------------VARIAVEIS------------------------------------
# Em python todas as variaveis são um obj
# Todas as variaveis recebem algo com o sinal de =

nome = 'Cristiano'
idade = 16
peso = 64.6

print (nome, idade, peso)
print ('Meu nome é', nome,'tenho', idade,'anos e peso', peso)

# Input, questiona o USER sobre algo, e guarda dentro da varialvel esse valor que o USER escreveu

nome = input('Qual é o teu nome? ')
idade = input('Qual é a tua idade? ')
peso = input('Qual é o teu peso? ')

print (nome, idade, peso)
print ('Agora sei que o seu nome é', nome, 'e a sua idade é', idade, 'e o seu peso é', peso, 'kg.')

# Exemplo de codigo que pode dar errado(pois eu quero que ele some, e ele esta a juntar apenas, pois coloquei aspas onde não devia)

print('-------------------------Codigo errado---------------------------')
n1 = input('First number is? ')
n2 = input('Second number is? ')
soma = n1 + n2
print('A soma dos meus número é', soma)

##############################################
#CODIGO CERTO PARA FAZER SOMA SERIA ENTÃO ####
##############################################

#Pois, para que ele faça junção (concatenar) eu tenho de definir o TIPO PRIMITIVOS que pode ser (int: para números inteiros) (float: para números decimais) (bool: sistema boolano) (str: que representa apenas TEXTO)

# SE NENHUM TIPO PRIMITIVO FOR DEFINIDO, AUTOMATICAMENTE ELE IRA COLOCAR COMO PADRÃO O PRIMITIVO ------STR------

print('--------------------------Codigo certo---------------------------')
n1 = int(input('Qual é o número? '))
n2 = int(input('Qual é o segundo número? '))
soma = n1 + n2
print('A soma dos meus números é', soma)

# Mas existe uma forma mais facil de printar os dados(com o ".format()") podemos escrever apenas uma str com as chaves que vão buscar as variaveis ao format por ordem

# Mas desta vez vou usar a frase "A soma é x utilizei o valor x com o valor x"

print('A soma é {} utilizei o valor {} e fscom o valor {}'.format(soma, n1 , n2))

# FORMA MAIS RECENTE DE FORMATAÇÃO DE TEXTO

print(f'O valor da soma é {soma}')

# Verificar qual o primitivo do valor numa variavel com (isalpha: para verificar se tem letra) (isnumeric: para verificar se tem números) (isalnum: para verificar se tem letra e números)

teste = input('Digite algo: ')

# Verifica se o valor da variavel n tem letras e se for verdade devolve true senão false
print(f'A variavel tem só letras ----> {teste.isalpha()}')

# Verifica se o valor da variavel n tem número e se for verdade devolve true senão false
print(f'A varialvel tem só números ----> {teste.isnumeric()}')

# Verifica se o valor da variavel n tem número e letras e se for verdade for devolve true senão false
print(f'A varialvel tem números ou letras ----> {teste.isalnum()}')
