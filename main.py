"""
Script principal que controla o fluxo da aplicação bancária.
"""

from conta import mostrar_menu, efetuar_deposito, efetuar_saque, exibir_extrato

def main():
    saldo = 0.0
    extrato = []       # lista de strings com as movimentações
    numero_saques = 0  # contador de saques realizados no dia

    while True:
        opcao = mostrar_menu()

        if opcao == "d":
            try:
                valor = float(input("Informe o valor do depósito: ").replace(",", "."))
            except ValueError:
                print("Operação falhou! Valor de depósito inválido.")
                continue

            saldo = efetuar_deposito(saldo, extrato, valor)

        elif opcao == "s":
            try:
                valor = float(input("Informe o valor do saque: ").replace(",", "."))
            except ValueError:
                print("Operação falhou! Valor de saque inválido.")
                continue

            saldo, numero_saques = efetuar_saque(saldo, extrato, numero_saques, valor)

        elif opcao == "e":
            exibir_extrato(saldo, extrato)

        elif opcao == "q":
            print("Obrigado por usar nosso sistema. Até logo!")
            break

        else:
            print("Operação inválida! Por favor, selecione uma das opções disponíveis.")

if __name__ == "__main__":
    main()
