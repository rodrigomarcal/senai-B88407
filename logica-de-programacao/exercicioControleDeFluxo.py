print("Digite sua idade: ")
idade = input()
idade = int(idade)

print("Sua idade é:",idade)

if idade >= 60:
    print("Você é um idoso")
elif idade > 18:
    print("Você é adulto")
elif idade >= 12:
    print("Você é um adolescente")
elif idade > 2:
    print("Você é uma criança")
else:
    print("Você é um bebê")