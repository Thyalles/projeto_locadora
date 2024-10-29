def menu_carros():
    try:
            opc_menu_carro=int(input("Selecione a opção :\n (1) Cadastrar um carro \n (2) Altualizar \n (3) Ver carros cadastrados \n (4) Exluir carro cadastrado \n (5) Voltar ao menu anterior"))
            match opc_menu_carro:
                case 1: 
                    cadastrar_carro()
                case 2: 
                    atualizar_carro()
                case 3:
                    vizualizar_carros()
                case 4: 
                    exlcluir_carro()         
                case 5:
                    print("Voltando ao menu anterior!")
                    menu_adm()
                case _:
                    opcao_invalida_principal()
                    menu_adm()
    except:
            opcao_invalida_principal()
            menu_adm()