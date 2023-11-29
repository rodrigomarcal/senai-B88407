
dicionarioDeUsuarios = {
    "Aisha" : "@123MoonLight",
    "Fernando" : "euamopizzadechocolatecomfrangodecatupiry",
    "Rodrigo" : "meunomenaoehrodrigo"
    }

nomeDeUsuario = input("Digite seu nome de usuário: ")
senha = input("Digite sua senha: ")
    
if nomeDeUsuario in dicionarioDeUsuarios:
    if dicionarioDeUsuarios[nomeDeUsuario] == senha:
        print("Login bem-sucedido!")
else:
    print("Usuário ou senha inválidos!")

