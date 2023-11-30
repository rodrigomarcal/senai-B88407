#

dicionarioDeUsuarios = {
    "admin" : "admin"
}

# Função para cadastrar um novo usuário no sistema
def cadastrarUsuario (dicionarioDeUsuariosLocal):

    nomeUsuarioLocal = input("Digite um nome de usuário: ")
    
    if nomeUsuarioLocal in dicionarioDeUsuariosLocal:
        print("Esse nome de usuário já foi utilizado. Tente outro nome.")
        return cadastrarUsuario(dicionarioDeUsuariosLocal)
    else:
        senhaLocal = input("Digite uma nova senha: ")
        senhaLocalConfirmacao = input("Confirme sua senha: ")
        if senhaLocal == senhaLocalConfirmacao:
            return dicionarioDeUsuariosLocal.update({nomeUsuarioLocal : senhaLocal})
        else:
            print("As senhas não coincidem. Por favor tente novamente.")
            return cadastrarUsuario(dicionarioDeUsuariosLocal)

# Função para efetuar login do usuário
def loginUsuario (dicionarioDeUsuariosLocal):

    nomeDeUsuarioLocal = input("Digite seu nome de usuário: ")
    senhaLocal = input("Digite sua senha: ")

    if nomeDeUsuarioLocal in dicionarioDeUsuariosLocal:
        if dicionarioDeUsuariosLocal[nomeDeUsuarioLocal] == senhaLocal:
            print("Login bem-sucedido. Bem-vindo(a)", nomeDeUsuarioLocal + "!")
    else:
        print("Login ou senha inválidos.")

# Loop de menu principal (lobby de atendimento)

numeroDigitado = 0

while numeroDigitado != 3:
    
    numeroDigitado = int(input("Bem-vindo à central de atendimento."
                               "Solicite um dos serviços abaixo digitando um dos os seguintes números\n"
                               "(1): Cadastrar-se uma conta sistema.\n"
                               "(2): Acessar sua conta.\n"
                               "(3): Cancelar operação\n"))

    if numeroDigitado == 1:
        cadastrarUsuario(dicionarioDeUsuarios)
    elif numeroDigitado == 2:
        loginUsuario(dicionarioDeUsuarios)
    elif numeroDigitado == 3:
        break
    else:
        print("Solicitação de serviço inválida ou não listada. Tente novamente")

print(dicionarioDeUsuarios)