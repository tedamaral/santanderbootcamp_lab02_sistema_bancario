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
    opcao = input(menu).lower()

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("❌ Operação falhou! Valor inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        if valor <= 0:
            print("❌ Operação falhou! Valor inválido.")
        elif valor > saldo:
            print("❌ Saldo insuficiente.")
        elif valor > limite:
            print("❌ Valor excede o limite por saque.")
        elif numero_saques >= LIMITE_SAQUES:
            print("❌ Limite de saques diários atingido.")
        else:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

    elif opcao == "e":
        print("\n======= EXTRATO =======")
        print(extrato if extrato else "Nenhuma movimentação realizada.")
        print(f"Saldo: R$ {saldo:.2f}")
        print("========================")

    elif opcao == "q":
        print("✅ Saindo do sistema. Até mais!")
        break

    else:
        print("❌ Opção inválida. Tente novamente.")
