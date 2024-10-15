menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        valor_deposito = float(input("Informe o valor que você quer depositar: "))

        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f"Depósito: R$ {valor_deposito:.2f}\n"
            print(f"O depósito de R$ {valor_deposito:.2f} foi realizado com sucesso.")

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "2":

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saques: # se o limite foi excedido, não há necessidade de pedir o valor do saque
            print("Operação falhou! O número máximo de saques foi excedido.")

        else:
            valor_saque = float(input("Informe o valor do saque: "))

            excedeu_saldo = valor_saque > saldo

            excedeu_limite = valor_saque > limite       

            if excedeu_saldo:
                print("Operação falhou! O saldo é insuficiente para realizar o saque.")

            elif excedeu_limite:
                print("Operação falhou! O valor do saque excedeu o limite para cada saque.")

            elif valor_saque > 0:
                saldo -= valor_saque
                extrato += f"Saque: R$ {valor_saque:.2f}\n"
                numero_saques += 1
                print(f"O saque no valor de R$ {valor_saque} foi realizado com sucesso.")

            else:
                print("Operação falhou! O valor informado é inválido.")

    elif opcao == "3":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato) # se extrato for vazio, if not é verdadeiro.
        # essa estrutura da linha acima é chamada de operador ternário: saída verdadeiro | condição | saída falso
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("\n==========================================")

    elif opcao == "4":
        break

    else:
        print("Operação inválida, por favor selecione uma operação válida.")