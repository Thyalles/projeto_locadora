arquivo = os.path.join(os.path.dirname(__file__), 'cadastro_dos_carros.json')

def carregar_carros():
    # Verifica se o arquivo existe, se não existir, cria um arquivo com lista vazia
    if not os.path.exists(arquivo):
        with open(arquivo, 'w') as f:
            json.dump({}, f, indent=4)
    
    # Carrega o conteúdo do arquivo
    with open(arquivo, 'r') as f:
        return json.load(f)
    
# Salvo as lterações feitas    
def salvar_dados(arquivo, carros):
    with open(arquivo, 'w' ) as f:
      json.dump(carros,f, indent=4)   

# Atualizo algum dado do dicionario
def atualizar_carro():

   carros=carregar_carros()
   print(carros)
   
   while True:
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