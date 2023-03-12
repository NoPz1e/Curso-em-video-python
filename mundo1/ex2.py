###Vender carro####
print('='*20,'bem-vindo','='*20)

####Stock e preços sem iva####
#mercedes#
claS = 1
claP = 20000

#repitição#
while True:

    #Escolher marca do carro#
    print('-'*70)
    print('Temos disponível carros das seguintes marcas: Mercedes, Nissan, Ford')
    marca = input('De qual marca deseja ver os carros disponíveis: ').lower()

    #Apresenta e escolhe um modelo Mercedes#
    if marca == "mercedes":

        #Escolhe um modelo dos três apresentados#
        print('Da marca Mercedes temos diponível os modelos:\n >>>> Mercedes-AMG Classe C Limousine(1),\n >>>> Mercedes-AMG G 63(2),\n >>>> Mercedes-AMG CLA Shooting Brake(3).')

        modeloM = int(input('Escolha modelo para ver o seu preço\n (digite apenas o número que corresponde ao modelo dele): ' ))
        if modeloM == 1:

            #Verificação de stock#
            if claS == 0:
                semstock = input('O modelo que selecionou não temos em stock, deseja ver o preço mesmo assim(S ou N): ').lower()
                if semstock == 's':
                    #Verifica se é Particular ou Empresa#
                    parenp1 = input('Sé for particular digite P e empresa digite E: ').lower()
                    if parenp == 'p':
                        print(f'O preço do carro é de {claP*1.23:.3f}€')
                    elif parenp == 'e':
                        print(f'O preço do carro é de {claP:.3f}€')

                    #verifica se quer escolher outro carro#
                    mais_carro = input('Deseja escolher outro modelo(S ou N): ').lower()
                    if mais_carro == 's':
                        continue
                    else:
                        break
                else:
                    print('Obrigado, espero que volte!')
                    break

    #Verifica se é Particular ou Empresa#
    parenp = input('Sé for particular digite P e empresa digite E: ').lower()
'''
            if parenp == 'p':
                print(f'O preço do carro é de {claP*1.23:.3f}€')

                #Compra do carro#
                comprar = input('Deseja adquirir este carro(S ou N): ').lower()
                if comprar == 's':
                    print('Compra efetuada com susseso, sua encomenda chegara dentro de 5 dias')
                    claS -= 1
                    mais_carro = input('Deseja comprar mais algum carro(S ou N): ').lower()

                    if mais_carro == "s":
                        continue

                    else:
                        print('Obrigado por comprar conosco!')
                        break

                else:
                    #Pergunta ao utilizador se quer visualizar outro carro#
                    veroutro = input('Deseja ver outro carro(S ou N): ').lower()
                    if veroutro == 's':
                        continue
                    else:
                        print('Obrigado!')
                        break


            elif parenp == 'e':
                print(f'O preço do carro é de {claP:.3f}€')

                #Compra do carro#
                comprar = input('Deseja adquirir este carro(S ou N): ').lower()
                if comprar == 's':
                    print('Compra efetuada com susseso, sua encomenda chegara dentro de 5 dias')
                    claS -= 1
                    mais_carro = input('Deseja comprar mais algum carro(S ou N): ').lower()
                    if mais_carro == "s":
                        continue

                    else:
                        print('Obrigado por comprar conosco!')
                        break

                else:
                    #Pergunta ao utilizador se quer visualizar outro carro#
                    veroutro = input('Deseja ver outro carro(S ou N): ')
                    if veroutro == 's':
                        continue
                    else:
                        print('Obrigado!')
                        break
'''