import textwrap

def menu():
    menu="""\n
        =======================Menu=======================
        \n
        [1] Depositar
        [2] Sacar
        [3] Extrato
        [4] Novo usuário
        [5] Nova conta
        [6] Listar contas
        [0] Sair
    =>"""
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor>0:
        saldo+=valor
        extrato+=f"Depósito: R${valor:.2f}\n"
        print("\nDepósito realizado com sucesso!")
        
    else:
        print("\nOperação falhou: valor informado é inválido.")
        
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
        
    excedeu_saldo=valor>saldo
    excedeu_limite=valor>limite
    excedeu_saques=numero_saques>=limite_saques
    
    if excedeu_saldo:
        print("\nOperação falhor: você não tem saldo suficiente.")
    
    elif excedeu_limite:
        print("\nOperação falhor: valor de saque excede o limite.")
        
    elif excedeu_saques:
        print("\nOperação falhor: você excedeu o número máximo de saques por dia.")
        
    elif valor>0:
        saldo-=valor
        extrato+=f"Saque: R${valor:.2f}\n"
        numero_saques+=1
        print("\nSaque realizado com sucesso!")
    
    else:
        print("\nOperação falhou: valor informado é inválido.")
        
    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações nessa conta." if not extrato else extrato)
    print(f"Saldo R${saldo:.2f}\n")
    print("================================")
    
def criar_usuario(usuarios):
    cpf=input("Informe o CPF (somente numeros):")
    usuario=filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print("\n Já existe usuário com esse CPF!")
        return

    nome=input("Nome completo: ")
    data_nascimento=input("Data de nascimento (dd-mm-aa): ")
    endereco=input("Endereço (logradouro, número, bairro, cidade/sigla estado): ")
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco":endereco})
    
    print("\n===== Usuário cadastrado com sucesso! =====")
    
def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados=[usuario for usuario in usuarios if usuario["cpf"]==cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None
    
def criar_conta(agencia, numero_conta, usuarios):
    cpf=input("CPF do usuário:")
    usuario=filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print("\nConta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    else:
        print("\nUsuário não encontrado, fluxo de criação de conta encerrado!")
        
def listar_contas(contas):
    for conta in contas:
        linha=f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("="*100)
        print(textwrap.dedent(linha))


def main():
    saldo=0
    limite=500
    extrato=""
    numero_saques=0
    LIMITE_SAQUES=3
    AGENCIA="0001"
    usuarios=[]
    contas=[]
    
    while True:
        opcao=menu()
        if opcao=="1":
            valor=float(input("Valor do depósito:"))
            saldo, extrato=depositar(saldo, valor, extrato)
        
        elif opcao=="2":
            valor=float(input("Valor do saque:"))
            saldo, extrato=sacar(saldo=saldo, valor=valor, extrato=extrato, limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES)
        
        elif opcao=="3":
            exibir_extrato(saldo, extrato=extrato)
        
        elif opcao=="4":
            criar_usuario(usuarios)
            
        elif opcao=="5":
            numero_conta=len(contas)+1
            conta=criar_conta(AGENCIA, numero_conta, usuarios)
            
            if conta:
                contas.append(conta)
                
        elif opcao=="6":
            listar_contas(contas)
        
        elif opcao=="0":
            print("Obrigada, volte sempre!")
            break
        
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")
            
main()
    
# menu="""

# [d] Depositar
# [s] Sacar
# [e] Extrato
# [q] Sair

# =>"""

# saldo=0
# limite=500
# extrato=""
# numero_saques=0
# LIMITE_SAQUES=3

# while True:
#     opcao=input(menu)
    
#     if opcao=="d":
#         valor=float(input("Informe o valor do depósito: "))
        
#         if valor>0:
#             saldo+=valor
#             extrato+=f"Depósito: R${valor:.2f}\n"
            
#         else:
#             print("Operação falhou: valor informado é inválido.")
    
#     elif opcao=="s":
#         valor=float(input("Informe o valor do saque: "))
        
#         excedeu_saldo=valor>saldo
#         excedeu_limite=valor>limite
#         excedeu_saques=numero_saques>=LIMITE_SAQUES
        
#         if excedeu_saldo:
#             print("Operação falhor: você não tem saldo suficiente.")
        
#         elif excedeu_limite:
#             print("Operação falhor: valor de saque excede o limite.")
            
#         elif excedeu_saques:
#             print("Operação falhor: você excedeu o número máximo de saques por dia.")
            
#         elif valor>0:
#             saldo-=valor
#             extrato+=f"Saque: R${valor:.2f}\n"
#             numero_saques+=1
        
#         else:
#             print("Operação falhou: valor informado é inválido.")
            
#     elif opcao=="e":
#         print("\n================ EXTRATO ================")
#         print("Não foram realizadas movimentações nessa conta." if not extrato else extrato)
#         print(f"Saldo R${valor:.2f}\n")
#         print("================================")
        
#     elif opcao=="q":
#         print("Obrigado, até logo!")
#         break
    
#     else:
#         print("Operação inválida, por favor selecione novamente a operação desejada.")