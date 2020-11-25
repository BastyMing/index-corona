import pandas as pd
import matplotlib.pyplot as plt

workbook = "Casos.xlsx"

df = pd.read_excel(workbook)

print(df.head())

valores = df[["Dia", "Mes", "Casos"]]
print (valores)

ax = valores.plot.bar(x="Dia", y="Casos", rot=0)

plt.show()
