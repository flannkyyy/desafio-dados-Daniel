import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("teste_indicium_precificacao.csv")
print(df.info())
print(df.describe())
plt.figure(figsize=(10,5))
sns.histplot(df["price"], bins=50, kde=True)
plt.xlim(0, 1000)
plt.title("Distribuição de Preços")
plt.xlabel("Preço (USD)")
plt.ylabel("Frequência")
plt.show()
