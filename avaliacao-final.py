conta = {
    "123456789" : 50,
    "abcdefghij" : 40
}

def autenticar():

    print("Digite sua senha:")
    senha_local = input()

    if senha_local in conta:
        print("Login bem-sucedido")
        return operacoes_bancarias(senha_local)
    else:
        print("Senha inválida. Tente novamente")
        return None
    
def verificar_saldo (senha_local):

    print("O saldo da sua conta é R$" + str(conta[senha_local]))
    return

def depositar (senha_local):

    print("Qual o valor que deseja depositar?")
    valor_local = int(input())

    conta[senha_local] = conta[senha_local] + valor_local

    print("A quantia de R$" + str(valor_local) + " foi adicionada ao saldo atual")
    print("O saldo atual é de R$" + str(conta[senha_local]))

    return

def retirar (senha_local):

    print("O saldo é de R$" + str(conta[senha_local]))
    print("Qual o valor que deseja retirar?")
    valor_local = int(input())

    if valor_local >= conta[senha_local]:
        print("O valor a retirar é maior que o saldo da conta: " + str(conta[senha_local]))
        print("Deseja retirar todo o dinheiro?\n"
              "(1): Sim\n"
              "(2): Não")
        opcao = int(input())

        if opcao == 1:
            conta[senha_local] = 0
        if opcao == 2:
            print("Nenhum valor foi retirado. Voltando ao menu")
            return
        else:
            print("Operação inválida")
    else:
        conta[senha_local] = conta[senha_local] - valor_local

    print("A quantia de R$" + str(valor_local) + " foi retirada da conta")
    print("O saldo atual é de R$" + str(conta[senha_local]))

    return

def operacoes_bancarias(senha_local):
    while True:

        print("Bem vindo ao menu de caixa eletrônico\n"
                "Digite uma das opções abaixo\n"
                "(1): Verificar saldo\n"
                "(2): Depositar dinheiro\n"
                "(3): Retirar dinheiro\n"
                "(4): Deslogar")
        opcao = int(input())

        if opcao == 1:
            verificar_saldo(senha_local)
        elif opcao == 2:
            depositar(senha_local)
        elif opcao == 3:
            retirar(senha_local)
        elif opcao == 4:
            print("Deslogando...")
            return None
        else:
            print("Operação inválida. Tente novamente")

while True:

    print("Digite uma das opções abaixo\n"
          "(1): Autenticar no sistema\n"
          "(2): Sair")
    opcao = int(input())

    if opcao == 1:
        senha = autenticar()
    elif opcao == 2:
        break
    else:
        print("Operação inválida. Tente novamente")