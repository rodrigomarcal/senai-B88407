import pandas as pd

dados = pd.DataFrame(
    {
        "Produto" : ["Calça", "Camiseta", "Sapato", "Boné", "Bolsa"],
        "Janeiro" : [23, 17, 28, 39, 50],
        "Fevereiro" : [5, 87, 56, 23, 11],
        "Março" : [19, 5, 67, 24, 56],
        "Abril" : [45, 74, 29, 30, 14],
        "Maio" : [9, 10, 26, 56, 89],
        "Junho" : [18, 45, 23, 47, 34]
    }
)

print(dados, "\n")

# Obter índice da linha com o maior valor de quantidade de vendas em janeiro
indice_maior_venda_janeiro = dados["Janeiro"].idxmax()

# Obter o nome do produto mais vendido a partir do índice obtido anteriormente
produto_mais_vendido_janeiro = dados["Produto"][indice_maior_venda_janeiro]

# Índice das colunas de "Janeiro" e "Fevereiro"
indice_jan = dados.columns.get_loc("Janeiro")
indice_fev = dados.columns.get_loc("Fevereiro")

# Índice das linhas onde o produto é "Camiseta" (lista)
indice_camiseta = dados.index[dados["Produto"] == "Camiseta"].to_list()

# Cálculo do aumento percentual de janeiro para fevereiro
vendas_camisetas_jan = dados.iloc[indice_camiseta[0]][indice_jan]
vendas_camisetas_fev = dados.iloc[indice_camiseta[0]][indice_fev]

aumento = (vendas_camisetas_fev * 100) / vendas_camisetas_jan
print("O aumento foi de {:.2f}%".format(aumento))

i = 0
vendas_totais = []

for dado in dados.values:    

    total = 0
    for venda in dado:
        if type(venda) == int or type(venda) == float:
            total = total + venda
    vendas_totais.append(total)

print(vendas_totais)
print(max(vendas_totais))