import datetime

# Variáveis Globais
saldo = 0.0
limite_saque = 500.0
extrato = []
quantidade_saques = 0
LIMITE_SAQUES_DIARIOS = 3

def depositar(valor):
    global saldo
    if valor > 0:
        saldo += valor
        extrato.append(f"{datetime.datetime.now()} - Depósito: R$ {valor:.2f}")
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Valor inválido! Depósito deve ser maior que zero.")

def sacar(valor):
    global saldo, quantidade_saques
    if quantidade_saques >= LIMITE_SAQUES_DIARIOS:
        print("Limite de saques diários atingido!")
        return

    if valor > limite_saque:
        print(f"Limite de saque é R$ {limite_saque:.2f} por operação.")
    elif valor > saldo:
        print("Saldo insuficiente para essa operação!")
    elif valor <= 0:
        print("O valor do saque deve ser positivo!")
    else:
        saldo -= valor
        quantidade_saques += 1
        extrato.append(f"{datetime.datetime.now()} - Saque: R$ {valor:.2f}")
        print(f"Saque de R$ {valor:.2f} realizado com sucesso!")

def exibir_extrato():
    print("\n========== EXTRATO ==========")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        for item in extrato:
            print(item)
    print(f"Saldo atual: R$ {saldo:.2f}")
    print("=============================\n")

def menu():
    while True:
        print("\n=== Sistema Bancário ===")
        print("[1] Depósito")
        print("[2] Saque")
        print("[3] Extrato")
        print("[4] Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            valor = float(input("Informe o valor do depósito: R$ "))
            depositar(valor)

        elif opcao == "2":
            valor = float(input("Informe o valor do saque: R$ "))
            sacar(valor)

        elif opcao == "3":
            exibir_extrato()

        elif opcao == "4":
            print("Encerrando o sistema. Até mais!")
            break

        else:
            print("Opção inválida! Escolha uma opção válida.")

menu()

#teste actions