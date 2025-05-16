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
            saldo =+valor
            print(f"Depósito de {valor} realizado.")           
            
    if opcao == "s":
        print("Saque")

    if opcao == "e":
        print("Extrato")
    
    if opcao == "q":
        print("Saindo...")
        break
    else:
        print("Opção inválida, por favor selecione novamente a operação desejada.")