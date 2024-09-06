#####################################
# sistema bancario v2
# versao 1.0
# - Programa para deposito, saque e visualização de extrato.
# - O programa utiliza uma lista para armazenar o movimento do extrato.
# - Valor limite para saque R$ 500,00
# - Limite de saques por execuçao 3
# versao 2.0
# - Separado as operações em funções
# - Incluir funções de cadastro de clientes e cadastro de contas
# - um cliente por conta
# - CPF contem apenas numeros e nao pode ser duplicado

menu = """
    =================================
    =        Sistema Bancario       =
    =================================
    = 1 - Depositar Dinheiro        =
    = 2 - Sacar Dinheiro            =
    = 3 - Ver Extrato               =
    = 4 - Cadastrar cliente         =
    = 5 - Listar cliente            =
    = 6 - Cadastrar conta           =
    = 7 - Listar conta              =
    = 8 - Sair                      =
    =================================
    
    Entre com a opção desejada: 
"""

def  cadastrar_cliente(clientes):
    try:
        cpf = int(input("Digite o CPF do cliente, apenas numeros: ") )
    except ValueError:
        print("\n***   CPF invalido, apenas numeros   ***")
        return
    cliente = filtrar_cliente(cpf, clientes)
    if cliente:
        print("\n***   CPF ja cadastrado   ***")
        return
    
    nome = input("Digite o nome do cliente completo: ")
    data_nascimento = input("Informe a data do nascimento (dd-mm-aaaa): ")
    endereco = input("Digite o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
    
    clientes.append({"cpf":cpf, "nome":nome, "data_nascimento":data_nascimento, "endereco":endereco})
    
    print("\n   Cliente cadastrado!\n")
    return 

def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente["cpf"] == cpf]  
    return clientes_filtrados[0] if clientes_filtrados else None

def listar_cliente(clientes):
    print(clientes)
    return

def cadastrar_conta(agencia, conta_numero, clientes):
    try:
        cpf = int(input("Digite o CPF do cliente, apenas numeros: ") )
    except ValueError:
        print("\n***   CPF invalido, apenas numeros   ***")
        return
    cliente = filtrar_cliente(cpf, clientes)
    
    if cliente:
        print("\n   Conta criada!\n")
        return {"agencia":agencia, "conta_numero":conta_numero, "cliente":cliente}
    
    print("\n***   Cliente não existe, cadastro de conta não realizado!   ***\n")

def listar_contas(contas):    
    for conta in contas:
        linha = f"""\
            Agência:\t{conta["agencia"]}
            C/C:\t{conta["conta_numero"]}
            Titular:\t{conta['cliente']['nome']}
        """
        print("=" * 50)
        print(linha)
    return

def depositar(saldo, extrato, valor, /):
    if valor > 0:
        saldo += valor
        extrato += f"deposito {valor:.2f}\n"
        print(f"\n   Deposito realizado. Saldo atual R${saldo:.2f}\n")
    else:
        print("\n***   Valor invalido, apenas valores positivos   ***")
    return extrato, saldo

def sacar(*, saldo, valor, extrato,saque_realizado,limite_saque,valor_limite):
    if saque_realizado >= limite_saque:
        print(f"\n***   Limite de saque diário {limite_saque } atingido! Não pode ser realizado.   ***\n")  
                  
    elif  valor > saldo:
        print("\n***       Saldo insuficiente! Não pode ser realizado.   ***\n")
        
    elif  valor > valor_limite:
        print("\n***       Limite de valor do saque diário atingido! Não pode ser realizado.   ***\n")
        
    elif valor > 0:    
        saldo -= valor
        extrato += f"Saque de R$ {valor:.2f}\n"   
        saque_realizado += 1         
        print(f"\n\n    Saldo atual: R${saldo:.2f}\n") 
    else: 
        print("\n***  Falhou! Valor inválido   ***")
        
    return saldo, extrato

def mostrar_extrato(saldo, /, *, extrato):
    print("\n\n===========\n= EXTRATO =\n===========")        
    print("Não há movimentações" if not extrato else extrato)
    print("===========\n")
    print(f"\n    Saldo atual: R${saldo:.2f}\n") 
      
    
def main():
    AGENCIA = "0001"
    LIMITE_SAQUE = 3
    
    saldo = 0
    saque_realizado = 0
    valor_limite = 500
    extrato = ''
    clientes = []
    contas = []
    
    while True:     
        try: 
            opcao = int(input(menu))
        except ValueError:
            print("\n\n***    Opção inválida. Por favor, tente novamente.   ***\n")
            continue
        match opcao:
            case 1:
                try:       
                    valor = float(input("\n    Qual valor você deseja depositar? R$ "))
                except ValueError:
                    print("\n***   Valor inválido   ***")
                    continue            
                extrato, saldo = depositar(saldo, extrato, valor)                
            case 2:
                try:
                    valor = float(input("\n    Qual valor você deseja sacar? R$ "))
                except ValueError:
                    print("\n***   Valor inválido   ***")
                    continue
                saldo, extrato = sacar(saldo=saldo, valor=valor, extrato=extrato, saque_realizado=saque_realizado, limite_saque=LIMITE_SAQUE, valor_limite=valor_limite)
            case 3:
                mostrar_extrato(saldo, extrato=extrato)
            case 4:
                cadastrar_cliente(clientes)
            case 5:
                listar_cliente(clientes)
            case 6:
                conta_numero = len(contas) + 1                
                conta = cadastrar_conta(AGENCIA, conta_numero, clientes)
                if conta:
                    contas.append(conta)

            case 7:
                listar_contas(contas)
            case 8:
                print("\n\nAté logo.\n\n--------------")
                break
            case _:
                print("\n\n***    Opção inválida. Por favor, tente novamente.")
                

main()       

        
        
        
        
