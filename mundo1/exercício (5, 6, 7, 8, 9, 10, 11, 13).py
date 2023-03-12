while True:

    # mostra ao user os exercícios disponiveis
    print('''Neste ficheiro tenho disponivel os seguintes exercícios:
    >>>(5)> Digitar um numero, para o computador apresentar o numero antecessor e sucessor.
    >>>(6)> Criar um algoritmo que leia um numero e mostre o seu dobro, triplo e raiz quadrada.
    >>>(7)> Calcular a média de duas notas escolares.
    >>>(8)> Conversor de medidas, metros para centímetros.
    >>>(9)> Mostrar a tabuada de um numero inserido pelo o USER.
    >>>(10)> Converter EUR para REAIS e DOLARES.
    >>>(11)> Ler a dimensão de uma parede e calcular a sua área quadrada,\nmostrando qual seria a quantidade de tinta necessária para pitar toda a área em Litros. 
    >>>(12)> Venda de um carro com 23% sobre o valor, se for empresa.
    >>>(13)> Indica qual é o salario atual e qual o aumento que irá receber, apresentado o valor final e a percentagem de aumento.
    ''')

    # pergunta ao utilizador qual exercício deseja visualizar
    exer = int(input('Digite o número do exercício que deseja visualizar: '))

    ####Exercício 5####

    if exer == 5:

        print('-' * 20, 'Exercício 5', '-' * 20)

        # Pergunta ao utilizador uma medida em metros
        num = int(input('Digite uma medida em metros: '))

        # calcula o antecessor
        nummais = num + 1

        # calcula o sucessor
        nummenos = num - 1

        # escreve os resulados
        print(f'O número digitado é {num}, e o antecessor é {nummenos}, e o sucessor é {nummais}')

        # pergunta se deseja voltar ao inicio ou acabar o codigo
        repetir = input('Deseja exprimentar outro exercício(S ou N): ').lower()
        if repetir == 's':
            continue
        else:
            print('Espero que tenha gostado, adeus!')
            break

    ####Exercício 6####

    if exer == 6:

        print('-' * 20, 'Exercício 6', '-' * 20)

        # pergunta ao utilizador um número
        num1 = int(input('Digite um número: '))

        # calcula o dobro
        dobro = num1 * 2

        # calcula o triplo
        triplo = num1 * 3

        # calcula o raiz quadrada
        raiz = num1 ** 0.5

        # apresenta os resultados
        print(
            f'O número original é {num1},\no seu dobro é {dobro}, \n5o seu triplo {triplo} \ne o sua raiz quadrada é {raiz}')

        # pergunta se deseja voltar ao inicio ou acabar o codigo
        repetir = input('Deseja exprimentar outro exercício(S ou N): ').lower()
        if repetir == 's':
            continue
        else:
            print('Espero que tenha gostado, adeus!')
            break

    ####Exercício 7####

    if exer == 7:

        print('-' * 20, 'Exercício 7', '-' * 20)

        # pergunta a primeira nota
        nota1 = int(input('Escreva uma nota: '))

        # pergunta a segunda nota
        nota2 = int(input('escreva outra nota: '))

        # calcula a media
        resultado = (nota1 + nota2) / 2

        # apresenta a média
        print(f'A sua média é {resultado}')

        # pergunta se deseja voltar ao inicio ou acabar o codigo
        repetir = input('Deseja exprimentar outro exercício(S ou N): ').lower()
        if repetir == 's':
            continue
        else:
            print('Espero que tenha gostado, adeus!')
            break

    ####Exercício 8####

    if exer == 8:

        print('-' * 20, 'Exercício 8', '-' * 20)

        while True:

            # pergunta se o user quer fazer a conversão de metros para centimetros ou de centimetros para metros
            mece = input('Deseja fazer a conversão de metros para centimetros(metros),\nou de centimetros para metros(cent): ')

            if mece == 'metros':

                # pergunta ao user qual número em metros que quer passar para centimetros
                metros = float(input('Digite o número em metros: '))

                # calcula os centimetros
                cent = float(metros * 100)

                # apresenta o resultado em centimetros
                print(f'O valor {metros:.2f} metros convertidos são {cent:.2f} centimetros')

            elif mece == 'cent':

                # pergunta ao user qual número em metros que quer passar para centimetros
                metros = float(input('Digite o número em centimetros: '))

                # calcula os metros
                cent = float(metros / 100)

                # apresenta o resultado em centimetros
                print(f'O valor {metros:.2f} centimetros convertidos são {cent:.2f} metros')

            # pergunta se o user deseja converter outro valor
            valor = input('Deseja converter outro valor(S ou N): ').lower()

            if valor == 's':
                continue
            else:
                break

        # pergunta se deseja voltar ao inicio ou acabar o codigo
        repetir = input('Deseja exprimentar outro execício(S ou N): ').lower()
        if repetir == 's':
            continue
        else:
            print('Espero que tenha gostado, adeus!')
            break

    ####Exercício 9####

    if exer == 9:

        print('-' * 20, 'Exercício 9', '-' * 20)

        # pergunta o número que o user deseja saber a tabuada
        tab = int(input('Digite o número do qual deseja saber a tabuada: '))

        # apresenta a tabuada do número requisitado
        print(f'''A tabuada do número {tab} é:
        >>> 1 x {tab} = {tab};
        >>> 2 x {tab} = {tab * 2};
        >>> 3 x {tab} = {tab * 3};
        >>> 4 x {tab} = {tab * 4};
        >>> 5 x {tab} = {tab * 5};
        >>> 6 x {tab} = {tab * 6};
        >>> 7 x {tab} = {tab * 7};
        >>> 8 x {tab} = {tab * 8};
        >>> 9 x {tab} = {tab * 9};
        >>> 10 x {tab} = {tab * 10};
        ''')

        # pergunta se deseja voltar ao inicio ou acabar o codigo
        repetir = input('Deseja exprimentar outro exercício(S ou N): ').lower()
        if repetir == 's':
            continue
        else:
            print('Espero que tenha gostado, adeus!')
            break

    ####Exercício 10####

    if exer == 10:

        print('-' * 20, 'Exercício 10', '-' * 20)

        # pede um valor em euro ao user
        euro = float(input('Digite um valor em euro: '))

        # converte para reais
        reais = euro * 5.45

        # converte para dollar
        dolar = euro * 1.06

        while True:
            # pergunta ao user se quer converter para dólar ou reais
            redo = input('Quer converter para dólar ou reais: ').lower()

            if redo == 'reais':
                # apresenta o valor convertido para reais
                print(f'O valor {euro:.2f}€ são R${reais:.2f}')

                # verifica se deseja converter para outra moeda
                conv = input('Deseja converter para outra moeda(S ou N): ').lower()

                if conv == 's':
                    continue
                else:
                    break

            elif redo == 'dolar':
                print(f'O valor {euro:.2f}€ são US${dolar:.2f}')

                # verifica se deseja converter para outra moeda
                conv = input('Deseja converter para outra moeda(S ou N): ').lower()

                if conv == 's':
                    continue
                else:
                    break
        # pergunta se deseja voltar ao inicio ou acabar o codigo
        repetir = input('Deseja exprimentar outro exercício(S ou N): ').lower()
        if repetir == 's':
            continue
        else:
            print('Espero que tenha gostado, adeus!')
            break

    ####Exercício 11####

    if exer == 11:

        print('-' * 20, 'Exercício 11', '-' * 20)

        # pergunta largura da parede em metros
        larg = float(input('Qual a largura da parede em metros: '))

        # pergunta altura da parede em metros
        alt = float(input('Qual a altura da parede em metros: '))

        # calcula a área
        area: float = larg * alt

        # apresenta a área da parede em metros quadrados
        print(f'A área da parede têm {area:.2f}m^2')

        # pergunta se deseja saber a quantidade tinta necessaria para pintar a parede
        nec = input('Deseja saber a tinta necessaria para pintar a parede(S ou N): ').lower()

        if nec == 's':
            # pergunta o número demãos que deseja utilizar
            demaos = int(input('Qual a quantidade demãos que deseja utilizar na parede: '))

            # pergunta o rendimento da tinta em metro quadrado (geralmete encontra-se na embalagem)
            rend = float(input('Qual o rendimento da tinta em metro quadrado\n(geralmente encontra-se na embalagem): '))

            # calcula a quantidade de tinta necessaria para pintar a parede
            cal = rend / demaos
            tinta = area / cal

            # apresenta a quantidade de tinta necessaria para pintar a parede
            print(f'A Quantidade tinta necessaria para pintar a parede é {tinta:.2f}l')

        # pergunta se deseja voltar ao inicio ou acabar o codigo
        repetir = input('Deseja exprimentar outro exercício(S ou N): ').lower()
        if repetir == 's':
            continue

        else:
            print('Espero que tenha gostado, adeus!')
            break

    ####Exercício 12####

    if exer == 12:

        print('-' * 20, 'Exercício 12', '-' * 20)

        print('O exercício 12 não esta disponivel, estara disponivel em outro file, peço desculpa!')

        # pergunta se deseja voltar ao inicio ou acabar o codigo
        repetir = input('Deseja exprimentar outro exercício(S ou N): ').lower()
        if repetir == 's':
            continue

        else:
            print('Espero que tenha gostado, adeus!')
            break

    ####Exercício 13####

    print('-' * 20, 'Exercício 13', '-' * 20)

    if exer == 13:

        # pergunta qual o salario atual do user
        salat = float(input('Qual o seu salario atual: '))

        # pergunta qual o aumento que irá receber
        aume = float(input('Qual o aumento que irá receber: '))

        # calcula a em percentagem o aumento de salario do user
        perce = aume * 100 / salat

        # apresenta o aumento em percentagem ao user
        print(f'O seu salario({salat:.2f}€), com o aumento de {aume:.2f}€,\nficara mais alto em {perce:.2f}%.')

        # pergunta se deseja voltar ao inicio ou acabar o codigo
        repetir = input('Deseja exprimentar outro exercício(S ou N): ').lower()
        if repetir == 's':
            continue

        else:
            print('Espero que tenha gostado, adeus!')
            break