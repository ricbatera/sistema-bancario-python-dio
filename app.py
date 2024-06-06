menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """

saldo = 0
limite_saque = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES_DIARIOS = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Quanto quer depositar? "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"Pronto! Depósito no valor R$ {valor:.2f} efetuado com sucesso.")

        else:
            print("Algo deu errado! Verifique o valor digitado e tente novamente.")

    elif opcao == "2":
        valor = float(input("De quanto precisa? "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite_saque

        excedeu_saques = numero_saques >= LIMITE_SAQUES_DIARIOS

        if excedeu_saldo:
            print("Algo deu errado! Não há saldo suficiente para saque.")

        elif excedeu_limite:
            print(f"Algo deu errado! O limite máximo para saques é de R$ {limite_saque:.2f}.")

        elif excedeu_saques:
            print("Algo deu errado! Você atingiou a quantidade máxima de saques para hoje.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print(f"Pronto! Saque no valor R$ {valor:.2f} efetuado com sucesso.")

        else:
            print("Algo deu errado! Verifique o valor digitado e tente novamente.")

    elif opcao == "3":
        print("\n================ EXTRATO ================")
        print("Não há movimentações recentes." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "0":
        break

    else:
        print("Opção inválida! Por favor selecione a opção correta no menu abaixo.")