menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito:"))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Quanto deseja sacar?"))

        saldo_insuficiente= valor > saldo

        limite_insuficiente= valor > limite

        limite_saque = numero_saques >= LIMITE_SAQUES 

        if saldo_insuficiente:
            print("Saldo insuficiente, falha ao realizar operação")
        elif limite_insuficiente:
            print("Limite insuficiente, falha ao realizar operação")
        elif limite_saque:
            print(f"Falha ao realizar saque, você atingiu o limite de {LIMITE_SAQUES} saques diários")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: {valor:.2f}\n"
            numero_saques += 1
        else:
            print("Operação falhou! O valor informado é inválido.")    

    elif opcao == "e":
        print("---------Extrato---------")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    
    elif opcao == "q":
        print("Saindo...")
        break
    else:
        print("Opção inválida, por favor selecione novamente a operação desejada.")