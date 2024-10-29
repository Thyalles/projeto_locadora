carros={}
import json
import re
arquivo = os.path.join(os.path.dirname(__file__), 'cadastro_dos_carros.json')


def carregar_carros():
    # Verifica se o arquivo existe, se não existir, cria um arquivo com lista vazia
    if not os.path.exists(arquivo):
        with open(arquivo, 'w') as f:
            json.dump({}, f, indent=4)
    
    # Carrega o conteúdo do arquivo
    with open(arquivo, 'r') as f:
        return json.load(f)

def preencher_marca_carro():
    global marca_carro
    marca_carro=input("Marca do carro: ")
    while True:
        try:
            validar=int(input(f'Confirma que a marca está correta?\n{marca_carro}\n1-Sim\n2-Não\n'))
            match validar:
                case 1:
                    return marca_carro
                case 2:
                    marca_carro= input("Marca do carro: ")
                case _:
                    print("Opção invalida")
                    continue
        except:
            print("Formato invalido! Por favor, insira 1 ou 2.")        

def preencher_modelo_carro():
    global modelo_carro
    modelo_carro=input("Modelo do carro: ")
    while True:
        try:
            validar=int(input(f'Confirma que o modelo está correto?\n{modelo_carro}\n1-Sim\n2-Não\n'))
            match validar:
                case 1:
                    return modelo_carro
                case 2:
                    modelo_carro= input("Marca do carro: ")
                case _:
                    print("Opção invalida")
                    continue
        except:
            print("Formato invalido! Por favor, insira 1 ou 2.")        

def preencher_ano_fabricacao():    
       while True:    
            global ano_fabricacao 
            ano_fabricacao=input("Ano de fabricação: (aaaa)")
            if len(ano_fabricacao) == 4:
                while True:
                    try:
                        validar = int(input(f'Confirma o ano de fabricação?\n{ano_fabricacao}\n1-Sim\n2-Não\n'))

                        match validar:
                            case 1:
                                return ano_fabricacao
                            case 2:
                               preencher_ano_fabricacao()
                            case __:
                                print("Opção invalida!")
                                continue
                
                    except:
                        print("Formato invalido! Por favor, insira 1 ou 2.")
            else:
                
                continue

def preencher_placa():
    while True:
        global placa_carro
        placa_carro=input("Informe a placa do carro: ")
        padrao = r'^[A-Z]{3}\d[A-Z]{1}\d{2}$'
        if re.match (padrao, placa_carro):
           
            while True:
                try:
                    
                    validar = int(input(f'Confirma sua Placa?\n{placa_carro}\n1-Sim\n2-Não\n'))

                    match validar:
                        case 1:
                            return placa_carro
                        case 2:
                            preencher_placa()
                        case __:
                            print("Opção invalida!")
                            continue
                
                except:
                    print("Formato invalido! Por favor, insira 1 ou 2.")

    
        else:
            print("Formato invalido!")
            continue
        
def preencher_chassi_carro():
    while True:      
        global chassi_carro  
        chassi_carro=input("Informe o chassi do carro: ")
        padrao = r'^[A-HJ-NPR-Z0-9]{17}$'
        if re.match (padrao, chassi_carro):
           
            while True:
                try:
                    
                    validar = int(input(f'Confirma seu Chassi?\n{chassi_carro}\n1-Sim\n2-Não\n'))

                    match validar:
                        case 1:
                            return chassi_carro
                        case 2:
                            preencher_chassi_carro()
                        case __:
                            print("Opção invalida!")
                            continue
                
                except:
                    print("Formato invalido! Por favor, insira 1 ou 2.")
        else:
            print("Formato invalido!")
            continue

def preencher_cor_carro():  
    global cor_carro      
    cor_carro=input("Informe a cor do carro: ")
    while True:
        try:
            validar =int(input(f'Confirma a cor?\n{cor_carro}\n1-Sim\n2-Não\n'))
            match validar:
                case 1:
                        return cor_carro
                case 2: 
                    cor_carro=input("Informe a cor do carro: ")
                case _:
                    print("Opção invalida!")
                    continue
        except:
            print("Formato invalido! Por favor, insira 1 ou 2.")


def preencher_tipo_carro():  
    global tipo_carro      
    tipo_carro=input("Informe o tipo do carro: ")
    while True:
        try:
            validar =int(input(f'Confirma o tipo do caaro?\n{tipo_carro}\n1-Sim\n2-Não\n'))
            match validar:
                case 1:
                        return tipo_carro
                case 2: 
                    tipo_carro=input("Informe o tipo do carro: ")
                case _:
                    print("Opção invalida!")
                    continue
        except:
            print("Formato invalido! Por favor, insira 1 ou 2.")

def preencher_quilometragem_carro():
    while True:
        global quilometragem_carro
        quilometragem_carro=int(input("Informe a quilometragem do carro: "))
        if isinstance(quilometragem_carro, (int, float)) and quilometragem_carro >= 0:
            while True:
                try:
                    validar =int(input(f'Confirma a quilometragem do carro?\n{quilometragem_carro}\n1-Sim\n2-Não\n'))
                    match validar:
                        case 1:
                                return quilometragem_carro
                        case 2: 
                            preencher_quilometragem_carro()
                        case _:
                            print("Opção invalida!")
                            continue
                except:
                    print("Formato invalido! Por favor, insira 1 ou 2.")
        else:
            print("Opção invalida")
            continue

def preenncher_combustivel_carro(): 
    global combustivel_carro       
    combustivel_carro=input("Informe o tipo do combustível do carro: ")
    while True:
        try:
            validar =int(input(f'Confirma o tipo de combustível do carro?\n{combustivel_carro}\n1-Sim\n2-Não\n'))
            match validar:
                case 1:
                     return combustivel_carro
                case 2: 
                    combustivel_carro=input("Informe o tipo do combustível do carro: ")
                case _:
                    print("Opção invalida!")
                    continue
        except:
           print("Formato invalido! Por favor, insira 1 ou 2.")
       
        
def preencher_num_portas():         
    while True:   
        global numero_portas
        numero_portas=int(input("Quantas portas: "))
        if isinstance(numero_portas, (int)) and numero_portas >= 0:
            while True:
                try:
                    validar =int(input(f'Confirma o número de portas do carro?\n{numero_portas}\n1-Sim\n2-Não\n'))
                    match validar:
                        case 1:
                                return numero_portas
                        case 2: 
                            preencher_num_portas()
                        case _:
                            print("Opção invalida!")
                            continue
                except:
                    print("Formato invalido! Por favor, insira 1 ou 2.")
        else:
            print("Opção invalida")
            continue

def preencher_capacidade_carro():     
    while True: 
        global capacidade_carro      
        capacidade_carro=int(input("Qual a capacidade? (número de passageiros) "))
        if isinstance(capacidade_carro, (int)) and capacidade_carro >= 0 and capacidade_carro<=7:
            while True:
                try:
                    validar =int(input(f'Confirma a capacidade do carro?\n{capacidade_carro}\n1-Sim\n2-Não\n'))
                    match validar:
                        case 1:
                                return capacidade_carro
                        case 2: 
                            preencher_capacidade_carro
                        case _:
                            print("Opção invalida!")
                            continue
                except:
                    print("Formato invalido! Por favor, insira 1 ou 2.")
        else:
            print("Opção invalida")
            continue

def preencher_itens_carro():   
    global itens_carro         
    itens_carro=input("Itens de conforto e segurança (ar-condicionado, airbag, etc.):  ")
    while True:
        try:
            validar =int(input(f'Confirma os itens de conforto e segurança?\n{itens_carro}\n1-Sim\n2-Não\n'))
            match validar:
                case 1:
                        return itens_carro
                case 2: 
                     itens_carro=input("Itens de conforto e segurança (ar-condicionado, airbag, etc.):  ")
                case _:
                    print("Opção invalida!")
                    continue
        except:
            print("Formato invalido! Por favor, insira 1 ou 2.")

def preencher_condicao_carro():
    global condicao_carro            
    condicao_carro=input("Condição do veículo (novo, usado, em manutenção): ")
    while True:
        try:
            validar =int(input(f'Confirma a condição do carro?\n{condicao_carro}\n1-Sim\n2-Não\n'))
            match validar:
                case 1:
                        return condicao_carro
                case 2: 
                     condicao_carro=input("Condição do veículo (novo, usado, em manutenção): ")
                case _:
                    print("Opção invalida!")
                    continue
        except:
            print("Formato invalido! Por favor, insira 1 ou 2.")    

         
def preencher_tarifa_carro():                
    while True:
        global tarifa_carro
        tarifa_carro=float(input("Qual o valor da tarifa diaria?  "))
        
        if isinstance(tarifa_carro, (int, float)) and tarifa_carro >= 0:
            while True:
                try:
                    validar =int(input(f'Confirma a tarifa diaria?\n{tarifa_carro}\n1-Sim\n2-Não\n'))
                    match validar:
                        case 1:
                                return tarifa_carro
                        case 2: 
                            preencher_tarifa_carro
                        case _:
                            print("Opção invalida!")
                            continue
                except:
                    print("Formato invalido! Por favor, insira 1 ou 2.")
        else:
            print("Opção invalida")
            continue

def cadastrar_carro():
    while True:
        try:
            menu_cadastro_carros()

            preencher_marca_carro()

            preencher_modelo_carro()

            preencher_ano_fabricacao()

            preencher_placa()

            preencher_chassi_carro()

            preencher_cor_carro()

            preencher_tipo_carro()

            preencher_quilometragem_carro()

            preenncher_combustivel_carro()

            preencher_num_portas()

            preencher_capacidade_carro()

            preencher_itens_carro()

            preencher_condicao_carro()

            preencher_tarifa_carro()

            cadastro_sucesso()
        except:
            continue
        resp=input("Deseja Voltar ao menu? (s/n) ")
        if resp =='s' or resp =="S":
            menu_adm()
        else:
            print("Volte sempre!")
            break    
   

def cadastro_sucesso():             

    carros=carregar_carros()                   
                       
    carros[placa_carro]={"Marca do carro": marca_carro,"Modelo": modelo_carro, "Ano de fabricação": ano_fabricacao,"Chassi": chassi_carro,"Cor do carro": cor_carro,"Tipo do carro": tipo_carro,"Quilometragem": quilometragem_carro,"Tipo de combustível": combustivel_carro,"Número de portas": numero_portas,"Capacidade": capacidade_carro,"Itens de conforto": itens_carro,"Condição do veículo": condicao_carro,"Tarifa": tarifa_carro}                                                                                                  
                       
    with open(arquivo, 'w' ) as f:
      json.dump(carros, f, indent=4, ensure_ascii=False) 

    print("Cadastro feito com sucesso!!")
