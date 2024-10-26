
def login_cliente():
    # Solicita o CPF e a senha do usuário
    cpf = preencher_cpf()
    senha = preencher_senha()

    # Verificar se o cpf está no arquivo json
    try:
        with open("cliente.json", "r") as file:
            clientes = json.load(file)
        
        if cpf in clientes:
            cliente_data = clientes[cpf]
            
            if cliente_data["SENHA"] == senha:
                print("Login realizado com sucesso!")
            else:
                print("Senha incorreta. Tente novamente.")
        else:
            print("CPF não encontrado. Tente novamente ou cadastre-se.")

    except:
        print("Erro ao realizar login:")
