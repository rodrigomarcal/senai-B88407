# Operadores de comparação: usados para comparar dois valores
# o resultado das operações retornam True (verdadeiro) ou False (falso)

# == (igual)
# != (diferente) 
# > (maior que)
# < (menor que)
# >= (maior ou igual a)
# <= (menor ou igual a)

valor1 = 9
valor2 = 5

igual = valor1 == valor2
diferente = valor1 != valor2
maiorQue = valor1 > valor2
menorQue = valor1 < valor2
maiorOuIgual = valor1 >= valor2
menorOuIgual = valor1 <= valor2

print("{} é igual a {}? {}".format(valor1, valor2, igual))
print("{} é diferente de {}? {}".format(valor1, valor2, diferente))
print("{} é maior que {}? {}".format(valor1, valor2, maiorQue))
print("{} é menor que {}? {}".format(valor1, valor2, menorQue))
print("{} é maior ou igual a {}? {}".format(valor1, valor2, maiorOuIgual))
print("{} é menor ou igual a {}? {}\n".format(valor1, valor2, menorOuIgual))

# Operadores lógicos: usados combinar condições/comparações e retornar resultado True (verdadeiro) ou False (falso)
# and (e): resultado verdadeiro quando todas as condições são verdadeiras
# ou (ou): resultado verdadeiro quando pelo menos uma das condições é verdadeira
# not (negação): inverte o resultado obtido das condições

condicaoE = (valor1 > valor2) and (valor1 != valor2)
condicaoOu = (valor1 == valor2) or (valor1 < valor2) 
condicaoNot = not(valor1 == valor2)

print("Condição and (e): {} é maior que {} e diferente de {}? {}".format(valor1, valor2, valor2, condicaoE))
print("Condição or (ou): {} é igual a {} ou menor que {}? {}".format(valor1, valor2, valor2, condicaoOu))
print("Condição not (negação): {} é igual a {}? {}".format(valor1, valor2, condicaoNot))