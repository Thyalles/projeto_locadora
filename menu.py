import os
import json
import time
from datetime import datetime

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
                            if(verificar_cnh(numero_cnh)):
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

    # Criando o objeto 
    obj_json = json.dumps(dic_cadastrar_cliente, indent=4)
    # Criando o arquivo com o json e salvando
    with open ("cliente.json" , "w") as file:
        file.write(obj_json)

    print("Cadastrado com sucesso!")

# Menu do cliente caso deseja fazer login ou cadastrar-se
def menu_cliente():
    try:
        opcao = int(input("MENU CLIENTE\n1-Login.\n2-Cadastrar.\n3-Voltar ao menu anterior.\n"))

        match opcao:
            case 1:
                ######################################
                #fazer validaçoes para efetuar o login
                ######################################
                print("Logado")
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

def menu_procurar_cliente():
    try:
        opcao = int(input("\n1-Visualizar Cliente\n2-Atualizar Cliente\n3-Deletar Cliente\n4-Voltar ao menu anterior.\n"))

        match opcao:
            case 1:
                #inplementar
                print("Visualizar Cliente")
                menu_procurar_cliente()
            case 2:
                #inplementar
                print("Atualizar Cliente")
                menu_procurar_cliente()
            case 3:
                #inplementar
                print("Deletar Cliente")
                menu_procurar_cliente()
            case 4:
                os.system('cls')
                print("Voltando ao menu anterior!")
                menu_adm_cliente()
            case __:
                opcao_invalida_principal()
                menu_procurar_cliente()
    except:
        opcao_invalida_principal()
        menu_procurar_cliente()

def menu_adm_cliente():
    try:
        opcao = int(input("ADM CLIENTE\n1-Cadastrar Cliente\n2-Procurar Cliente\n3-Voltar ao menu anterior.\n"))

        match opcao:
            case 1:
                cadastrar_cliente()
                menu_adm_cliente()
            case 2:
                print("PROCURAR CLIENTE")
                menu_procurar_cliente()
            case 3 :
                os.system('cls')
                print("Voltando ao menu anterior!")
                menu_adm()
            case __:
                opcao_invalida_principal()
                menu_adm_cliente() 
    except:
        opcao_invalida_principal()
        menu_adm_cliente



def menu_adm():
    try:
        opcao = int(input("MENU ADMINISTRADOR\n1-Cliente\n2-Carro\n3-Alugar\n4-Voltar ao menu anterior.\n"))

        match opcao:
            case 1:
                menu_adm_cliente()
                menu_adm()
            case 2:
                print("MENU CARRO")
                menu_adm()
            case 3:
                print("MENU ALUGAR")
                menu_adm()
            case 4 :
                os.system('cls')
                print("Voltando ao menu anterior!")
                main()
            case __:
                opcao_invalida_principal()
                menu_adm() 
    except:
        opcao_invalida_principal()
        menu_adm()


def login_adm():
    print("Login\n")
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
        opcao = int(input("Escolha uma opção:\n1-Adminitrador.\n2-Cliente.\n3-Encerrar Programa.\n"))

        match opcao:
            case 1:
                #acessar menu de administradores
                print("Menu Admin")
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