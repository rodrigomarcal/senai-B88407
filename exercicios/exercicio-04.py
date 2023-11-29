
def calculaCustoPorKm (tipoVeiculo):

    if tipoVeiculo == 1:
        custoPorKm = 0.5
    elif tipoVeiculo == 2:
        custoPorKm = 0.2
    elif tipoVeiculo == 3:
        custoPorKm = 0.1
    else:
        print("Tipo de veículo inválido")
        return None

    return custoPorKm

def calculaCustoTotal (custoPorKm, distancia):
    if custoPorKm == None:
        return "Viagem cancelada"
    return custoPorKm * distancia

tipoVeiculo = int(input("Com qual veículo que deseja viajar? Digite um dos seguintes números:\n"
                        "(1) --> Carro\n"
                        "(2) --> Moto\n"
                        "(3) --> Bicicleta\n"))

custoPorKm = calculaCustoPorKm(tipoVeiculo)

distancia = float(input("Qual a distância a ser percorrida (em quilômetros)? "))

print(calculaCustoTotal(custoPorKm, distancia))