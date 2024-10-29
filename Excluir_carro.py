def excluir_carro():

    #carregando o json
    carros=carregar_carros()
    for placa_carros in carros:
        print(placa_carros)
    while True:
        try:
            excluir_carro=input("Qual carro você deseja excluir? \n")
            if excluir_carro in carros:
                confirm_excluir=int(input("Deseja realmente excluir? 1 - sim / 2 - Não \n"))
                match confirm_excluir:
                    case 1:
                        carros.pop(excluir_carro)
                        for placa_carros in carros:
                            print("Carros restantes:", placa_carros)
                        print("Excluido com sucesso")
                        
                        #Salvando as alterações no Json
                        salvar_dados(arquivo,carros)
                    
                    case 2:
                        print("Voltando")
                        menu_adm()
                    case _:
                        print("Opção invalida")
                        continue
            else:
                print("Não encontrado! tente novamente")
                continue        
        except: 
            print("Valor invalido, tente novamente")
            menu_adm()