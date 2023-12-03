# Central de atendimento de McDonalds

cardapioDeComidas = {
    "Big Mac" : 10.0,
    "McLanche Feliz" : 8.0,
    "Mcchicken" : 12.0
}

carrinho = {

}

def exibirMenu (cardapioDeComidasLocal):

    print("")
    numero = 1
    for lanche in cardapioDeComidasLocal:
        print("Opção ({}) {}: R$ {:.2f}".format(numero, lanche, cardapioDeComidasLocal[lanche]))
        numero += 1

def exibirPedido (cardapioDeComidasLocal, carrinhoLocal):

    print("")
    numero = 1
    precoTotal = 0

    print("--- PEDIDOS ---")

    # Checa se o dicionário 'carrinho' está vazio
    if not bool(carrinhoLocal):
            print("\nParece que carrinho está vazio :(")
            print("Você pode adicionar itens ao seu carrinho através da opção \"Adicionar um item ao carrinho\" no menu principal")
    else:        
        for lanche in carrinhoLocal:
            print("({}) {}: qtde: {}. Preço unitário: R$ {:.2f}. Preço total {:.2f}".format(
                numero, lanche, carrinhoLocal[lanche], cardapioDeComidas[lanche], (carrinhoLocal[lanche] * cardapioDeComidasLocal[lanche])
                ))
            numero += 1
            precoTotal = precoTotal + (carrinhoLocal[lanche] * cardapioDeComidasLocal[lanche])
        print("Preço total do pedido:", precoTotal)
    

def adicionarItem(cardapioDeComidasLocal, carrinhoLocal):

    print("")

    while True:

        busca = 1
        opcao = int(input("Qual item deseja adicionar? (Digite (0) para cancelar e retornar ao menu principal)\n: "))

        if opcao == 0:
            print("Cancelando operação...\n")
            break
        else:
            quantidade = int(input("Qual a quantidade que deseja levar? "))

            # Loop para procurar item no dicionário
            for lanche in cardapioDeComidasLocal.keys():

                if lanche in carrinhoLocal and busca == opcao:
                    carrinhoLocal[lanche] = carrinhoLocal[lanche] + quantidade
                else:
                    if busca == opcao:
                        carrinhoLocal.update({lanche : quantidade})
                        break
                busca += 1

            opcao = int(input("Deseja adicionar mais algum item?\n(1): Sim\n(2): Não\n: "))
            if opcao == 1:
                None
            elif opcao == 2:
                return
            else:
                print("Operação inválida. Retornando ao menu principal...")
                return

def removerItem(cardapioDeComidasLocal, carrinhoLocal):

    while True:

        if not bool(carrinhoLocal):
            print("\nVocê não possui nenhum item adicionado ao carrinho. Tente outra operação\n")
            break

        opcao = int(input("Qual item deseja remover? (Digite (0) para cancelar e retornar ao menu principal)\n: "))
        busca = 1

        if opcao == 0:
            print("Cancelando operação...\n")
            break
        else:
            # Loop para procurar item no dicionário
            for lanche in cardapioDeComidasLocal.keys():

                if lanche in carrinhoLocal and busca == opcao:
                    if carrinhoLocal[lanche] > 1:
                        print("Há mais de um item igual a esse no carrinho. O que deseja fazer?\n")

                        while True:
                            opcao = int(input(
                                "Digite uma das opções abaixo?\n(0): Cancelar operação e voltar ao menu de remoção.\n(1): Remover tudo.\n(2): Selecionar quantidade a remover.\n: "
                            ))

                            if opcao == 0:
                                break
                            elif opcao == 1:
                                opcao = int(input(
                                    "Deseja realmente remover o item do carrinho?\n" + "(1): Sim\n(2): Não.\n: "))
                                
                                if opcao == 1:
                                    carrinhoLocal.pop(lanche)
                                elif opcao == 2:
                                    print("Cancelando remoção...")
                                    break
                                else:
                                    print("Operação inválida.\nCancelando remoção...")
                            elif opcao == 2:
                                quantidade = int(input("Informe a quantidade a ser removida: "))

                                opcao = int(input(
                                    "Deseja realmente prosseguir com a remoção dos itens do carrinho?\n" + "(1): Sim\n(2): Não\n(3): Informar um valor diferente para remover\n: "))
                                
                                if opcao == 1:
                                    if quantidade >= carrinhoLocal[lanche]:
                                        carrinhoLocal.pop(lanche)
                                    elif quantidade < 1:
                                        break
                                    else:
                                        carrinhoLocal[lanche] = carrinhoLocal[lanche] - quantidade
                                elif opcao == 2:
                                    print("Cancelando remoção...\nVoltando ao menu principal...")
                                    return
                                elif opcao == 3:
                                    None
                                else:
                                    print("Operação inválida.\nCancelando remoção...")
                                    return

                            else:
                                print("Operação inválida. Tente novamente.")
                    else:
                        opcao = int(input("Deseja realmente remover {} do carrinho?\n".format(lanche) + "(1): Sim\n(2): Não\n: "))
                        
                        if opcao == 1:
                            carrinhoLocal.pop(lanche)
                            print("{} foi removido do carrinho.\nVoltando ao menu principal...".format(lanche))
                            return
                        elif opcao == 2:
                            print("Cancelando remoção...")
                            return
                        else:
                            print("Operação inválida.\nCancelando remoção...")
                            return

                busca += 1

    return

print("Bem-vindo à central de atendimento do MacDonalds. Solicite um dos serviços abaixo digitando o número referente\n")

while True:

    print("\nQual serviço deseja solicitar?\n")

    
    opcao = int(input("(1): Exibir cardápio de comidas\n(2): Exibir carrinho\n(3): Adicionar um item ao carrinho\n(4): Remover um item do carrinho.\n(5): Encerrar atendimento\n: "))
    
    if opcao == 1:
        exibirMenu(cardapioDeComidas)
    elif opcao == 2:
        exibirPedido(cardapioDeComidas, carrinho)
    elif opcao == 3:
        adicionarItem(cardapioDeComidas, carrinho)
        print(carrinho)
    elif opcao == 4:
        removerItem(cardapioDeComidas, carrinho)
    elif opcao == 5:
        print("\nEncerrando atendimento...")
        break
    else:
        print("Opção inválida. Tente novamente.")