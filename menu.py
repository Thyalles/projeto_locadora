import os
import re
import json
import time
from datetime import datetime
arquivo = os.path.join(os.path.dirname(__file__), 'cadastro_dos_carros.json')

def menu_carros():
    os.system('cls')
    try:
            opc_menu_carro=int(input("Selecione a opção :\n (1) Cadastrar um carro \n (2) Altualizar \n (3) Excluir um carro \n (4) Buscar carro cadastrado \n (5) Voltar \n"))
            match opc_menu_carro:
                case 1: 
                    cadastrar_carro()
                    menu_adm()
                case 2: 
                    atualizar_carro()
                    menu_adm()
                case 3:
                    excluir_carro()
                    menu_adm()
                case 4:
                    buscar_carro() 
                    menu_adm()
                case 5:
                    print("Voltando ao menu anterior!")
                    menu_adm()
                case _:
                    opcao_invalida_principal()
                    menu_adm()
    except:
            opcao_invalida_principal()
            menu_adm()

#Buscar e/ou listar os carros cadastrados
def buscar_carro():
    
    #carregar os dados do json
    carros=carregar_carros()
    while True:
        try:
            resp_buscar_carro=int(input(" (1) Visualizar todos os carros \n (2) Buscar um carro específico \n (3) Sair \n"))
            match resp_buscar_carro:
                case 1:
                    for veiculos in carros:
                        print("=" *50)
                        print("LISTA DE CARROS:")
                        print("-" *50)
                        print(f"Marca: {carros.get(veiculos).get('Marca do carro')} || Modelo: {carros.get(veiculos).get('Modelo')}  || Placa: {carros.get(veiculos).get('Placa')} ||  Ano de Fabricação: {carros.get(veiculos).get('Ano de fabricação')} ||  Chassi: {carros.get(veiculos).get('Chassi')} ||  Cor: {carros.get(veiculos).get('Cor do Carro')} || Tipo do carro: {carros.get(veiculos).get('Tipo do carro')} ||  Quilometragem: {carros.get(veiculos).get('Quilometragem')} ||  Combustivél: {carros.get(veiculos).get('Tipo de Combustível')} ||  Número de portas: {carros.get(veiculos).get('Número de portas')} ||  Capacidade: {carros.get(veiculos).get('Capacidade')}  || Condição do veículo: {carros.get(veiculos).get('Condição do veículo')} || Tarifa: {carros.get(veiculos).get('Tarifa')}, ") 
                        print("=" *50)
                        print("-" *50)    
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



#Exluir um carro cadastrado do dicionario
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


def carregar_carros():
    # Verifica se o arquivo existe, se não existir, cria um arquivo com lista vazia
    if not os.path.exists(arquivo):
        with open(arquivo, 'w') as f:
            json.dump({}, f, indent=4)
    
    # Carrega o conteúdo do arquivo
    with open(arquivo, 'r') as f:
        return json.load(f)

def menu_cadastro_carros():
    os.system('cls')    
    print(" Bem Vindo ")
    print(" Para cadastrar os carros, insira as informações a seguir:  ")

def carregar_dados():
   with open ('cadastro_dos_carros.json', 'r') as arquivo:
    return json.load(arquivo)

def salvar_dados(arquivo, carros):
    with open(arquivo, 'w' ) as f:
      json.dump(carros,f, indent=4)   

def atualizar_carro():
   carros=carregar_carros()
   
   
    
   while True:
      for veiculos in carros:
        print("=" *50)
        print("LISTA DE CARROS:")
        print("-" *50)
        print(f"Marca: {carros.get(veiculos).get('Marca do carro')} || Modelo: {carros.get(veiculos).get('Modelo')}  || Placa: {carros.get(veiculos).get('Placa')} ||  Ano de Fabricação: {carros.get(veiculos).get('Ano de fabricação')} ||  Chassi: {carros.get(veiculos).get('Chassi')} ||  Cor: {carros.get(veiculos).get('Cor do Carro')} || Tipo do carro: {carros.get(veiculos).get('Tipo do carro')} ||  Quilometragem: {carros.get(veiculos).get('Quilometragem')} ||  Combustivél: {carros.get(veiculos).get('Tipo de Combustível')} ||  Número de portas: {carros.get(veiculos).get('Número de portas')} ||  Capacidade: {carros.get(veiculos).get('Capacidade')}  || Condição do veículo: {carros.get(veiculos).get('Condição do veículo')} || Tarifa: {carros.get(veiculos).get('Tarifa')}, ") 
        print("=" *50)
        print("-" *50)    
      try:
         placa_carros=input("Informe a placa do carro que você deseja alterar: ")
         if placa_carros in carros:
            chave_carros=(input(" Qual dado voce gostaria de atualizar? "))
            if chave_carros in carros[placa_carros]:
                novo_valor=input("Informe o novo dado: ")
                carros[placa_carros][chave_carros]=novo_valor
                salvar_dados(arquivo,carros)
                print(carros)
            else:
                print("Dado não encontrado, tente novamente")
                menu_adm()    
      except:
         print("Valor invalido")
         menu_adm()  

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
        try:
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


        except:
            print("Por favor, inserir apenas digitos!")
        
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
    os.system('cls')
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
                       
    carros[placa_carro]={"Placa": placa_carro,"Marca do carro": marca_carro,"Modelo": modelo_carro, "Ano de fabricação": ano_fabricacao,"Chassi": chassi_carro,"Cor do carro": cor_carro,"Tipo do carro": tipo_carro,"Quilometragem": quilometragem_carro,"Tipo de combustível": combustivel_carro,"Número de portas": numero_portas,"Capacidade": capacidade_carro,"Itens de conforto": itens_carro,"Condição do veículo": condicao_carro,"Tarifa": tarifa_carro}                                                                                                  
                       
    with open(arquivo, 'w' ) as f:
      json.dump(carros, f, indent=4, ensure_ascii=False) 


# Caso insira uma opcao invalida, o usuario precisara aperta 
# alguma tecla para voltar ao menu inicial.
def opcao_invalida_principal():
    print("Opção Invalida!")
    input("Digite uma tecla para voltar ao menu\n")

# Preenchendo o nome completo do cliente
def preencher_nome_cliente():     

    nome = input("Informe seu nome completo\n")
    
    while True:
        try:
            validar = int(input(f'Confirma que o seu nome esta correto?\n{nome}\n1-Sim\n2-Não\n'))

            match validar:
                case 1:
                    return nome
                case 2:
                     nome = input("Informe seu nome completo\n")
                case __:
                    print("Opção invalida!")
                    continue
        
        except:
            print("Formato invalido! Por favor, insira 1 ou 2.")


# Preenchendo a data de nascimento e idade do cliente
def preencher_data_nascimento():
    while True:

        data = input("Infome sua data de nascimento(ddmmaaaa): (apenas números!)\n")

        # Confirma se foi digitado apenas numeros e tem 8 digitos de entrada
        if len(data) == 8 and data.isdigit():
            data_formatada = f"{data[:2]}/{data[2:4]}/{data[4:]}"
        else:
            print("Formato de data inválido! Por favor, use o formato DDMMAAAA.")
            continue

        try:
            # Converte a data formatada para o formato da biblioteca DATETIME
            data_nasc = datetime.strptime(data_formatada, f"%d/%m/%Y")
            
            # Calcula quantos anos o cliente tem
            anos = datetime.now().year - data_nasc.year
            
            # Valida se o aniversario do cliente ainda não aconteceu, se verdade ele retira 1 ano 
            if (datetime.now().month<= data_nasc.month)and(datetime.now().day < data_nasc.day):
                anos-=1
            
            # Valida a maior idade do cliente, caso falso volta ao menu do cliente
            if (anos<18):
                print("Você deve ter mais de 18 anos para se cadastrar.")
                print("Cancelando cadastro...")
                menu_cliente()
            
            while True:
                try:
                    validar = int(input(f'Confirma sua data de nascimento?\n{data_formatada}\n1-Sim\n2-Não\n'))

                    match validar:
                        case 1:
                            return data_formatada
                        case 2:
                            preencher_data_nascimento()
                        case __:
                            print("Opção invalida!")
                            continue
                
                except:
                    print("Formato invalido! Por favor, insira 1 ou 2.")
        
        except:
            print("Formato de data inválido! Por favor, use o formato DDMMAAAA.")


# verificando o CPF
def verificar_cpf(cpf):
    aux = 10
    soma_d1 = soma_d2 = 0
    d1 = d2 = 0
    nome_cpf_d1 = cpf[:9]
    nome_cpf_d2 = cpf[:10]

    for i in nome_cpf_d1:     
        soma_d1 = soma_d1 + (int(i)* aux)
        aux-=1
 
    if((soma_d1%11)<2):
        d1 = 0
    else:
        d1 = 11-(soma_d1%11)

    aux = 11

    for i in nome_cpf_d2:
        soma_d2 = soma_d2 + (int(i)*aux)
        aux-=1

    if((soma_d2%11)<2):
        d2 = 0
    else:
        d2 = 11-(soma_d2%11)

    digitos = str(d1) + str(d2)
    cpf_digitos = cpf[9:]
    
    if(digitos == cpf_digitos):        
        return True
    

# valida o cpf se ja foi cadastrado
def validar_cpf(cpf):
    try:
        dados_cliente = carregar_clientes()

        if cpf in dados_cliente:
            # CPF já cadastrado
            return False
        else:
            #CPF não cadastrado
            return True

    except:
        print("Erro ao procurar o CPF em clientes!")


# LOGAR CPF cliente
def logar_cpf():
    while True:
        
        cpf = input("Infome seu CPF: (apenas números!)\n")
        
        if len(cpf) == 11 and cpf.isdigit(): 
            while True:
                try:
                    validar = int(input(f'Confirma seu CPF?\n{cpf}\n1-Sim\n2-Não\n'))

                    match validar:
                        case 1:
                            if(verificar_cpf(cpf)):
                                print("CPF Valido!")
                                return cpf
                            else:
                                print("CPF invalido!")
                                break
                        case 2:
                            break
                        case __:
                            print("Opção invalida!")

                except:
                    print("Formato invalido! Por favor, insira 1 ou 2.")          
            
        else:
            print("CPF inválido! Por favor, use apenas 11 digitos.")


# Preenchendo o CPF
def preencher_cpf():
    while True:
        
        cpf = input("Infome seu CPF: (apenas números!)\n")
        
        if len(cpf) == 11 and cpf.isdigit(): 
            while True:
                try:
                    validar = int(input(f'Confirma seu CPF?\n{cpf}\n1-Sim\n2-Não\n'))

                    match validar:
                        case 1:
                            if(verificar_cpf(cpf) and validar_cpf(cpf)):
                                print("CPF Valido!")
                                return cpf
                            else:
                                print("CPF invalido!")
                                break
                        case 2:
                            break
                        case __:
                            print("Opção invalida!")

                except:
                    print("Formato invalido! Por favor, insira 1 ou 2.")          
            
        else:
            print("CPF inválido! Por favor, use apenas 11 digitos.")
            

# Preenchendo o RG
def preencher_rg():
    while True:

        rg = input("Infome seu RG: (apenas números!)\n")

        # Algumas identidades podem conter de 7 a 9 digitos, incluindo letra
        if len(rg) == 9 or len(rg) == 8 or len(rg) == 7:
            while True:
                try:
                    validar = int(input(f'Confirma seu RG?\n{rg}\n1-Sim\n2-Não\n'))

                    match validar:
                        case 1:
                            print("RG Valido!")
                            return rg
                        case 2:
                            break
                        case __:
                            print("Opção invalida!")

                except:
                    print("Formato invalido! Por favor, insira 1 ou 2.")  
        
        else:
            print("RG inválido! Por favor, use apenas 9 digitos.")


# Preencher a Nascionalidade
def preencher_nascionalidade():

    nascionalidade = input("Informe a sua nascionalidade: ")

    while True:
        try:
            validar = int(input(f'Confirma a sua nascionalidade?\n{nascionalidade}\n1-Sim\n2-Não\n'))

            match validar:
                case 1:
                    return nascionalidade
                case 2:
                     nascionalidade = input("Informe a sua nascionalidade: ")
                case __:
                    print("Opção invalida!")
                    continue
        
        except:
            print("Formato invalido! Por favor, insira 1 ou 2.")


# Preenchendo endereco
def preencher_endereco():
    print("Endereço\n")
    while True:

        endereco_rua = input("Rua: ")
        endereco_numero = input("Número: ")
        endereco_complemento = input("Complemento(caso necessario): ")
        endereco_bairro = input("Bairro: ")
        endereco_cidade = input("Cidade: ")
        endereco_estado = input("Estado: ")
        endereco_cep = input("CEP: ")

        try:
            os.system('cls')
            print(f'Rua: {endereco_rua}')
            print(f'Numero: {endereco_numero}')
            print(f'Complemento: {endereco_complemento}')
            print(f'Bairro: {endereco_bairro}')
            print(f'Cidade: {endereco_cidade}')
            print(f'Estado: {endereco_estado}')
            print(f'CEP: {endereco_cep}')
            validar = int(input('Confirma seu ENDEREÇO?\n1-Sim\n2-Não\n'))

            match validar:
                case 1:
                    endereco = {
                        "RUA": endereco_rua,
                        "NUMERO": endereco_numero,
                        "COMPLEMENTO": endereco_complemento,
                        "BAIRRO": endereco_bairro,
                        "CIDADE": endereco_cidade,
                        "ESTADO": endereco_estado,
                        "CEP": endereco_cep
                    }

                    return endereco

                case 2:
                    preencher_endereco()
                case __:
                    print("Opção invalida!")
        except:
            print("Formato invalido! Por favor, insira 1 ou 2.") 


# Preenchendo o telefone
def preencher_telefone():

    ddd = input("DDD(três digitos): ")
    
    if len(ddd) == 3 and ddd.isdigit():
        while True:
            celular = input("Celular: ")

            if(len(celular) == 8 or len(celular) == 9) and celular.isdigit():
                while True:
                    try:    
                        os.system('cls')
                        print(f'DDD: {ddd}')
                        print(f'Celular: {celular}')
                        validar = int(input('Confirma seu Celular?\n1-Sim\n2-Não\n'))

                        match validar:
                            case 1:
                                telefone = {
                                    "DDD": ddd,
                                    "CELULAR": celular
                                }

                                return telefone

                            case 2:
                                preencher_telefone()
                            case __:
                                print("Opção invalida!")

                    except:
                        print("Formato invalido! Por favor, insira 1 ou 2.") 

                break # break para sair do loop primeiro loop

            else:
                print("Apenas digitos para o número do celular!")

    else:
        print("DDD informado não possui 3 digitos")
        preencher_telefone()


#Preencher o Email
def preencher_email():

    mail = input("Infome seu EMAIL: \n")

    while True:
        try:
            validar = int(input(f'Confirma seu e-mail?\n{mail}\n1-Sim\n2-Não\n'))

            match validar:
                case 1:
                    print("Email salvo!")
                    return mail
                case 2:
                    mail = input("Infome seu EMAIL: \n")
                case __:
                    print("Opção invalida!")

        except:
            print("Formato invalido! Por favor, insira 1 ou 2.")


# Verificando o número da CNH
def verificar_cnh(cnh):
    aux = 11
    soma_dv = 0
    dv = 0

    for i in cnh:
        soma_dv = soma_dv + (int(i) * aux)
        aux-=1

    if (soma_dv%11)>1:
        dv = 11-(soma_dv%11)
    else:
        dv = 0

    digito = cnh[10:]
    digito_cnh = str(dv)   

    if(digito == digito_cnh):
        return True


#valida se a CNH ja foi cadastrada
def validar_cnh(cnh):
    try:
        dados_cliente = carregar_clientes()

        for cpf in dados_cliente:
            if dados_cliente[cpf]["NUMERO_CNH"] == cnh:
                return False
            else:
                return True

    except:
        print("Erro ao procurar o CPF em clientes!")


# Preencher o número da CNH
def preencher_cnh():
    while True:

        numero_cnh = input("Infome seu número da CNH: (apenas números!)\n")

        if len(numero_cnh) == 11 and numero_cnh.isdigit():
            while True:
                try:
                    validar = int(input(f'Confirma o número da sua CNH?\n{numero_cnh}\n1-Sim\n2-Não\n'))

                    match validar:
                        case 1:
                            if(verificar_cnh(numero_cnh) and validar_cnh(numero_cnh)):
                                print("Número da CNH Valido!")
                                return numero_cnh
                            else:
                                print("Número da CNH invalido!")
                                break
                        case 2:
                            break
                        case __:
                            print("Opção invalida!")

                except:
                    print("Formato invalido! Por favor, insira 1 ou 2.") 

        else:
            print("Número da CNH invalido! Por favor, use apenas 11 digitos.")


# Preencher a válidade da CNH
def preencher_validade_cnh():
    while True:
        carteira_status = False

        validade = input("Infome a data de validade da CNH(ddmmaaaa): (apenas números!)\n")

        if len(validade) == 8 and validade.isdigit():
            validade_formatada = f"{validade[:2]}/{validade[2:4]}/{validade[4:]}"
        else:
            print("Formato de data inválido! Por favor, use o formato DDMMAAAA.")
            continue

        try:
            # Converte a data formatada para o formato da biblioteca DATETIME
            validade_cnh = datetime.strptime(validade_formatada, f"%d/%m/%Y")

            # calcula quantos anos tem para vencer a carteira
            anos = validade_cnh.year - datetime.now().year

            if anos < 1:
                if (datetime.now().month == validade_cnh.month)and(datetime.now().day >= validade_cnh.day):
                    print("Sua carteira venceu!")
                    carteira_status = False
                    validade = {
                        "VALIDADE": validade_formatada,
                        "CARTEIRA_STATUS": carteira_status
                    }
                    return validade

                elif (datetime.now().month == validade_cnh.month)and(datetime.now().day < validade_cnh.day):
                    print("Sua carteira vence esse mês!")
                    carteira_status = False
                    validade = {
                        "VALIDADE": validade_formatada,
                        "CARTEIRA_STATUS": carteira_status
                    }
                    return validade

                else:
                    meses = validade_cnh.month - datetime.now().month
                    print(f'Sua carteira vence em {meses} mese(s).')
                    carteira_status = True
                    validade = {
                        "VALIDADE": validade_formatada,
                        "CARTEIRA_STATUS": carteira_status
                    }
                    return validade
            else:
                print(f'validade da carteira vence em {anos} anos!')
                carteira_status = True

                validade = {
                        "VALIDADE": validade_formatada,
                        "CARTEIRA_STATUS": carteira_status
                    }
                return validade            

        except:
             print("Formato de data inválido! Por favor, use o formato DDMMAAAA.")


# Preencher a categoria da CNH
def preencher_categoria_cnh():

    categoria = input("Informe a categoria de sua CNH: ")

    while True:
        try:
            validar = int(input(f'Confirma que a categoria da CNH?\n{categoria}\n1-Sim\n2-Não\n'))

            match validar:
                case 1:
                    return categoria
                case 2:
                     categoria = input("Informe a categoria de sua CNH: ")
                case __:
                    print("Opção invalida!")
                    continue
        
        except:
            print("Formato invalido! Por favor, insira 1 ou 2.")


# LOGAR senha cliente
def logar_senha():

    senha = input("Insira uma senha de 8 digitos(apenas números!): ")

    if len(senha)==8 and senha.isdigit():
        return senha
        
    else:
        print("Senha invalida! Por favor, use apenas 8 digitos!")
        preencher_senha()


# Preencher senha de Login
def preencher_senha():

    senha = input("Insira uma senha de 8 digitos(apenas números!): ")

    if len(senha)==8 and senha.isdigit():
        senha2 = input("Insira novamente a mesma senha: ")
        if senha == senha2:
            print("Senha cadastrada")
            return senha
        else:
            print("senhas diferentes!")
            preencher_senha()
    else:
        print("Senha invalida! Por favor, use apenas 8 digitos!")
        preencher_senha()


# Carregar todos os dados salvo de clientes do JSON
def carregar_clientes():
        # verifica se o arquivo existe
    if os.path.exists("cliente.json"):

        # Ler o conteudo existente
        with open("cliente.json", "r") as file:
            dados = json.load(file)
            return dados
        
    else:
        dados = {}
        return dados
    

# Cadastrando os dados do cliente
def cadastrar_cliente():
    
    # Informações Pessoais    
    nome_completo = preencher_nome_cliente()

    data_nascimento = preencher_data_nascimento()
    
    cpf = preencher_cpf()

    rg = preencher_rg()

    nascionalidade = preencher_nascionalidade()

    senha = preencher_senha()

    
    # Endereço
    endereco = preencher_endereco()

    
    # Contatos
    telefone = preencher_telefone()

    mail = preencher_email()


    # Carteira de habilitação
    numero_cnh = preencher_cnh()
    
    validade_cnh = preencher_validade_cnh()
    
    categoria_cnh = preencher_categoria_cnh()

 
    # Criando o dicionario com as informações preenchidas pelo usuario
    dic_cadastrar_cliente = {
        cpf:{
            "NOME": nome_completo,
            "DATA_NASCIMENTO" : data_nascimento,
            "CPF" : cpf,
            "RG" : rg,
            "NASCIONALIDADE" : nascionalidade,
            "SENHA" : senha,
            "ENDERECO" : endereco,
            "TELEFONE" : telefone,
            "MAIL" : mail,
            "NUMERO_CNH" : numero_cnh,
            "VALIDADE_CNH" : validade_cnh,
            "CATEGORIA_CNH" : categoria_cnh
        }
    }

    dados_cliente = carregar_clientes()

    # Adiciona novos dados ao dicionario 
    dados_cliente.update(dic_cadastrar_cliente)

    # Salva o dicionario atualizado
    with open("cliente.json", "w") as file:
        json.dump(dados_cliente, file, indent=4)


    print("Cadastrado com sucesso!")


def cliente_atulizar_cliente(cpf):
    try:
        dados_cliente = carregar_clientes()

        if cpf in dados_cliente:
            while True:
                try:
                    opcao = int(input("Atualizar:\n(1) CNH\n(2) Data de Validadade da CNH\n(3) Categoria da CNH\n(4) EMAIL\n(5) Celular\n(6) Endereço\n(7) Voltar\n"))

                    match opcao:
                        case 1:
                            nova_cnh = preencher_cnh()

                            # Adiciona novos dados ao dicionario 
                            dados_cliente[cpf]["NUMERO_CNH"] = nova_cnh   

                            # Salva o dicionario atualizado
                            with open("cliente.json", "w") as file:
                                json.dump(dados_cliente, file, indent=4) 

                        case 2:
                            nova_validade_cnh = preencher_validade_cnh()

                            # Adiciona novos dados ao dicionario 
                            dados_cliente[cpf]["VALIDADE_CNH"] = nova_validade_cnh   

                            # Salva o dicionario atualizado
                            with open("cliente.json", "w") as file:
                                json.dump(dados_cliente, file, indent=4) 

                        case 3:
                            nova_categoria_cnh = preencher_categoria_cnh()

                            # Adiciona novos dados ao dicionario 
                            dados_cliente[cpf]["CATEGORIA_CNH"] = nova_categoria_cnh   

                            # Salva o dicionario atualizado
                            with open("cliente.json", "w") as file:
                                json.dump(dados_cliente, file, indent=4) 
                        
                        case 4:
                            novo_mail = preencher_email()

                            # Adiciona novos dados ao dicionario 
                            dados_cliente[cpf]["MAIL"] = novo_mail   

                            # Salva o dicionario atualizado
                            with open("cliente.json", "w") as file:
                                json.dump(dados_cliente, file, indent=4) 

                        case 5:
                            novo_celular = preencher_telefone()

                            # Adiciona novos dados ao dicionario 
                            dados_cliente[cpf]["TELEFONE"] = novo_celular   

                            # Salva o dicionario atualizado
                            with open("cliente.json", "w") as file:
                                json.dump(dados_cliente, file, indent=4) 

                        case 6: 
                            novo_endereco = preencher_endereco()

                            # Adiciona novos dados ao dicionario 
                            dados_cliente[cpf]["ENDERECO"] = novo_endereco   

                            # Salva o dicionario atualizado
                            with open("cliente.json", "w") as file:
                                json.dump(dados_cliente, file, indent=4) 

                        case 7:
                            menu_cliente_logado(cpf)

                        case __:
                            opcao_invalida_principal()

                except:
                    print("Formato invalido! Por favor, insira apenas as opções validas!")




    except:
        print("Erro ao atualizar dados!")


def menu_cliente_logado(cpf):
    try:
        opcao = int(input("MENU CLIENTE\n(1) Atualizar meus dados.\n(2) Solicitar Aluguel.\n(3) Deslogar\n"))

        match opcao:
            case 1:
                cliente_atulizar_cliente(cpf)
            case 2:
                ############################
                #solicitar alugel de carros#
                ############################
                menu_cliente_logado(cpf)
                
            case 3:
                os.system('cls')
                print("Voltando ao menu anterior!")
                main()
            case __:
                opcao_invalida_principal()
                menu_cliente()

    except:
        opcao_invalida_principal()
        menu_cliente()


# Acesso a conta do cliente
def login_cliente():
    # Solicita o CPF e a senha do usuário
    cpf = logar_cpf()
    senha = logar_senha()

    # Verificar se o cpf está no arquivo json
    try:
        with open("cliente.json", "r") as file:
            clientes = json.load(file)
        
        if cpf in clientes:
            cliente_data = clientes[cpf]
            
            if cliente_data["SENHA"] == senha:
                print("Login realizado com sucesso!")
                menu_cliente_logado(cpf)
            else:
                print("Senha incorreta. Tente novamente.")
                menu_cliente()
        else:
            print("CPF não encontrado. Tente novamente ou cadastre-se.")
            menu_cliente()

    except:
        print("Erro ao realizar login:")
        menu_cliente()


# Menu do cliente caso deseja fazer login ou cadastrar-se
def menu_cliente():
    try:
        opcao = int(input("MENU CLIENTE\n(1) Login.\n(2) Cadastrar.\n(3) Voltar\n"))

        match opcao:
            case 1:
                login_cliente()
            case 2:
                cadastrar_cliente()
                menu_cliente()
                
            case 3:
                os.system('cls')
                print("Voltando ao menu anterior!")
                main()
            case __:
                opcao_invalida_principal()
                menu_cliente()

    except:
        opcao_invalida_principal()
        menu_cliente()


# ADM - visualiza todos os clientes do JSON
def visualizar_clientes():
    try:
        dados_cliente = carregar_clientes()

        quantidade = 0


        for cliente in dados_cliente:
            print(f"NOME: {dados_cliente.get(cliente).get("NOME")}")
            print(f"DATA DE NASCIMENTO: {dados_cliente.get(cliente).get("DATA_NASCIMENTO")}")
            print(F"NASCIONALIDADE: {dados_cliente.get(cliente).get("NASCIONALIDADE")}")
            print(F"CPF: {dados_cliente.get(cliente).get("CPF")}")
            print(F"RG: {dados_cliente.get(cliente).get("RG")}")
            print(F"CNH: {dados_cliente.get(cliente).get("NUMERO_CNH")}")
            print(F"VALIDADE CNH: {dados_cliente.get(cliente).get("VALIDADE_CNH").get("VALIDADE")}")
            print(F"TIPA CNH: {dados_cliente.get(cliente).get("CATEGORIA_CNH")}")
            print(F"EMAIL: {dados_cliente.get(cliente).get("MAIL")}")
            print(F"CELULAR: {dados_cliente.get(cliente).get("TELEFONE").get("DDD")} {dados_cliente.get(cliente).get("TELEFONE").get("CELULAR")}")
            print(F"ENDEREÇO: {dados_cliente.get(cliente).get("ENDERECO").get("RUA")}, {dados_cliente.get(cliente).get("ENDERECO").get("NUMERO")}, {dados_cliente.get(cliente).get("ENDERECO").get("COMPLEMENTO")}, {dados_cliente.get(cliente).get("ENDERECO").get("BAIRRO")}, {dados_cliente.get(cliente).get("ENDERECO").get("CIDADE")}, {dados_cliente.get(cliente).get("ENDERECO").get("ESTADO")}, {dados_cliente.get(cliente).get("ENDERECO").get("CEP")}")
            print("##################################################################################################\n\n")
            quantidade+=1

        print(f"Quantidade total de cliente: {quantidade}")

    except:
        print("Erro ao acessar os arquivos dos clintes!")


# ADM - atualizar Cliente
def atualizar_cliente(cpf):
    try:
        dados_cliente = carregar_clientes()

        if cpf in dados_cliente:
            while True:
                try:
                    opcao = int(input("Atualizar:\n(1) Nome\n(2) Data de Nascimento\n(3) Nascionalidade\n(4) CPF\n(5) RG\n(6) CNH\n(7) Data de Validadade da CNH\n(8) Categoria da CNH\n(9) EMAIL\n(10) Celular\n(11) Endereço\n(12) Voltar\n"))

                    match opcao:
                        # Atualizar nome
                        case 1:
                            novo_nome = preencher_nome_cliente()
                            
                            # Adiciona novos dados ao dicionario 
                            dados_cliente[cpf]["NOME"] = novo_nome
                            
                            # Salva o dicionario atualizado
                            with open("cliente.json", "w") as file:
                                json.dump(dados_cliente, file, indent=4)
                        
                        # Atualizar data de nascimento
                        case 2:
                            novo_nascimento = preencher_data_nascimento()
                            
                            # Adiciona novos dados ao dicionario 
                            dados_cliente[cpf]["DATA_NASCIMENTO"] = novo_nascimento   

                            # Salva o dicionario atualizado
                            with open("cliente.json", "w") as file:
                                json.dump(dados_cliente, file, indent=4) 

                        # Atualizar Nascionalidade
                        case 3:
                            nova_nascionalidade = preencher_nascionalidade()

                            # Adiciona novos dados ao dicionario 
                            dados_cliente[cpf]["NASCIONALIDADE"] = nova_nascionalidade   

                            # Salva o dicionario atualizado
                            with open("cliente.json", "w") as file:
                                json.dump(dados_cliente, file, indent=4) 

                        # Atualizar CPF
                        case 4:
                            novo_cpf = preencher_cpf()

                            dic_atualizar_cliente = {
                                novo_cpf:{
                                    "NOME": dados_cliente[cpf]["NOME"],
                                    "DATA_NASCIMENTO" : dados_cliente[cpf]["DATA_NASCIMENTO"],
                                    "CPF" : novo_cpf,
                                    "RG" : dados_cliente[cpf]["RG"],
                                    "NASCIONALIDADE" : dados_cliente[cpf]["NASCIONALIDADE"],
                                    "SENHA" : dados_cliente[cpf]["SENHA"],
                                    "ENDERECO" : dados_cliente[cpf]["ENDERECO"],
                                    "TELEFONE" : dados_cliente[cpf]["TELEFONE"],
                                    "MAIL" : dados_cliente[cpf]["MAIL"],
                                    "NUMERO_CNH" : dados_cliente[cpf]["NUMERO_CNH"],
                                    "VALIDADE_CNH" : dados_cliente[cpf]["VALIDADE_CNH"],
                                    "CATEGORIA_CNH" : dados_cliente[cpf]["CATEGORIA_CNH"]
                                }
                            }

                            # Adiciona novos dados ao dicionario 
                            dados_cliente.update(dic_atualizar_cliente)

                            # remove os antigos dados do dicionario
                            dados_cliente.pop(cpf)

                            # Salva o dicionario atualizado
                            with open("cliente.json", "w") as file:
                                json.dump(dados_cliente, file, indent=4) 

                        case 5:
                            novo_rg = preencher_rg()

                            # Adiciona novos dados ao dicionario 
                            dados_cliente[cpf]["RG"] = novo_rg   

                            # Salva o dicionario atualizado
                            with open("cliente.json", "w") as file:
                                json.dump(dados_cliente, file, indent=4) 
                        
                        case 6:
                            nova_cnh = preencher_cnh()

                            # Adiciona novos dados ao dicionario 
                            dados_cliente[cpf]["NUMERO_CNH"] = nova_cnh   

                            # Salva o dicionario atualizado
                            with open("cliente.json", "w") as file:
                                json.dump(dados_cliente, file, indent=4) 

                        case 7:
                            nova_validade_cnh = preencher_validade_cnh()

                            # Adiciona novos dados ao dicionario 
                            dados_cliente[cpf]["VALIDADE_CNH"] = nova_validade_cnh   

                            # Salva o dicionario atualizado
                            with open("cliente.json", "w") as file:
                                json.dump(dados_cliente, file, indent=4) 

                        case 8:
                            nova_categoria_cnh = preencher_categoria_cnh()

                            # Adiciona novos dados ao dicionario 
                            dados_cliente[cpf]["CATEGORIA_CNH"] = nova_categoria_cnh   

                            # Salva o dicionario atualizado
                            with open("cliente.json", "w") as file:
                                json.dump(dados_cliente, file, indent=4) 
                        
                        case 9:
                            novo_mail = preencher_email()

                            # Adiciona novos dados ao dicionario 
                            dados_cliente[cpf]["MAIL"] = novo_mail   

                            # Salva o dicionario atualizado
                            with open("cliente.json", "w") as file:
                                json.dump(dados_cliente, file, indent=4) 

                        case 10:
                            novo_celular = preencher_telefone()

                            # Adiciona novos dados ao dicionario 
                            dados_cliente[cpf]["TELEFONE"] = novo_celular   

                            # Salva o dicionario atualizado
                            with open("cliente.json", "w") as file:
                                json.dump(dados_cliente, file, indent=4) 

                        case 11: 
                            novo_endereco = preencher_endereco()

                            # Adiciona novos dados ao dicionario 
                            dados_cliente[cpf]["ENDERECO"] = novo_endereco   

                            # Salva o dicionario atualizado
                            with open("cliente.json", "w") as file:
                                json.dump(dados_cliente, file, indent=4) 

                        case 12:
                            menu_procurar_cliente()

                        case __:
                            opcao_invalida_principal()

                except:
                    print("Formato invalido! Por favor, insira apenas as opções validas!")

        else:
            print("CPF não encontrado!")

    except: 
        print("Erro ao atualizar cliente!")


# ADM - deletar Cliente
def deletar_cliente(cpf):
    try:
        dados_cliente = carregar_clientes()

        if cpf in dados_cliente:

            while True:
                try:
                    for cliente in dados_cliente:
                        if cpf == cliente:
                            print(f"NOME: {dados_cliente.get(cliente).get("NOME")}")
                            print(f"DATA DE NASCIMENTO: {dados_cliente.get(cliente).get("DATA_NASCIMENTO")}")
                            print(F"NASCIONALIDADE: {dados_cliente.get(cliente).get("NASCIONALIDADE")}")
                            print(F"CPF: {dados_cliente.get(cliente).get("CPF")}")
                            print(F"RG: {dados_cliente.get(cliente).get("RG")}")
                            print(F"CNH: {dados_cliente.get(cliente).get("NUMERO_CNH")}")
                            print(F"VALIDADE CNH: {dados_cliente.get(cliente).get("VALIDADE_CNH").get("VALIDADE")}")
                            print(F"TIPA CNH: {dados_cliente.get(cliente).get("CATEGORIA_CNH")}")
                            print(F"EMAIL: {dados_cliente.get(cliente).get("MAIL")}")
                            print(F"CELULAR: {dados_cliente.get(cliente).get("TELEFONE").get("DDD")} {dados_cliente.get(cliente).get("TELEFONE").get("CELULAR")}")
                            print(F"ENDEREÇO: {dados_cliente.get(cliente).get("ENDERECO").get("RUA")}, {dados_cliente.get(cliente).get("ENDERECO").get("NUMERO")}, {dados_cliente.get(cliente).get("ENDERECO").get("COMPLEMENTO")}, {dados_cliente.get(cliente).get("ENDERECO").get("BAIRRO")}, {dados_cliente.get(cliente).get("ENDERECO").get("CIDADE")}, {dados_cliente.get(cliente).get("ENDERECO").get("ESTADO")}, {dados_cliente.get(cliente).get("ENDERECO").get("CEP")}")
                            print("##################################################################################################\n\n")
                        


                    validar = int(input('Confirma que quer deletar o cliente?\n1-Sim\n2-Não\n'))

                    match validar:
                        case 1:
                            # remove os antigos dados do dicionario
                            dados_cliente.pop(cpf)

                            # Salva o dicionario atualizado
                            with open("cliente.json", "w") as file:
                                json.dump(dados_cliente, file, indent=4)

                            print("Cliente Deletado!")
                            break
                            
                        case 2:
                            menu_procurar_cliente()
                        case __:
                            print("Opção invalida!")
                            continue
                
                except:
                    print("Formato invalido! Por favor, insira 1 ou 2.")

             

        else:
            print("CPF não encontrado!")

    except:
        print("Erro ao deletar cliente!")


# ADM - procurar Cliente
def menu_procurar_cliente():
    try:
        opcao = int(input("\n(1) Visualizar todos os Clientes\n(2) Atualizar Cliente\n(3) Deletar Cliente\n(4) Voltar\n"))

        match opcao:
            case 1:
                os.system('cls')
                visualizar_clientes()
                menu_procurar_cliente()
            case 2:
                os.system('cls')
                cpf = input("Informe o CPF: ")
                atualizar_cliente(cpf)
                menu_procurar_cliente()
            case 3:
                os.system('cls')
                cpf = input("Informe o CPF: ")
                deletar_cliente(cpf)
                menu_procurar_cliente()
            case 4:
                os.system('cls')
                print("Voltando ao menu anterior!")
                menu_adm_cliente()
            case __:
                os.system('cls')
                opcao_invalida_principal()
                menu_procurar_cliente()
    except:
        opcao_invalida_principal()
        menu_procurar_cliente()


# ADM - Menu Cliente
def menu_adm_cliente():
    try:
        opcao = int(input("ADM CLIENTE\n(1) Cadastrar Cliente\n(2) Procurar Cliente\n(3) Voltar\n"))

        match opcao:
            case 1:
                os.system('cls')
                cadastrar_cliente()
                menu_adm_cliente()
            case 2:
                os.system('cls')
                menu_procurar_cliente()
            case 3 :
                os.system('cls')
                print("Voltando ao menu anterior!")
                menu_adm()
            case __:
                os.system('cls')
                opcao_invalida_principal()
                menu_adm_cliente() 
    except:
        opcao_invalida_principal()
        menu_adm_cliente


# Menu do administrador
def menu_adm():
    try:
        opcao = int(input("MENU ADMINISTRADOR\n(1) Cliente\n(2) Carro\n(3) Alugar\n(4) Voltar\n"))

        match opcao:
            case 1:
                os.system('cls')
                menu_adm_cliente()
                menu_adm()
            case 2:
                os.system('cls')
                menu_carros()
                menu_adm()
            case 3:
                os.system('cls')
                print("MENU ALUGAR")
                menu_adm()
            case 4 :
                os.system('cls')
                print("Voltando ao menu anterior!")
                main()
            case __:
                os.system('cls')
                opcao_invalida_principal()
                menu_adm() 
    except:
        opcao_invalida_principal()
        menu_adm()


#acesso a area de Administraçao do app
def login_adm():
    print("Login ADM\n")
    login = input("CPF: ")

    if len(login)==11 and login.isdigit():
        senha = input("Senha: ")

        if len(senha)==8 and senha.isdigit():
            with open("adm.json") as file:
                dados_adm = json.load(file)
            
                if dados_adm.get(login) and dados_adm.get(login).get("SENHA") == senha:
                    print("LOGADO")
                    menu_adm()

        else:
            print("Senha invalida!")
            main()

    
    else:
        print("CPF invalido!")
        main()


# Menu Inicial na tela do programa.
def main():
    os.system('cls')
    print("""
****************************
    Bem-Vindo a LocAqui!
****************************
""")
    # TRY e EXCEPT - vai inpedir que o programa de erro caso o usuario
    # entre com algum valor que nao seja inteiro.
    try:
        opcao = int(input("Escolha uma opção:\n(1) Adminitrador.\n(2) Cliente.\n(3) Encerrar Programa.\n"))

        match opcao:
            case 1:
                #acessar menu de administradores
                login_adm()
            case 2:
                #acessar menu de Clientes
                os.system('cls')
                menu_cliente()
            case 3:
                os.system('cls')
                print("Encerrando o programa...")
            case __:
                opcao_invalida_principal()
                main()

    except:
        opcao_invalida_principal()
        main()

if __name__ == "__main__":
    main()