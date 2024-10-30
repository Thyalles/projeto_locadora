#Buscar e/ou listar os carros cadastrados
def buscar_carro():
    
    #carregar os dados do json
    carros=carregar_carros()
    while True:
        try:
            resp_buscar_carro=int(input("Para visualizar todos os carros digite (1) \n Para Buscar um carro específico, digite (2) \n Para sair, digite (3) \n"))
            match resp_buscar_carro:
                case 1:
                    for carros in carros:
                        print(carros)
                case 2:
                    buscador_carro=input("Digite qual carro você quer conferir \n")
                    if buscador_carro in carros:
                        
                        print(carros[buscador_carro])
                        break
                    else:
                        print("Não encontrado, tente novamente")
                        continue
                case 3:
                    print("Saindo")
                    menu_adm()
                case _:
                    print("Valor invalido, tente novamente")
                    continue    
        except:
            print("Valor invalido, tente novamente")
            menu_adm()
