#  Import Pandas Biblioteca poderosa para manipulação e análise de dados.

# Criando arquivo csv
# import pandas as pd

# data = {
#     "Produto": ["Celular Android1","Celular Android2","Celular Android3"],
#     "Quantidade": [2,5,7],
#     "Preço": [1000,2000,3000]
# }


# df = pd.DataFrame(data)
# # esse codigo acima cria um dataframe que é basicamente uma tabela parecida com a do excel

# df.to_csv("vendas.csv",index=False)
# print("Arquivo Criado")
# index=false para tirar o indice do arquivo


# Ler e analisar arquivo csv 
import pandas as pd

df = pd.read_csv("vendas.csv")

# filtrando dados 
# df_celular = df[df["Produto"] == "Celular Android1"]

total_vendas = df.groupby("Produto")[["Quantidade"]].sum().reset_index()
# total de vendas
# df_total_vendas = total_vendas =  total_vendas.reset_index()

# df_total_vendas.to_csv("Total_de_vendas.csv", index=False)


soma_vendas = df["Quantidade"].sum()
# soma das vendas

# salvando os resultados em um novo csv 


print(soma_vendas)
# head() é usado para visualizar os primeiros registro do arquivo 
# se quisesse ver todos os registro do arquivo poderia usar o proprio df normal


