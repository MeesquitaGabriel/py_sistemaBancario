# py\_sistemaBancario

## Descrição do Projeto

O **py\_sistemaBancario** é um sistema bancário simples, desenvolvido em Python, que permite ao usuário realizar operações básicas de conta corrente, como depósito, saque e visualização de extrato. Focado em modularidade e legibilidade, o projeto está organizado em diferentes arquivos que se comunicam entre si, facilitando futuras extensões e manutenções.

## Funcionalidades

* **Depósito**: Adicionar valor positivo à conta.
* **Saque**: Retirar valor da conta, respeitando limite por operação e número máximo de saques diários.
* **Extrato**: Exibir todas as movimentações realizadas (depósito e saque), além do saldo atualizado.
* **Limites**:

  * Limite de saque por operação: R\$ 500,00.
  * Limite de saques por dia: 3.

## Estrutura de Arquivos

```
py_sistemaBancario/
├── constantes.py    # Define constantes do sistema (limites de saque)
├── conta.py         # Implementa as funções principais de operação bancária
└── main.py          # Script principal que controla o fluxo interativo do usuário
```

* **constantes.py**: Contém valores fixos, como `LIMITE_SAQUE_VALOR` e `LIMITE_SAQUES`.
* **conta.py**: Implementa funções para:

  * `mostrar_menu()`: Exibe opções ao usuário.
  * `efetuar_deposito(saldo, extrato, valor)`: Realiza depósitos.
  * `efetuar_saque(saldo, extrato, numero_saques, valor)`: Realiza saques, validando limites.
  * `exibir_extrato(saldo, extrato)`: Imprime o extrato e o saldo.
* **main.py**: Responsável por:

  * Inicializar variáveis de controle (saldo, extrato, número de saques).
  * Loop principal que lê a opção do usuário e chama funções adequadas.
  * Tratamento de exceções para entradas inválidas.

## Requisitos

* Python 3.6 ou superior.

Nenhuma biblioteca externa é necessária; o sistema utiliza apenas recursos da biblioteca padrão do Python.

## Instalação e Execução

1. **Clone** este repositório:

   ```bash
   git clone https://github.com/MeesquitaGabriel/py_sistemaBancario.git
   ```

2. **Navegue** até o diretório do projeto:

   ```bash
   cd py_sistemaBancario
   ```

3. **Execute** o script principal:

   ```bash
   python main.py
   ```

4. **Siga** as instruções exibidas no console:

   * Digite `d` para depósito.
   * Digite `s` para saque.
   * Digite `e` para visualizar o extrato.
   * Digite `q` para sair.

## Uso

Ao iniciar o sistema, o usuário vê um menu com as opções disponíveis. Em cada operação:

* **Depósito**: Digite `d` e informe o valor (ex.: `100.50` ou `100,50`).
* **Saque**: Digite `s` e informe o valor. O sistema checará:

  * Se o valor é positivo.
  * Se não ultrapassa R\$ 500,00 por operação.
  * Se ainda não atingiu o limite de 3 saques no dia.
  * Se há saldo suficiente.
* **Extrato**: Digite `e` para visualizar todas as movimentações realizadas até o momento e o saldo atual.
* **Sair**: Digite `q` para encerrar o programa.

## Exemplo de Sessão

```
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
=> d
Informe o valor do depósito: 200,00
Depósito de R$ 200.00 realizado com sucesso.

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
=> s
Informe o valor do saque: 50
Saque de R$ 50.00 realizado com sucesso.

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
=> e

================ EXTRATO ================
Depósito: R$ 200.00
Saque:    R$ 50.00

Saldo: R$ 150.00
==========================================

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
=> q
Obrigado por usar nosso sistema. Até logo!
```

## Possíveis Extensões

* Suporte a múltiplas contas simultâneas.
* Persistência de dados (banco de dados ou arquivo JSON) para manter histórico entre execuções.
* Autenticação de usuário (login/senha).
* Interface gráfica simples (Tkinter, PyQt ou outra).
* Transferência entre contas.
* Configuração dinâmica de limites por meio de arquivo de configuração.

## Contribuição

1. Faça um *fork* deste repositório.
2. Crie uma *branch* com sua feature ou correção: `git checkout -b minha-feature`.
3. Faça commit das mudanças: `git commit -m "Descrição da feature"`.
4. Envie para o repositório remoto: `git push origin minha-feature`.
5. Abra um *pull request* no GitHub.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE). Sinta-se à vontade para usar, modificar e distribuir conforme os termos da licença.

## Autor

**Gabriel Meesquita**

* GitHub: [MeesquitaGabriel](https://github.com/MeesquitaGabriel)
* Projeto original de exemplo e prática de modularização em Python.
