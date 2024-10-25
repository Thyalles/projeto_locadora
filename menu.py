import os
import json
from datetime import datetime

# Caso insira uma opcao invalida, o usuario precisara aperta 
# alguma tecla para voltar ao menu inicial.
def opcao_invalida_principal():
    print("Opção Invalida!")
    input("Digite uma tecla para voltar ao menu\n")

#cadastrando e validando o nome completo do cliente
def cadastrar_nome_cliente():     

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


# Cadastrando e validando a data de nascimento e idade do cliente
def cadastrar_data_nascimento():
    while True:

        data = input("Infome sua data de nascimento(ddmmaaaa): (apenas números!)\n")

        # Confirma se foi digitado apenas numeros e tem 8 digitos de entrada
        if len(data) == 8 and data.isdigit():
            data_formatada = f"{data[:2]}/{data[2:4]}/{data[4:]}"
            print(data_formatada)
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
                            cadastrar_data_nascimento()
                        case __:
                            print("Opção invalida!")
                            continue
                
                except:
                    print("Formato invalido! Por favor, insira 1 ou 2.")
        
        except:
            print("Formato de data inválido! Por favor, use o formato DDMMAAAA.222")


        

# Cadastrando os dados do cliente
def cadastrar_cliente():

    nome_completo = cadastrar_nome_cliente()

    data_nascimento = cadastrar_data_nascimento()

    




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
                ###############################################
                #abrir os inputs para cadastrar um novo cliente
                ###############################################
                print("Cadastrado")
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