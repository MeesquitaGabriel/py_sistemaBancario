"""
Módulo que implementa as operações de uma conta bancária simples:
- Depósito
- Saque
- Impressão de extrato
"""

from constantes import LIMITE_SAQUE_VALOR, LIMITE_SAQUES


def mostrar_menu() -> str:
    """
    Exibe o menu e retorna a opção escolhida pelo usuário (em minúsculas).
    """
    menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """
    return input(menu).strip().lower()


def efetuar_deposito(saldo: float, extrato: list, valor: float) -> float:
    """
    Tenta depositar um valor na conta.
    Retorna o saldo atualizado. Em caso de valor inválido, mantém o saldo.
    """
    if valor <= 0:
        print("Operação falhou! O valor do depósito deve ser positivo.")
        return saldo

    saldo += valor
    extrato.append(f"Depósito: R$ {valor:.2f}")
    print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
    return saldo


def efetuar_saque(saldo: float, extrato: list, numero_saques: int, valor: float) -> (float, int):
    """
    Tenta sacar um valor da conta. Retorna uma tupla com (saldo_atualizado, número_de_saques_atualizado).
    Verifica se há saldo suficiente, se não excede o limite de saque por operação e se não ultrapassa o limite diário.
    """
    # Validações
    if valor <= 0:
        print("Operação falhou! O valor do saque deve ser positivo.")
        return saldo, numero_saques

    if numero_saques >= LIMITE_SAQUES:
        print("Operação falhou! Número máximo de saques diários excedido.")
        return saldo, numero_saques

    if valor > LIMITE_SAQUE_VALOR:
        print(f"Operação falhou! O valor do saque excede o limite de R$ {LIMITE_SAQUE_VALOR:.2f} por operação.")
        return saldo, numero_saques

    if valor > saldo:
        print("Operação falhou! Saldo insuficiente.")
        return saldo, numero_saques

    # Se todas as validações passarem:
    saldo -= valor
    numero_saques += 1
    extrato.append(f"Saque:    R$ {valor:.2f}")
    print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
    return saldo, numero_saques


def exibir_extrato(saldo: float, extrato: list) -> None:
    """
    Imprime o extrato de movimentações e o saldo atual.
    """
    print("\n================ EXTRATO ================")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        for linha in extrato:
            print(linha)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================\n")
