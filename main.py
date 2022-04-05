import pandas as pd
import json
from pandas import json_normalize
import warnings
warnings.simplefilter("ignore")

# Importando json e convertendo para dataframe do pandas
with open("db/basejson.json") as file:
    base = json.load(file)
df = json_normalize(base)

# Criando filtro para status 2 e dropando
dfFilter = df[df["status"] == 2].index
dfWithoutStatus2 = df.drop(dfFilter)

# Empréstimo 147
loan147 = dfWithoutStatus2[dfWithoutStatus2["loan"] == 147]
loan147["amount"] = loan147["amount"].astype(float)
loan147 = loan147.reset_index()
sumLoan147 = loan147["amount"].sum()

lote1_147 = 0.0
lote2_147 = 0.0
contador147 = 0
while True:
    print('Empréstimo 147\nLote 1 R$ 226.000,00')
    while lote1_147 < 226000.0:
        lote1_147 += loan147.at[contador147, "amount"]
        contador147 += 1
        print('Investimento: ' + loan147.at[contador147, "uuid"])

    print('\nEmpréstimo 147\nLote 2 R$ 164.000,00')
    while lote2_147 < 164000.0:
        lote2_147 += loan147.at[contador147, "amount"]
        print('Investimento: ' + loan147.at[contador147, "uuid"])
        contador147 += 1
    break

# Empréstimo 148
loan148 = dfWithoutStatus2[dfWithoutStatus2["loan"] == 148]
loan148["amount"] = loan148["amount"].astype(float)
loan148 = loan147.reset_index()
sumLoan148 = loan148["amount"].sum()

lote1_148 = 0.0
lote2_148 = 0.0
contador148 = 0
while True:
    print('\nEmpréstimo 148\nLote 1 R$ 94.000,00')
    while lote1_148 < 94000.0:
        lote1_148 += loan148.at[contador148, "amount"]
        contador148 += 1
        print('Investimento: ' + loan148.at[contador148, "uuid"])

    print('\nEmpréstimo 148\nLote 2 R$ 26.000,00')
    while lote2_148 < 26000.0:
        lote2_148 += loan148.at[contador148, "amount"]
        print('Investimento: ' + loan148.at[contador148, "uuid"])
        contador148 += 1

    break


